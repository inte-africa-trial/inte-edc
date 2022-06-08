from django import forms
from edc_constants.constants import HIV
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator
from edc_visit_schedule.utils import raise_if_baseline
from respond_forms.form_validator_mixins import ResultFormValidatorMixin
from respond_forms.utils import raise_if_clinical_review_does_not_exist

from ..models import Hba1cResult
from .mixins import CrfFormValidatorMixin


class Hba1cResultFormValidator(ResultFormValidatorMixin, CrfFormValidatorMixin, FormValidator):
    def clean(self):
        raise_if_baseline(self.cleaned_data.get("subject_visit"))
        raise_if_clinical_review_does_not_exist(self.cleaned_data.get("subject_visit"))
        self.validate_drawn_date_by_dx_date(HIV, "HIV infection")


class Hba1cResultForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = Hba1cResultFormValidator

    class Meta:
        model = Hba1cResult
        fields = "__all__"
