from django import forms
from edc_sites.forms import SiteModelFormMixin
from edc_action_item.forms.action_item_form_mixin import ActionItemFormMixin
from edc_form_validators.form_validator_mixin import FormValidatorMixin
from edc_form_validators.form_validator import FormValidator

from ..models import HivInitialReview


class HivInitialReviewFormValidator(FormValidator):
    pass


class HivInitialReviewForm(
    SiteModelFormMixin, FormValidatorMixin, ActionItemFormMixin, forms.ModelForm
):

    form_validator_cls = HivInitialReviewFormValidator

    class Meta:
        model = HivInitialReview
        fields = "__all__"
