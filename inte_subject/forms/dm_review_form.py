from django import forms
from edc_form_validators.form_validator import FormValidator

from ..models import DmReview
from .mixins import (
    GlucoseFormValidatorMixin,
    raise_if_clinical_review_does_not_exist,
    CrfModelFormMixin,
    CrfFormValidatorMixin,
)


class DmReviewFormValidator(
    GlucoseFormValidatorMixin, CrfFormValidatorMixin, FormValidator,
):
    def clean(self):
        raise_if_clinical_review_does_not_exist(self.cleaned_data.get("subject_visit"))
        self.validate_glucose_test()


class DmReviewForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = DmReviewFormValidator

    class Meta:
        model = DmReview
        fields = "__all__"
