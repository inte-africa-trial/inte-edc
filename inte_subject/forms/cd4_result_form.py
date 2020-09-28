from django import forms
from django.conf import settings
from edc_form_validators.form_validator import FormValidator
from edc_utils import convert_php_dateformat
from inte_subject.diagnoses import Diagnoses, InitialReviewRequired

from ..models import Cd4Result
from .mixins import (
    CrfFormValidatorMixin,
    CrfModelFormMixin,
    raise_if_baseline,
    raise_if_clinical_review_does_not_exist,
    ResultFormValidatorMixin,
)


class Cd4ResultFormValidator(
    ResultFormValidatorMixin, CrfFormValidatorMixin, FormValidator
):
    def clean(self):
        if self.cleaned_data.get("subject_visit"):
            raise_if_baseline(self.cleaned_data.get("subject_visit"))
            raise_if_clinical_review_does_not_exist(
                self.cleaned_data.get("subject_visit")
            )
        self.validate_drawn_date_by_dx_date("hiv_dx_date", "HIV infection")


class Cd4ResultForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = Cd4ResultFormValidator

    class Meta:
        model = Cd4Result
        fields = "__all__"
