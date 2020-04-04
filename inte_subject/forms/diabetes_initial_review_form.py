from django import forms
from edc_action_item.forms.action_item_form_mixin import ActionItemFormMixin
from edc_constants.constants import YES, NO
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator

from ..models import DiabetesInitialReview


class DiabetesInitialReviewFormValidator(FormValidator):
    def clean(self):

        self.required_if(
            NO,
            field="glucose_measurement_taken",
            field_required="glucose_measurement_reason_not_taken",
        )

        self.required_if(
            YES, field="glucose_measurement_taken", field_required="glucose"
        )
        self.required_if(
            YES, field="glucose_measurement_taken", field_required="glucose_quantifier"
        )
        self.required_if(
            YES, field="glucose_measurement_taken", field_required="glucose_units"
        )


class DiabetesInitialReviewForm(
    CrfModelFormMixin, ActionItemFormMixin, forms.ModelForm
):
    form_validator_cls = DiabetesInitialReviewFormValidator

    class Meta:
        model = DiabetesInitialReview
        fields = "__all__"
