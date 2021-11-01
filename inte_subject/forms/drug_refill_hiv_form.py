from django import forms
from edc_form_validators.form_validator import FormValidator

from ..models import DrugRefillHiv
from .mixins import (
    CrfFormValidatorMixin,
    CrfModelFormMixin,
    DrugRefillFormValidatorMixin,
    validate_total_days,
)


class DrugRefillHivFormValidator(
    DrugRefillFormValidatorMixin, CrfFormValidatorMixin, FormValidator
):
    pass


class DrugRefillHivForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = DrugRefillHivFormValidator

    def clean(self):
        validate_total_days(self, return_in_days=self.cleaned_data.get("return_in_days"))

    class Meta:
        model = DrugRefillHiv
        fields = "__all__"
