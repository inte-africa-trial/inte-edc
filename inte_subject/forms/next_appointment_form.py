from django import forms
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator
from inte_consent.models import SubjectConsent
from inte_screening.constants import (
    DIABETES_CLINIC,
    HIV_CLINIC,
    HYPERTENSION_CLINIC,
    NCD_CLINIC,
)

from ..models import (
    NextAppointment,
    HivInitialReview,
    DiabetesInitialReview,
    HypertensionInitialReview,
)
from .crf_form_validator_mixin import CrfFormValidatorMixin


class NextAppointmentValidator(CrfFormValidatorMixin, FormValidator):
    def clean(self):
        # hiv_clinic_appt_date
        condition = (
            self.clinic_type == HIV_CLINIC
            or HivInitialReview.objects.filter(
                subject_visit__appointment__subject_identifier=self.subject_identifier,
                subject_visit__report_datetime__lte=self.cleaned_data.get(
                    "report_datetime"
                ),
            ).exists()
        )
        self.required_if_true(condition, field_required="hiv_clinic_appt_date")
        self.date_not_before(
            "report_datetime", "hiv_clinic_appt_date", convert_to_date=True,
        )
        ncd_condition = (
            DiabetesInitialReview.objects.filter(
                subject_visit__appointment__subject_identifier=self.subject_identifier,
                subject_visit__report_datetime__lte=self.cleaned_data.get(
                    "report_datetime"
                ),
            ).exists()
            or HypertensionInitialReview.objects.filter(
                subject_visit__appointment__subject_identifier=self.subject_identifier,
                subject_visit__report_datetime__lte=self.cleaned_data.get(
                    "report_datetime"
                ),
            ).exists()
        )
        self.required_if_true(
            ncd_condition and self.clinic_type == NCD_CLINIC,
            field_required="ncd_clinic_appt_date",
        )
        self.date_not_before(
            "report_datetime", "ncd_clinic_appt_date", convert_to_date=True,
        )
        self.required_if_true(
            ncd_condition and self.clinic_type == DIABETES_CLINIC,
            field_required="diabetes_clinic_appt_date",
        )
        self.date_not_before(
            "report_datetime", "diabetes_clinic_appt_date", convert_to_date=True,
        )
        self.required_if_true(
            ncd_condition and self.clinic_type == HYPERTENSION_CLINIC,
            field_required="hypertension_clinic_appt_date",
        )
        self.date_not_before(
            "report_datetime", "hypertension_clinic_appt_date", convert_to_date=True,
        )

    @property
    def clinic_type(self):
        return SubjectConsent.objects.get(
            subject_identifier=self.subject_identifier
        ).clinic_type


class NextAppointmentForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = NextAppointmentValidator

    class Meta:
        model = NextAppointment
        fields = "__all__"
