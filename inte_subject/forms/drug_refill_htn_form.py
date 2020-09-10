from django import forms
from edc_form_validators.form_validator import FormValidator

from ..models import DrugRefillHtn
from .mixins import (
    DrugRefillFormValidatorMixin,
    CrfModelFormMixin,
    CrfFormValidatorMixin,
)


class DrugRefillHtnFormValidator(
    DrugRefillFormValidatorMixin, CrfFormValidatorMixin, FormValidator
):
    pass


class DrugRefillHtnForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = DrugRefillHtnFormValidator

    class Meta:
        model = DrugRefillHtn
        fields = "__all__"
