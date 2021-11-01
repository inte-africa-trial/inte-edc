from django import forms
from edc_constants.constants import DM
from edc_dx_review.utils import raise_if_clinical_review_does_not_exist
from edc_form_validators.form_validator import FormValidator
from edc_visit_schedule.utils import raise_if_baseline

from ..models import Glucose
from .mixins import (
    CrfFormValidatorMixin,
    CrfModelFormMixin,
    GlucoseFormValidatorMixin,
    ResultFormValidatorMixin,
)


class GlucoseFormValidator(
    ResultFormValidatorMixin,
    GlucoseFormValidatorMixin,
    CrfFormValidatorMixin,
    FormValidator,
):
    def clean(self):
        if self.cleaned_data.get("subject_visit"):
            raise_if_baseline(self.cleaned_data.get("subject_visit"))
            raise_if_clinical_review_does_not_exist(self.cleaned_data.get("subject_visit"))
        self.validate_drawn_date_by_dx_date(DM, "Diabetes", drawn_date_fld="glucose_date")
        self.validate_glucose_test()


class GlucoseForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = GlucoseFormValidator

    class Meta:
        model = Glucose
        fields = "__all__"
