from django import forms
from django.apps import apps as django_apps
from django.core.exceptions import ObjectDoesNotExist
from edc_constants.constants import OTHER, YES
from edc_crf.modelform_mixins import CrfModelFormMixin as BaseCrfModelFormMixin
from edc_model import models as edc_models
from edc_model.models import InvalidFormat
from edc_utils import age
from edc_visit_schedule.constants import DAY1
from inte_subject.models import Medications

from ..models import ClinicalReviewBaseline


def model_exists_or_raise(form, model_cls=None):
    subject_identifier = form.cleaned_data.get("subject_visit").subject_identifier
    try:
        model_cls.objects.get(subject_visit__subject_identifier=subject_identifier)
    except ObjectDoesNotExist:
        raise forms.ValidationError(
            f"Complete the `{model_cls._meta.verbose_name}` CRF first."
        )
    return True


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
    """Asserts Baseline Clinical Review exists"""

    def clean(self):
        if self._meta.model != ClinicalReviewBaseline and self.cleaned_data.get(
            "subject_visit"
        ):
            model_exists_or_raise(self, model_cls=ClinicalReviewBaseline)
        return super().clean()


class CrfModelFormMixin(
    ClinicalReviewBaselineRequiredModelFormMixin, BaseCrfModelFormMixin
):
    pass


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
                raise forms.ValidationError(
                    f"Missing drug. Also expected {display_name}."
                )


class DrugRefillFormValidatorMixin:
    def clean(self):
        medications_exists_or_raise(self.cleaned_data.get("subject_visit"))
        if (
            self.cleaned_data.get("subject_visit")
            and self.cleaned_data.get("subject_visit").appointment.visit_code == DAY1
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
                self.estimated_date_from_ago("dx_ago")
                - self.cleaned_data.get("glucose_date")
            ).days > 1:
                raise forms.ValidationError(
                    {"glucose_date": "Invalid. Cannot be before diagnosis."}
                )
        self.required_if(YES, field="glucose_performed", field_required="glucose")
        self.required_if(
            YES, field="glucose_performed", field_required="glucose_quantifier"
        )
        self.required_if(YES, field="glucose_performed", field_required="glucose_units")


class ReviewFormValidatorMixin:
    def validate_test_and_care_dates(self):
        if self.cleaned_data.get("test_date") and self.cleaned_data.get(
            "care_start_date"
        ):
            if (
                self.cleaned_data.get("test_date")
                - self.cleaned_data.get("care_start_date")
            ).days > 1:
                raise forms.ValidationError(
                    {"care_start_date": "Invalid. Cannot be before test date."}
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
            subject_identifier = self.cleaned_data.get(
                "subject_visit"
            ).subject_identifier
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
