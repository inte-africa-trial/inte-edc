from django import forms
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_constants.constants import FORMER_SMOKER, YES
from edc_form_validators.form_validator import FormValidator

from ..models import OtherBaselineData
from .care_status_modelform_mixin import CareStatusRequiredModelFormMixin


class OtherBaselineDataFormValidator(FormValidator):
    def clean(self):

        self.required_if(
            FORMER_SMOKER, field="smoking_status", field_required="smoker_quit_ago"
        )

        self.applicable_if(YES, field="alcohol", field_applicable="alcohol_consumption")


class OtherBaselineDataForm(
    CareStatusRequiredModelFormMixin, CrfModelFormMixin, forms.ModelForm
):
    form_validator_cls = OtherBaselineDataFormValidator

    class Meta:
        model = OtherBaselineData
        fields = "__all__"
