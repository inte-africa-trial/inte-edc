from django import forms
from edc_form_validators.form_validator import FormValidator

from ..models import ClinicalReview
from .mixins import (
    EstimatedDateFromAgoFormMixin,
    CrfModelFormMixin,
    CrfFormValidatorMixin,
)


class ClinicalReviewFormValidator(CrfFormValidatorMixin, FormValidator):
    def clean(self):
        pass


class ClinicalReviewForm(CrfModelFormMixin, forms.ModelForm):

    form_validator_cls = ClinicalReviewFormValidator

    class Meta:
        model = ClinicalReview
        fields = "__all__"
