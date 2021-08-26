from django import forms
from edc_form_validators.form_validator import FormValidator

from ..models import DrugRefillHtn
from .mixins import (
    CrfFormValidatorMixin,
    CrfModelFormMixin,
    DrugRefillFormValidatorMixin,
    validate_total_days,
)


class DrugRefillHtnFormValidator(
    DrugRefillFormValidatorMixin, CrfFormValidatorMixin, FormValidator
):
    pass


class DrugRefillHtnForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = DrugRefillHtnFormValidator

    def clean(self):
        validate_total_days(self, return_in_days=self.cleaned_data.get("return_in_days"))

    class Meta:
        model = DrugRefillHtn
        fields = "__all__"
