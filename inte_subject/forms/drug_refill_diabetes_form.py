from django import forms
from edc_form_validators.form_validator import FormValidator

from ..models import DrugRefillDiabetes
from .mixins import (
    DrugRefillFormValidatorMixin,
    CrfModelFormMixin,
    CrfFormValidatorMixin,
)


class DrugRefillDiabetesFormValidator(
    DrugRefillFormValidatorMixin, CrfFormValidatorMixin, FormValidator
):
    pass


class DrugRefillDiabetesForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = DrugRefillDiabetesFormValidator

    class Meta:
        model = DrugRefillDiabetes
        fields = "__all__"
