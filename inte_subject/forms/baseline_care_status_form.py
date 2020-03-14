from django import forms
from edc_constants.constants import YES
from edc_crf.modelform_mixins import CrfModelFormMixin
from inte_screening.constants import HIV_CLINIC, NCD_CLINIC

from ..form_validators import BaselineCareStatusFormValidator
from ..models import BaselineCareStatus


class BaselineCareStatusForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = BaselineCareStatusFormValidator

    def clean(self):
        cleaned_data = super().clean()
        self.validate_enroled_clinic_vs_attending_clinic()
        return cleaned_data

    def validate_enroled_clinic_vs_attending_clinic(self):
        """Care status clinic type at screening and consent must
        match response to attending clinic"""
        if (
            self.cleaned_data.get("receives_care_at_hiv_clinic") != YES
            and self.primary_enrolment_clinic == HIV_CLINIC
        ):
            raise forms.ValidationError(
                {
                    "receives_care_at_hiv_clinic": "Subject was enrolled from an HIV Clinic."
                }
            )

        if (
            self.cleaned_data.get("receives_care_at_ncd_clinic") != YES
            and self.primary_enrolment_clinic == NCD_CLINIC
        ):
            raise forms.ValidationError(
                {
                    "receives_care_at_ncd_clinic": "Subject was enrolled from an NCD Clinic."
                }
            )

    @property
    def primary_enrolment_clinic(self):
        obj = self.get_consent(
            subject_identifier=self.subject_visit.subject_identifier,
            report_datetime=self.cleaned_data.get("report_datetime"),
        )
        return obj.clinic_type

    class Meta:
        model = BaselineCareStatus
        fields = "__all__"
