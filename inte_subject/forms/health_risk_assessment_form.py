from django import forms
from edc_crf.modelform_mixins import CrfModelFormMixin

from ..form_validators import HealthRiskAssessmentFormValidator
from ..models import HealthRiskAssessment


class HealthRiskAssessmentForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = HealthRiskAssessmentFormValidator

    class Meta:
        model = HealthRiskAssessment
        fields = "__all__"
