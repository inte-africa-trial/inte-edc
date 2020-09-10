from django import forms
from edc_form_validators.form_validator import FormValidator

from ..models import DrugRefillDm
from .mixins import (
    DrugRefillFormValidatorMixin,
    CrfModelFormMixin,
    CrfFormValidatorMixin,
)


class DrugRefillDmFormValidator(
    DrugRefillFormValidatorMixin, CrfFormValidatorMixin, FormValidator
):
    pass


class DrugRefillDmForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = DrugRefillDmFormValidator

    class Meta:
        model = DrugRefillDm
        fields = "__all__"
