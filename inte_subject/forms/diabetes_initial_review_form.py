from django import forms
from edc_action_item.forms.action_item_form_mixin import ActionItemFormMixin
from edc_constants.constants import YES
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator

from ..constants import INSULIN, DRUGS
from ..models import DiabetesInitialReview
from .care_status_modelform_mixin import CareStatusRequiredModelFormMixin
from .mixins import EstimatedDateFromAgoFormMixin


class DiabetesInitialReviewFormValidator(EstimatedDateFromAgoFormMixin, FormValidator):
    def clean(self):
        self.required_if(
            DRUGS, INSULIN, field="managed_by", field_required="med_start_ago",
        )

        if self.cleaned_data.get("med_start_ago") and self.cleaned_data.get("dx_ago"):
            if (
                self.estimated_date_from_ago("dx_ago")
                - self.estimated_date_from_ago("med_start_ago")
            ).days > 1:
                raise forms.ValidationError(
                    {"med_start_ago": "Invalid. Cannot be before diagnosis."}
                )
        self.required_if(YES, field="glucose_performed", field_required="glucose_date")
        if self.cleaned_data.get("glucose_date") and self.cleaned_data.get("dx_ago"):
            if (
                self.estimated_date_from_ago("dx_ago")
                - self.cleaned_data.get("glucose_date")
            ).days > 1:
                raise forms.ValidationError(
                    {"glucose_date": "Invalid. Cannot be before diagnosis."}
                )
        self.required_if(YES, field="glucose_performed", field_required="glucose")
        self.required_if(
            YES, field="glucose_performed", field_required="glucose_quantifier"
        )
        self.required_if(YES, field="glucose_performed", field_required="glucose_units")


class DiabetesInitialReviewForm(
    CareStatusRequiredModelFormMixin,
    CrfModelFormMixin,
    ActionItemFormMixin,
    forms.ModelForm,
):
    form_validator_cls = DiabetesInitialReviewFormValidator

    class Meta:
        model = DiabetesInitialReview
        fields = "__all__"
