from django import forms
from edc_form_validators.form_validator import FormValidator
from respond_forms.utils import raise_if_clinical_review_does_not_exist

from ..models import FamilyHistory
from .mixins import CrfFormValidatorMixin, CrfModelFormMixin


class FamilyHistoryFormValidator(CrfFormValidatorMixin, FormValidator):
    def clean(self):
        raise_if_clinical_review_does_not_exist(self.cleaned_data.get("subject_visit"))


class FamilyHistoryForm(CrfModelFormMixin, forms.ModelForm):

    form_validator_cls = FamilyHistoryFormValidator

    class Meta:
        model = FamilyHistory
        fields = "__all__"
