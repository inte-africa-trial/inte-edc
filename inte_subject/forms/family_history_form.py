from django import forms
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator

from ..models import FamilyHistory
from .care_status_modelform_mixin import CareStatusRequiredModelFormMixin
from .crf_form_validator_mixin import CrfFormValidatorMixin


class FamilyHistoryFormValidator(CrfFormValidatorMixin, FormValidator):
    def clean(self):
        pass


class FamilyHistoryForm(
    CareStatusRequiredModelFormMixin, CrfModelFormMixin, forms.ModelForm
):

    form_validator_cls = FamilyHistoryFormValidator

    class Meta:
        model = FamilyHistory
        fields = "__all__"
