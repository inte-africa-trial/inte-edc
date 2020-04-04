from django import forms
from edc_action_item.forms.action_item_form_mixin import ActionItemFormMixin
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator

from ..models import DiabetesInitialReview


class DiabetesInitialReviewFormValidator(FormValidator):
    def clean(self):

        self.required_if_true(
            self.cleaned_data.get("glucose"), field_required="glucose_units",
        )
        self.required_if_true(
            self.cleaned_data.get("glucose"), field_required="glucose_quantifier",
        )
        self.required_if_true(
            self.cleaned_data.get("glucose"), field_required="glucose_datetime",
        )
        self.required_if_true(
            self.cleaned_data.get("glucose_datetime"), field_required="glucose",
        )


class DiabetesInitialReviewForm(
    CrfModelFormMixin, ActionItemFormMixin, forms.ModelForm
):
    form_validator_cls = DiabetesInitialReviewFormValidator

    class Meta:
        model = DiabetesInitialReview
        fields = "__all__"
