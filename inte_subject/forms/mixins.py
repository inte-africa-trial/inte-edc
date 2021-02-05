from django import forms
from django.apps import apps as django_apps
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from edc_constants.constants import NEVER, NO, OTHER, YES
from edc_crf.modelform_mixins import CrfModelFormMixin as BaseCrfModelFormMixin
from edc_model import models as edc_models
from edc_model.models import InvalidFormat
from edc_utils import age, convert_php_dateformat

from inte_prn.icc_registered import (
    InterventionSiteNotRegistered,
    is_icc_registered_site,
)
from inte_sites.is_intervention_site import NotInterventionSite
from inte_visit_schedule.is_baseline import is_baseline

from ..diagnoses import Diagnoses, InitialReviewRequired, MultipleInitialReviewsExist
from ..models import (
    ClinicalReview,
    ClinicalReviewBaseline,
    HivInitialReview,
    HivReview,
    Medications,
)


def art_initiation_date(subject_identifier=None, report_datetime=None):
    """Returns date initiated on ART or None"""
    art_date = None
    try:
        initial_review = HivInitialReview.objects.get(
            subject_visit__subject_identifier=subject_identifier,
            report_datetime__lte=report_datetime,
        )
    except ObjectDoesNotExist:
        pass
    else:
        if initial_review.arv_initiated == YES:
            art_date = initial_review.best_art_initiation_date
        else:
            for review in HivReview.objects.filter(
                subject_visit__subject_identifier=subject_identifier,
                report_datetime__lte=report_datetime,
            ).order_by("-report_datetime"):
                if review.arv_initiated == YES:
                    art_date = review.arv_initiation_actual_date
                    break
    return art_date


def model_exists_or_raise(subject_visit=None, model_cls=None, singleton=None):
    singleton = False if singleton is None else singleton
    if singleton:
        opts = {"subject_visit__subject_identifier": subject_visit.subject_identifier}
    else:
        opts = {"subject_visit": subject_visit}
    try:
        model_cls.objects.get(**opts)
    except ObjectDoesNotExist:
        raise forms.ValidationError(
            f"Complete the `{model_cls._meta.verbose_name}` CRF first."
        )
    return True


def raise_if_baseline(subject_visit):
    if subject_visit and is_baseline(subject_visit=subject_visit):
        raise forms.ValidationError("This form is not available for completion at baseline.")


def raise_if_clinical_review_does_not_exist(subject_visit):
    if subject_visit:
        if is_baseline(subject_visit):
            model_exists_or_raise(
                subject_visit=subject_visit,
                model_cls=ClinicalReviewBaseline,
            )
        else:
            model_exists_or_raise(subject_visit=subject_visit, model_cls=ClinicalReview)


def medications_exists_or_raise(subject_visit):
    if subject_visit:
        try:
            Medications.objects.get(subject_visit=subject_visit)
        except ObjectDoesNotExist:
            raise forms.ValidationError(
                f"Complete the `{Medications._meta.verbose_name}` CRF first."
            )
    return True


def validate_total_days(form, return_in_days=None):
    return_in_days = return_in_days or form.cleaned_data.get("return_in_days")
    if (
        form.cleaned_data.get("clinic_days")
        and form.cleaned_data.get("club_days")
        and form.cleaned_data.get("purchased_days")
        and int(return_in_days or 0)
    ):
        total = (
            form.cleaned_data.get("clinic_days")
            or 0 + form.cleaned_data.get("club_days")
            or 0 + form.cleaned_data.get("purchased_days")
            or 0
        )
        if total != int(return_in_days or 0):
            raise forms.ValidationError(
                f"Patient to return for a drug refill in {return_in_days} days. "
                "Check that the total days match."
            )


class ClinicalReviewBaselineRequiredModelFormMixin:
    """Asserts Baseline Clinical Review exists or raise"""

    def clean(self):
        if self._meta.model != ClinicalReviewBaseline and self.cleaned_data.get(
            "subject_visit"
        ):
            model_exists_or_raise(
                subject_visit=self.cleaned_data.get("subject_visit"),
                model_cls=ClinicalReviewBaseline,
                singleton=True,
            )
        return super().clean()


class CrfModelFormMixin(ClinicalReviewBaselineRequiredModelFormMixin, BaseCrfModelFormMixin):
    pass


class ReviewFormValidatorMixin:
    def validate_care_delivery(self):
        is_applicable, applicable_msg, not_applicable_msg = self.get_integration_info()
        self.applicable_if_true(
            is_applicable,
            field_applicable="care_delivery",
            applicable_msg=applicable_msg,
            not_applicable_msg=not_applicable_msg,
        )
        self.required_if(NO, field="care_delivery", field_required="care_delivery_other")

    def get_integration_info(self):
        applicable = False
        applicable_msg = None
        not_applicable_msg = None
        model_cls = django_apps.get_model("inte_prn.integratedcareclinicregistration")
        try:
            is_icc_registered_site(report_datetime=self.report_datetime)
        except NotInterventionSite:
            not_applicable_msg = "This site was not selected for integrated care"
        except InterventionSiteNotRegistered:
            not_applicable_msg = (
                "This site's integrated care clinic is NOT open. "
                f"See facility form {model_cls._meta.verbose_name}."
            )

        else:
            applicable = True
            applicable_msg = "This site's integrated care clinic is open."
        return applicable, applicable_msg, not_applicable_msg


class EstimatedDateFromAgoFormMixin:
    def estimated_date_from_ago(self, f1):
        """Returns the estimated date using `duration_to_date` or None."""
        estimated_date = None
        if self.cleaned_data.get(f1):
            try:
                estimated_date = edc_models.duration_to_date(
                    self.cleaned_data.get(f1),
                    self.cleaned_data.get("report_datetime").date(),
                )
            except InvalidFormat as e:
                raise forms.ValidationError({f1: str(e)})
        return estimated_date


class DrugSupplyNcdFormMixin:

    list_model_cls = None

    def clean(self):
        cleaned_data = super().clean()
        data = dict(self.data.lists())
        rx = self.list_model_cls.objects.filter(id__in=data.get("rx") or [])
        rx_names = [obj.display_name for obj in rx]
        inline_drug_names = self.raise_on_duplicates()

        validate_total_days(self)

        if (
            self.cleaned_data.get("drug")
            and self.cleaned_data.get("drug").display_name not in rx_names
        ):
            treatment = " + ".join(rx_names)
            raise forms.ValidationError(
                f"Invalid. `{self.cleaned_data.get('drug').display_name}` "
                f"not in current treatment of `{treatment}`"
            )

        self.raise_on_missing_drug(rx_names, inline_drug_names)

        return cleaned_data

    def raise_on_duplicates(self):
        drug_names = []
        total_forms = self.data.get(f"{self.relation_label}_set-TOTAL_FORMS")
        for form_index in range(0, int(total_forms or 0)):
            inline_rx_id = self.data.get(f"{self.relation_label}_set-{form_index}-drug")
            if inline_rx_id:
                rx_obj = self.list_model_cls.objects.get(id=int(inline_rx_id))
                if rx_obj.display_name in drug_names:
                    raise forms.ValidationError("Invalid. Duplicates not allowed")
                drug_names.append(rx_obj.display_name)
        return drug_names

    @staticmethod
    def raise_on_missing_drug(rx_names, inline_drug_names):
        for display_name in rx_names:
            if display_name not in inline_drug_names:
                raise forms.ValidationError(f"Missing drug. Also expected {display_name}.")


class DrugRefillFormValidatorMixin:
    def clean(self):
        medications_exists_or_raise(self.cleaned_data.get("subject_visit"))
        if (
            self.cleaned_data.get("subject_visit")
            and is_baseline(self.cleaned_data.get("subject_visit"))
            and self.cleaned_data.get("rx_modified") == YES
        ):
            raise forms.ValidationError({"rx_modified": "Expected `No` at baseline."})

        self.m2m_other_specify(
            OTHER, m2m_field="modifications", field_other="modifications_other"
        )
        self.m2m_other_specify(
            OTHER,
            m2m_field="modification_reasons",
            field_other="modification_reasons_other",
        )


class GlucoseFormValidatorMixin:
    def validate_glucose_test(self):
        if self.cleaned_data.get("glucose_date") and self.cleaned_data.get("dx_ago"):
            if (
                self.estimated_date_from_ago("dx_ago") - self.cleaned_data.get("glucose_date")
            ).days > 1:
                raise forms.ValidationError(
                    {"glucose_date": "Invalid. Cannot be before diagnosis."}
                )
        self.required_if(YES, field="glucose_performed", field_required="glucose")
        self.required_if(YES, field="glucose_performed", field_required="glucose_quantifier")
        self.required_if(YES, field="glucose_performed", field_required="glucose_units")


class InitialReviewFormValidatorMixin:
    def raise_if_both_ago_and_actual_date(self):
        if self.cleaned_data.get("dx_ago") and self.cleaned_data.get("dx_date"):
            raise forms.ValidationError(
                {
                    "dx_ago": (
                        "Date conflict. Do not provide a response "
                        "here if the exact data of diagnosis is available."
                    )
                }
            )


class BPFormValidatorMixin:
    def validate_bp_reading(self, sys_field, dia_field):
        if self.cleaned_data.get(sys_field) and self.cleaned_data.get(dia_field):
            if self.cleaned_data.get(sys_field) < self.cleaned_data.get(dia_field):
                raise forms.ValidationError(
                    {dia_field: "Systolic must be greater than diastolic."}
                )


class CrfFormValidatorMixin:

    consent_model_cls = "inte_consent.subjectconsent"
    screening_model_cls = "inte_screening.subjectscreening"

    @property
    def age_in_years(self):
        return age(self.subject_consent.dob, self.report_datetime).years

    @property
    def subject_screening(self):
        subject_screening_model_cls = django_apps.get_model(self.screening_model_cls)
        return subject_screening_model_cls.objects.get(
            subject_identifier=self.subject_identifier
        )

    @property
    def primary_enrolment_clinic_type(self):
        return self.subject_screening.clinic_type

    @property
    def subject_identifier(self):
        try:
            subject_identifier = self.instance.subject_visit.subject_idenfifier
        except AttributeError:
            subject_identifier = self.cleaned_data.get("subject_visit").subject_identifier
        return subject_identifier

    @property
    def subject_consent(self):
        subject_consent_model_cls = django_apps.get_model(self.consent_model_cls)
        return subject_consent_model_cls.objects.get(
            subject_identifier=self.subject_identifier
        )

    @property
    def report_datetime(self):
        return self.cleaned_data.get("subject_visit").report_datetime


class ResultFormValidatorMixin:
    def validate_drawn_date_by_dx_date(self, attr, dx_msg_label, drawn_date_fld=None):
        drawn_date_fld = drawn_date_fld or "drawn_date"
        dx = Diagnoses(subject_visit=self.cleaned_data.get("subject_visit"), lte=True)
        try:
            dx_date = getattr(dx, attr)
        except InitialReviewRequired:
            dx_date = None
        if not dx_date:
            raise forms.ValidationError(
                "This form is not relevant. "
                f"Subject has not been diagnosed with {dx_msg_label}."
            )
        else:
            if dx_date > self.cleaned_data.get(drawn_date_fld):
                formatted_date = dx_date.strftime(
                    convert_php_dateformat(settings.SHORT_DATE_FORMAT)
                )
                raise forms.ValidationError(
                    {
                        "drawn_date": (
                            "Invalid. Subject was diagnosed with "
                            f"{dx_msg_label} on {formatted_date}."
                        )
                    }
                )


class MedicationAdherenceFormValidatorMixin:
    def clean(self):
        raise_if_clinical_review_does_not_exist(self.cleaned_data.get("subject_visit"))
        self.not_required_if(
            NEVER, field="last_missed_pill", field_required="missed_pill_reason"
        )
        self.m2m_other_specify(
            m2m_field="missed_pill_reason", field_other="other_missed_pill_reason"
        )


class DiagnosisFormValidatorMixin:
    def get_diagnoses(self):
        diagnoses = Diagnoses(
            subject_identifier=self.subject_identifier,
            report_datetime=self.report_datetime,
        )
        try:
            diagnoses.initial_reviews
        except InitialReviewRequired as e:
            raise forms.ValidationError(e)
        except MultipleInitialReviewsExist as e:
            raise forms.ValidationError(e)
        return diagnoses

    def applicable_if_not_diagnosed(
        self, diagnoses=None, field_dx=None, field_applicable=None, label=None
    ):
        diagnoses = diagnoses or self.get_diagnoses()

        self.applicable_if_true(
            getattr(diagnoses, field_dx) != YES,
            field_applicable=field_applicable,
            applicable_msg=(
                f"Patient was not previously diagnosed with {label}. " "Expected YES or NO."
            ),
            not_applicable_msg=f"Patient was previously diagnosed with {label}.",
        )

    def applicable_if_diagnosed(
        self, diagnoses=None, field_dx=None, field_applicable=None, label=None
    ):
        diagnoses = diagnoses or self.get_diagnoses()
        # htn
        self.applicable_if_true(
            getattr(diagnoses, field_dx) == YES,
            field_applicable=field_applicable,
            applicable_msg=(
                f"Patient was previously diagnosed with {label}. " "Expected YES or NO."
            ),
            not_applicable_msg=f"Patient was not previously diagnosed with {label}.",
        )
