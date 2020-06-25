from django import forms
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator

from ..models import DrugRefillDiabetes


class DrugRefillDiabetesFormValidator(FormValidator):
    def clean(self):
        pass


class DrugRefillDiabetesForm(
    CrfModelFormMixin, forms.ModelForm,
):
    form_validator_cls = DrugRefillDiabetesFormValidator

    class Meta:
        model = DrugRefillDiabetes
        fields = "__all__"
