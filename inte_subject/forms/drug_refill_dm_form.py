from django import forms
from edc_form_validators.form_validator import FormValidator

from ..models import DrugRefillDm
from .mixins import (
    CrfFormValidatorMixin,
    CrfModelFormMixin,
    DrugRefillFormValidatorMixin,
    validate_total_days,
)


class DrugRefillDmFormValidator(
    DrugRefillFormValidatorMixin, CrfFormValidatorMixin, FormValidator
):
    pass


class DrugRefillDmForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = DrugRefillDmFormValidator

    def clean(self):
        validate_total_days(self, return_in_days=self.cleaned_data.get("return_in_days"))

    class Meta:
        model = DrugRefillDm
        fields = "__all__"
