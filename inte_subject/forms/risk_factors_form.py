from django import forms
from edc_crf.modelform_mixins import CrfModelFormMixin

from ..form_validators import RiskFactorsFormValidator
from ..models import RiskFactors


class RiskFactorsForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = RiskFactorsFormValidator

    class Meta:
        model = RiskFactors
        fields = "__all__"
