from django import forms
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator

from ..models import DrugRefillHiv
from .mixins import DrugRefillFormValidatorMixin


class DrugRefillHivFormValidator(DrugRefillFormValidatorMixin, FormValidator):
    pass


class DrugRefillHivForm(
    CrfModelFormMixin, forms.ModelForm,
):
    form_validator_cls = DrugRefillHivFormValidator

    class Meta:
        model = DrugRefillHiv
        fields = "__all__"
