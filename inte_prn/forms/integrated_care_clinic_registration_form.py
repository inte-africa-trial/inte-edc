from django import forms
from edc_sites.forms import SiteModelFormMixin
from edc_form_validators.form_validator_mixin import FormValidatorMixin
from edc_form_validators.form_validator import FormValidator
from inte_sites.is_intervention_site import is_intervention_site

from ..models import IntegratedCareClinicRegistration


class IntegratedCareClinicRegistrationFormValidator(FormValidator):
    pass


class IntegratedCareClinicRegistrationForm(
    SiteModelFormMixin, FormValidatorMixin, forms.ModelForm
):

    form_validator_cls = IntegratedCareClinicRegistrationFormValidator

    def clean(self):
        cleaned_data = super().clean()
        if not is_intervention_site():
            raise forms.ValidationError(
                "Wait! This site is NOT an intervention site. Check randomization."
            )
        return cleaned_data

    class Meta:
        model = IntegratedCareClinicRegistration
        fields = "__all__"
