from django import forms
from edc_action_item.forms.action_item_form_mixin import ActionItemFormMixin
from edc_constants.constants import YES
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator

from ..models import Anthropometry


class AnthropometryFormValidator(FormValidator):
    def clean(self):
        self.required_if(YES, field="r2_taken", field_required="sys_blood_pressure_r2")
        self.required_if(YES, field="r2_taken", field_required="dia_blood_pressure_r2")


class AnthropometryForm(CrfModelFormMixin, ActionItemFormMixin, forms.ModelForm):
    form_validator_cls = AnthropometryFormValidator

    class Meta:
        model = Anthropometry
        fields = "__all__"
