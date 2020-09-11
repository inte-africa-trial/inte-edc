from django import forms
from edc_form_validators.form_validator import FormValidator

from ..models import HtnReview
from .mixins import (
    ReviewFormValidatorMixin,
    BPFormValidatorMixin,
    CrfModelFormMixin,
    CrfFormValidatorMixin,
)


class HtnReviewFormValidator(
    ReviewFormValidatorMixin, BPFormValidatorMixin, CrfFormValidatorMixin, FormValidator
):
    def clean(self):
        self.validate_bp_reading(
            "sys_blood_pressure", "dia_blood_pressure",
        )
        self.validate_test_and_care_dates()


class HtnReviewForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = HtnReviewFormValidator

    class Meta:
        model = HtnReview
        fields = "__all__"
