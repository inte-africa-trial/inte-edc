from django import forms
from edc_action_item.forms.action_item_form_mixin import ActionItemFormMixin
from edc_constants.constants import OTHER, YES
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator
from inte_screening.constants import HIV_CLINIC

from ..models import HivInitialReview
from .care_status_exists_or_raise import care_status_exists_or_raise
from .crf_form_validator_mixin import CrfFormValidatorMixin


class HivInitialReviewFormValidator(CrfFormValidatorMixin, FormValidator):
    def clean(self):
        care_status_exists_or_raise(self)
        if (
            self.subject_screening.clinic_type in [HIV_CLINIC]
            and self.cleaned_data.get("receives_care") != YES
        ):
            raise forms.ValidationError(
                {
                    "receives_care": "Patient was screened from an HIV clinic, expected `Yes`.",
                }
            )

        self.applicable_if(YES, field="receives_care", field_applicable="clinic")
        self.required_if(OTHER, field="clinic", field_required="clinic_other")
        self.required_if(
            YES, field="receives_care", field_required="clinic_next_appt_date"
        )
        self.required_if(
            YES, field="receives_care", field_required="arv_initiation_ago"
        )
        self.required_if(YES, field="receives_care", field_required="has_vl")
        self.required_if(YES, field="has_vl", field_required="vl")
        self.required_if(YES, field="has_vl", field_required="vl_date")
        self.required_if(YES, field="receives_care", field_required="has_cd4")
        self.required_if(YES, field="has_cd4", field_required="cd4")
        self.required_if(YES, field="has_cd4", field_required="cd4_date")
        self.required_if(
            YES, field="receives_care", field_required="current_arv_regimen"
        )
        self.validate_other_specify(
            field="current_arv_regimen", other_specify_field="other_current_arv_regimen"
        )


class HivInitialReviewForm(CrfModelFormMixin, ActionItemFormMixin, forms.ModelForm):
    form_validator_cls = HivInitialReviewFormValidator

    class Meta:
        model = HivInitialReview
        fields = "__all__"
