from django import forms
from edc_sites.forms import SiteModelFormMixin
from edc_form_validators.form_validator_mixin import FormValidatorMixin
from inte_form_validators import RiskFactorsFormValidator

from ..models import RiskFactors


class RiskFactorsForm(SiteModelFormMixin, FormValidatorMixin, forms.ModelForm):
    form_validator_cls = RiskFactorsFormValidator

    class Meta:
        model = RiskFactors
        fields = "__all__"
