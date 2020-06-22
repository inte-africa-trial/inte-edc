from django import forms
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_constants.constants import FORMER_SMOKER, YES
from edc_form_validators.form_validator import FormValidator

from ..models import HealthRiskAssessment


class HealthRiskAssessmentFormValidator(FormValidator):
    def clean(self):

        self.required_if(
            FORMER_SMOKER, field="smoking_status", field_required="smoker_quit_ago"
        )

        self.applicable_if(YES, field="alcohol", field_applicable="alcohol_consumption")


class HealthRiskAssessmentForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = HealthRiskAssessmentFormValidator

    class Meta:
        model = HealthRiskAssessment
        fields = "__all__"
