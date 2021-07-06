from django import forms
from django.apps import apps as django_apps
from django.contrib.sites.models import Site
from django.core.exceptions import ObjectDoesNotExist
from edc_constants.constants import FREE_OF_CHARGE, NEVER, NO, OTHER, YES
from edc_crf.modelform_mixins import CrfModelFormMixin as BaseCrfModelFormMixin
from edc_model import models as edc_models
from edc_model.models import InvalidFormat
from edc_utils import age
from edc_visit_schedule.utils import is_baseline
from respond_forms.utils import (
    medications_exists_or_raise,
    model_exists_or_raise,
    raise_if_clinical_review_does_not_exist,
    validate_total_days,
)

from inte_lists.models import DrugPaySources
from inte_prn.icc_registered import (
    InterventionSiteNotRegistered,
    is_icc_registered_site,
)
from inte_prn.models import IntegratedCareClinicRegistration
from inte_sites.is_intervention_site import NotInterventionSite, is_intervention_site

from ..models import ClinicalReviewBaseline


def raise_if_intervention_site_without_icc_registration():
    if is_intervention_site():
        try:
            IntegratedCareClinicRegistration.objects.get(site_id=Site.objects.get_current())
        except ObjectDoesNotExist:
            raise forms.ValidationError(
                "This is an intervention site. Complete the "
                f"`{IntegratedCareClinicRegistration._meta.verbose_name}` form first."
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


class MedicationAdherenceFormValidatorMixin:
    def clean(self):
        raise_if_clinical_review_does_not_exist(self.cleaned_data.get("subject_visit"))
        self.not_required_if(
            NEVER, field="last_missed_pill", field_required="missed_pill_reason"
        )
        self.m2m_other_specify(
            m2m_field="missed_pill_reason", field_other="other_missed_pill_reason"
        )


class HealthEconomicsFormValidatorMixin:
    def clean_education(self):
        cond = (
            self.cleaned_data.get("education_in_years") is not None
            and self.cleaned_data.get("education_in_years") > 0
        )

        if cond and self.cleaned_data.get("education_in_years") > self.age_in_years:
            raise forms.ValidationError(
                {
                    "education_in_years": (
                        "Cannot exceed subject's age. "
                        f"Got subject is {self.age_in_years} years old."
                    )
                }
            )

        self.required_if_true(cond, field_required="education_certificate")

        self.applicable_if_true(cond, field_applicable="primary_school")
        self.required_if(
            YES,
            field="primary_school",
            field_required="primary_school_in_years",
            field_required_evaluate_as_int=True,
        )
        self.applicable_if_true(cond, field_applicable="secondary_school")
        self.required_if(
            YES,
            field="secondary_school",
            field_required="secondary_school_in_years",
            field_required_evaluate_as_int=True,
        )
        self.applicable_if_true(cond, field_applicable="higher_education")
        self.required_if(
            YES,
            field="higher_education",
            field_required="higher_education_in_years",
            field_required_evaluate_as_int=True,
        )

    def clean_recv_drugs_by_duration(self, duration):
        conditions = [
            ("dm", "diabetes"),
            ("htn", "hypertension"),
            ("hiv", "HIV"),
            ("other", None),
        ]
        diagnoses = self.get_diagnoses()
        for cond, label in conditions:

            if cond == "other":
                self.applicable_if(
                    YES,
                    field=f"received_rx_{duration}",
                    field_applicable=f"rx_{cond}_{duration}",
                )
            else:
                if self.cleaned_data.get(f"received_rx_{duration}") == YES:
                    self.applicable_if_diagnosed(
                        diagnoses=diagnoses,
                        field_dx=f"{cond}_dx",
                        field_applicable=f"rx_{cond}_{duration}",
                        label=label,
                    )
                else:
                    self.applicable_if(
                        YES,
                        field=f"received_rx_{duration}",
                        field_applicable=f"rx_{cond}_{duration}",
                    )

            self.m2m_required_if(
                response=YES,
                field=f"rx_{cond}_{duration}",
                m2m_field=f"rx_{cond}_paid_{duration}",
            )
            self.m2m_single_selection_if(
                FREE_OF_CHARGE, m2m_field=f"rx_{cond}_paid_{duration}"
            )
            self.m2m_other_specify(
                OTHER,
                m2m_field=f"rx_{cond}_paid_{duration}",
                field_other=f"rx_{cond}_paid_{duration}_other",
            )
            self.m2m_other_specify(
                *[
                    obj.name
                    for obj in DrugPaySources.objects.all()
                    if obj.name != FREE_OF_CHARGE
                ],
                m2m_field=f"rx_{cond}_paid_{duration}",
                field_other=f"rx_{cond}_cost_{duration}",
                field_other_evaluate_as_int=True,
            )
