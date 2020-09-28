from django import forms
from edc_form_validators.form_validator import FormValidator

from ..models import Glucose
from .mixins import (
    CrfModelFormMixin,
    CrfFormValidatorMixin,
    GlucoseFormValidatorMixin,
    raise_if_baseline,
    raise_if_clinical_review_does_not_exist,
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
            raise_if_clinical_review_does_not_exist(
                self.cleaned_data.get("subject_visit")
            )
        self.validate_drawn_date_by_dx_date(
            "dm_dx_date", "Diabetes", drawn_date_fld="glucose_date"
        )
        self.validate_glucose_test()


class GlucoseForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = GlucoseFormValidator

    class Meta:
        model = Glucose
        fields = "__all__"
