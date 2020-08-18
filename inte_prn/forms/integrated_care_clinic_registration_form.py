from django import forms
from edc_sites.forms import SiteModelFormMixin
from edc_form_validators.form_validator_mixin import FormValidatorMixin
from edc_form_validators.form_validator import FormValidator

from ..models import IntegratedCareClinicRegistration


class IntegratedCareClinicRegistrationFormValidator(FormValidator):
    pass


class IntegratedCareClinicRegistrationForm(
    SiteModelFormMixin, FormValidatorMixin, forms.ModelForm
):

    form_validator_cls = IntegratedCareClinicRegistrationFormValidator

    class Meta:
        model = IntegratedCareClinicRegistration
        fields = "__all__"
