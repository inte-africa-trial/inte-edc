from django import forms
from edc_form_validators.form_validator import FormValidator

from ..models import FamilyHistory
from .mixins import CrfModelFormMixin, CrfFormValidatorMixin


class FamilyHistoryFormValidator(CrfFormValidatorMixin, FormValidator):
    def clean(self):
        pass


class FamilyHistoryForm(CrfModelFormMixin, forms.ModelForm):

    form_validator_cls = FamilyHistoryFormValidator

    class Meta:
        model = FamilyHistory
        fields = "__all__"
