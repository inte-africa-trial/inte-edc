from django import forms
from edc_constants.constants import OTHER, YES
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator

from ..models import Investigations


class InvestigationsFormValidator(FormValidator):
    def clean(self):
        condition = (
            self.cleaned_data.get("hiv_tested") == YES
            or self.cleaned_data.get("hypertension_tested") == YES
            or self.cleaned_data.get("diabtetes_tested") == YES
        )
        self.required_if_true(condition, field_required="reason")
        self.m2m_other_specify(OTHER, m2m_field="reason", field_other="reason_other")
        self.required_if_true(condition, field_required="test_date")


class InvestigationsForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = InvestigationsFormValidator

    class Meta:
        model = Investigations
        fields = "__all__"
