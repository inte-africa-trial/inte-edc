from django import forms
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator

from ..models import DrugRefillHypertension


class DrugRefillHypertensionFormValidator(FormValidator):
    def clean(self):
        pass


class DrugRefillHypertensionForm(
    CrfModelFormMixin, forms.ModelForm,
):
    form_validator_cls = DrugRefillHypertensionFormValidator

    class Meta:
        model = DrugRefillHypertension
        fields = "__all__"
