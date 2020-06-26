from django import forms
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator

from ..models import HivReview
from .mixins import ReviewFormValidatorMixin


class HivReviewFormValidator(ReviewFormValidatorMixin, FormValidator):
    def clean(self):
        self.validate_test_and_care_dates()


class HivReviewForm(
    CrfModelFormMixin, forms.ModelForm,
):
    form_validator_cls = HivReviewFormValidator

    class Meta:
        model = HivReview
        fields = "__all__"
