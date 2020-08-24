from django import forms
from edc_form_validators.form_validator import FormValidator

from ..models import DrugRefillHypertension
from .mixins import (
    DrugRefillFormValidatorMixin,
    CrfModelFormMixin,
    CrfFormValidatorMixin,
)


class DrugRefillHypertensionFormValidator(
    DrugRefillFormValidatorMixin, CrfFormValidatorMixin, FormValidator
):
    pass


class DrugRefillHypertensionForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = DrugRefillHypertensionFormValidator

    class Meta:
        model = DrugRefillHypertension
        fields = "__all__"
