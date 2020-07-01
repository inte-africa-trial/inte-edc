from django import forms
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator

from ..models import DrugRefillHiv
from .mixins import DrugRefillFormValidatorMixin, validate_total_days


class DrugRefillHivFormValidator(DrugRefillFormValidatorMixin, FormValidator):
    def clean(self):
        validate_total_days(
            self, return_in_days=self.cleaned_data.get("return_in_days")
        )


class DrugRefillHivForm(
    CrfModelFormMixin, forms.ModelForm,
):
    form_validator_cls = DrugRefillHivFormValidator

    class Meta:
        model = DrugRefillHiv
        fields = "__all__"
