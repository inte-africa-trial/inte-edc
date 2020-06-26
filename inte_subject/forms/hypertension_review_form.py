from django import forms
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator

from ..models import HypertensionReview
from .mixins import ReviewFormValidatorMixin, BPFormValidatorMixin


class HypertensionReviewFormValidator(
    ReviewFormValidatorMixin, BPFormValidatorMixin, FormValidator
):
    def clean(self):
        self.validate_bp_reading(
            "sys_blood_pressure", "dia_blood_pressure",
        )
        self.validate_test_and_care_dates()


class HypertensionReviewForm(
    CrfModelFormMixin, forms.ModelForm,
):
    form_validator_cls = HypertensionReviewFormValidator

    class Meta:
        model = HypertensionReview
        fields = "__all__"
