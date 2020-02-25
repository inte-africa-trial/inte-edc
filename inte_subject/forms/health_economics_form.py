from django import forms
from edc_sites.forms import SiteModelFormMixin
from edc_form_validators.form_validator_mixin import FormValidatorMixin

from ..form_validators import HealthEconomicsValidator
from ..models import HealthEconomics


class HealthEconomicsForm(SiteModelFormMixin, FormValidatorMixin, forms.ModelForm):
    form_validator_cls = HealthEconomicsValidator

    class Meta:
        model = HealthEconomics
        fields = "__all__"
