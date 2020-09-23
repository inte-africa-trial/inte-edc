from django import forms
from edc_form_validators.form_validator import FormValidator

from ..models import HivReview
from .mixins import (
    raise_if_clinical_review_does_not_exist,
    ReviewFormValidatorMixin,
    CrfModelFormMixin,
    CrfFormValidatorMixin,
)


class HivReviewFormValidator(
    ReviewFormValidatorMixin, CrfFormValidatorMixin, FormValidator
):
    def clean(self):
        raise_if_clinical_review_does_not_exist(self.cleaned_data.get("subject_visit"))
        self.validate_test_and_care_dates()


class HivReviewForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = HivReviewFormValidator

    class Meta:
        model = HivReview
        fields = "__all__"
