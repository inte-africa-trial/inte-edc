from django import forms
from edc_form_validators.form_validator import FormValidator

from ..models import DmReview
from .mixins import (
    GlucoseFormValidatorMixin,
    ReviewFormValidatorMixin,
    CrfModelFormMixin,
    CrfFormValidatorMixin,
)


class DmReviewFormValidator(
    ReviewFormValidatorMixin,
    GlucoseFormValidatorMixin,
    CrfFormValidatorMixin,
    FormValidator,
):
    def clean(self):
        self.validate_test_and_care_dates()
        self.validate_glucose_test()


class DmReviewForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = DmReviewFormValidator

    class Meta:
        model = DmReview
        fields = "__all__"
