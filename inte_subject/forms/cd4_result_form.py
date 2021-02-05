import pdb

from django import forms
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator

from ..models import Cd4Result
from .mixins import (  # CrfModelFormMixin,
    CrfFormValidatorMixin,
    ResultFormValidatorMixin,
    raise_if_baseline,
    raise_if_clinical_review_does_not_exist,
)


class Cd4ResultFormValidator(ResultFormValidatorMixin, CrfFormValidatorMixin, FormValidator):
    def clean(self):
        raise_if_baseline(self.cleaned_data.get("subject_visit"))
        raise_if_clinical_review_does_not_exist(self.cleaned_data.get("subject_visit"))
        self.validate_drawn_date_by_dx_date("hiv_dx_date", "HIV infection")


class Cd4ResultForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = Cd4ResultFormValidator

    class Meta:
        model = Cd4Result
        fields = "__all__"
