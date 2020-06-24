from django import forms
from edc_constants.constants import YES
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator

from ..models import Complications
from .crf_form_validator_mixin import CrfFormValidatorMixin


class ComplicationsFormValidator(CrfFormValidatorMixin, FormValidator):
    def clean(self):
        self.required_if(YES, field="stroke", field_required="stroke_ago")
        self.required_if(YES, field="heart_attack", field_required="heart_attack_ago")
        self.required_if(YES, field="renal_disease", field_required="renal_disease_ago")
        self.required_if(YES, field="vision", field_required="vision_ago")
        self.required_if(YES, field="numbness", field_required="numbness_ago")
        self.required_if(YES, field="foot_ulcers", field_required="foot_ulcers_ago")
        self.required_if(
            YES, field="complications", field_required="complications_other"
        )


class ComplicationsForm(CrfModelFormMixin, forms.ModelForm):

    form_validator_cls = ComplicationsFormValidator

    class Meta:
        model = Complications
        fields = "__all__"
