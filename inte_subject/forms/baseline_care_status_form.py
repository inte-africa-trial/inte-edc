import pdb

from django import forms

from edc_consent.modelform_mixins import RequiresConsentModelFormMixin
from edc_constants.constants import YES
from edc_sites.forms import SiteModelFormMixin
from edc_form_validators.form_validator_mixin import FormValidatorMixin
from edc_visit_tracking.modelform_mixins import VisitTrackingModelFormMixin
from inte_form_validators import BaselineCareStatusFormValidator
from inte_screening.constants import HIV_CLINIC, NCD_CLINIC

from ..constants import HIV, NCD
from ..models import BaselineCareStatus


class BaselineCareStatusForm(
    SiteModelFormMixin, RequiresConsentModelFormMixin, FormValidatorMixin, forms.ModelForm
):
    form_validator_cls = BaselineCareStatusFormValidator

    def clean(self):
        cleaned_data = super().clean()

        if self.cleaned_data.get("attending_hiv_clinic") != YES and self.enroled_from_clinic(HIV):
            raise forms.ValidationError(
                {"attending_hiv_clinic": "Subject was enrolled from an HIV Clinic."
                 }
            )

        if self.cleaned_data.get("attending_ncd_clinic") != YES and self.enroled_from_clinic(NCD):
            raise forms.ValidationError(
                {"attending_hiv_clinic": "Subject was enrolled from an HIV Clinic."
                 }
            )

        return cleaned_data

    @property
    def appointment(self):
        return self.subject_visit.appointment

    @property
    def subject_visit(self):
        return self.cleaned_data.get("subject_visit")

    def enroled_from_clinic(self):
        consent = self.get_consent(subject_identifier=self.subject_visit.subject_identifier,
                                   report_datetime=self.cleaned_data.get("report_datetime"))
        if consent.clinic_type == HIV_CLINIC:
            return HIV
        elif consent.clinic_type == NCD_CLINIC:
            return NCD
        return None

    class Meta:
        model = BaselineCareStatus
        fields = "__all__"
