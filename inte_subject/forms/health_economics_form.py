from django import forms
from edc_crf.modelform_mixins import CrfModelFormMixin

from ..form_validators import HealthEconomicsValidator
from ..models import HealthEconomics


class HealthEconomicsForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = HealthEconomicsValidator

    class Meta:
        model = HealthEconomics
        fields = "__all__"
