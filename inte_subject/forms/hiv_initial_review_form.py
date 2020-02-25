from django import forms
from edc_action_item.forms.action_item_form_mixin import ActionItemFormMixin
from edc_form_validators.form_validator import FormValidator

from ..models import HivInitialReview
from .form_mixins import SubjectModelFormMixin


class HivInitialReviewFormValidator(FormValidator):
    pass


class HivInitialReviewForm(SubjectModelFormMixin, ActionItemFormMixin, forms.ModelForm):
    form_validator_cls = HivInitialReviewFormValidator

    class Meta:
        model = HivInitialReview
        fields = "__all__"
