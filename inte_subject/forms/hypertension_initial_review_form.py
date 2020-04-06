from django import forms
from edc_action_item.forms.action_item_form_mixin import ActionItemFormMixin
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator

from ..models import HypertensionInitialReview


class HypertensionInitialReviewFormValidator(FormValidator):
    # TODO: add validation for M2M and other field, etc

    pass


class HypertensionInitialReviewForm(
    CrfModelFormMixin, ActionItemFormMixin, forms.ModelForm
):
    form_validator_cls = HypertensionInitialReviewFormValidator

    class Meta:
        model = HypertensionInitialReview
        fields = "__all__"
