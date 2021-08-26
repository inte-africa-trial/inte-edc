from django import forms
from edc_blood_results import BloodResultsFormValidatorMixin
from edc_constants.constants import NO, YES
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators import FormValidator
from edc_lab_panel.panels import hba1c_panel

from ..models import BloodResultsHba1c


class BloodResultsHba1cFormValidator(BloodResultsFormValidatorMixin, FormValidator):
    panel = hba1c_panel

    def clean(self) -> None:
        self.required_if(NO, field="performed", field_required="not_performed_reason")
        self.required_if(YES, field="performed", field_required="is_poc")
        super().clean()


class BloodResultsHba1cForm(CrfModelFormMixin, forms.ModelForm):

    form_validator_cls = BloodResultsHba1cFormValidator

    class Meta:
        model = BloodResultsHba1c
        fields = "__all__"
