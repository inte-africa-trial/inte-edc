from django import forms
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator

from ..models import DiabetesReview
from .mixins import GlucoseFormValidatorMixin, ReviewFormValidatorMixin


class DiabetesReviewFormValidator(
    ReviewFormValidatorMixin, GlucoseFormValidatorMixin, FormValidator
):
    def clean(self):
        self.validate_test_and_care_dates()
        self.validate_glucose_test()


class DiabetesReviewForm(
    CrfModelFormMixin, forms.ModelForm,
):
    form_validator_cls = DiabetesReviewFormValidator

    class Meta:
        model = DiabetesReview
        fields = "__all__"
