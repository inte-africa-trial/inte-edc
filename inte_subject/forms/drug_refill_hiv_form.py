from django import forms
from edc_form_validators.form_validator import FormValidator
from respond_forms.utils import validate_total_days

from ..models import DrugRefillHiv
from .mixins import (
    CrfFormValidatorMixin,
    CrfModelFormMixin,
    DrugRefillFormValidatorMixin,
)


class DrugRefillHivFormValidator(
    DrugRefillFormValidatorMixin, CrfFormValidatorMixin, FormValidator
):
    def clean(self):
        validate_total_days(self, return_in_days=self.cleaned_data.get("return_in_days"))


class DrugRefillHivForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = DrugRefillHivFormValidator

    class Meta:
        model = DrugRefillHiv
        fields = "__all__"
