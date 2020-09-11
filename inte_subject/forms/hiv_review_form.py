from django import forms
from edc_form_validators.form_validator import FormValidator

from ..models import HivReview
from .mixins import ReviewFormValidatorMixin, CrfModelFormMixin, CrfFormValidatorMixin


class HivReviewFormValidator(
    ReviewFormValidatorMixin, CrfFormValidatorMixin, FormValidator
):
    def clean(self):
        self.validate_test_and_care_dates()


class HivReviewForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = HivReviewFormValidator

    class Meta:
        model = HivReview
        fields = "__all__"
