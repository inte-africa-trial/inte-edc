from django import forms
from edc_form_validators.form_validator import FormValidator

from ..models import ViralLoadResult
from .mixins import (
    CrfModelFormMixin,
    CrfFormValidatorMixin,
    raise_if_baseline,
    raise_if_clinical_review_does_not_exist,
    ResultFormValidatorMixin,
)


class ViralLoadResultFormValidator(
    ResultFormValidatorMixin, CrfFormValidatorMixin, FormValidator
):
    def clean(self):
        if self.cleaned_data.get("subject_visit"):
            raise_if_baseline(self.cleaned_data.get("subject_visit"))
            raise_if_clinical_review_does_not_exist(
                self.cleaned_data.get("subject_visit")
            )
        self.validate_drawn_date_by_dx_date("hiv_dx_date", "HIV infection")


class ViralLoadResultForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = ViralLoadResultFormValidator

    class Meta:
        model = ViralLoadResult
        fields = "__all__"
