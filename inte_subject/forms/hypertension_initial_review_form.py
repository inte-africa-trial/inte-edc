from django import forms
from edc_action_item.forms.action_item_form_mixin import ActionItemFormMixin
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator

from ..constants import DRUGS
from ..models import HypertensionInitialReview
from .care_status_exists_or_raise import care_status_exists_or_raise


class HypertensionInitialReviewFormValidator(FormValidator):
    def clean(self):
        self.required_if(DRUGS, field="managed_by", field_required="med_start_ago")


class HypertensionInitialReviewForm(
    CrfModelFormMixin, ActionItemFormMixin, forms.ModelForm
):
    form_validator_cls = HypertensionInitialReviewFormValidator

    def clean(self):
        care_status_exists_or_raise(self)
        return super().clean()

    class Meta:
        model = HypertensionInitialReview
        fields = "__all__"
