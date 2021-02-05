from django import forms
from edc_form_validators.form_validator import FormValidator

from ..models import HtnReview
from .mixins import (
    BPFormValidatorMixin,
    CrfFormValidatorMixin,
    CrfModelFormMixin,
    ReviewFormValidatorMixin,
    raise_if_clinical_review_does_not_exist,
)


class HtnReviewFormValidator(
    ReviewFormValidatorMixin, BPFormValidatorMixin, CrfFormValidatorMixin, FormValidator
):
    def clean(self):
        raise_if_clinical_review_does_not_exist(self.cleaned_data.get("subject_visit"))
        self.validate_care_delivery()
        self.validate_bp_reading(
            "sys_blood_pressure",
            "dia_blood_pressure",
        )


class HtnReviewForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = HtnReviewFormValidator

    class Meta:
        model = HtnReview
        fields = "__all__"
