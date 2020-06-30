from django import forms
from edc_action_item.forms.action_item_form_mixin import ActionItemFormMixin
from edc_constants.constants import OTHER, YES
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator
from inte_screening.constants import HIV_CLINIC

from ..models import HivInitialReview
from .crf_form_validator_mixin import CrfFormValidatorMixin
from .care_status_modelform_mixin import CareStatusRequiredModelFormMixin
from .mixins import EstimatedDateFromAgoFormMixin


class HivInitialReviewFormValidator(
    EstimatedDateFromAgoFormMixin, CrfFormValidatorMixin, FormValidator
):
    def clean(self):
        if (
            self.subject_screening.clinic_type in [HIV_CLINIC]
            and self.cleaned_data.get("receives_care") != YES
        ):
            raise forms.ValidationError(
                {
                    "receives_care": (
                        "Patient was screened from an HIV clinic, expected `Yes`."
                    ),
                }
            )

        self.applicable_if(YES, field="receives_care", field_applicable="clinic")
        self.required_if(OTHER, field="clinic", field_required="clinic_other")
        self.required_if(
            YES, field="receives_care", field_required="arv_initiation_ago"
        )

        if self.cleaned_data.get("dx_ago") and self.cleaned_data.get(
            "arv_initiation_ago"
        ):
            if self.estimated_date_from_ago(
                "arv_initiation_ago"
            ) < self.estimated_date_from_ago("dx_ago"):
                raise forms.ValidationError(
                    {
                        "arv_initiation_ago": "Invalid. Cannot start ART before HIV diagnosis"
                    }
                )

        self.required_if(YES, field="receives_care", field_required="has_vl")
        self.required_if(YES, field="has_vl", field_required="vl")
        self.required_if(YES, field="has_vl", field_required="vl_date")
        if self.cleaned_data.get("vl_date") and self.cleaned_data.get("dx_ago"):
            if self.cleaned_data.get("vl_date") < self.estimated_date_from_ago(
                "dx_ago"
            ):
                raise forms.ValidationError(
                    {"vl_date": "Invalid. Cannot be before HIV diagnosis"}
                )
        self.required_if(YES, field="receives_care", field_required="has_cd4")
        self.required_if(YES, field="has_cd4", field_required="cd4")
        self.required_if(YES, field="has_cd4", field_required="cd4_date")
        if self.cleaned_data.get("cd4_date") and self.cleaned_data.get("dx_ago"):
            if self.cleaned_data.get("cd4_date") < self.estimated_date_from_ago(
                "dx_ago"
            ):
                raise forms.ValidationError(
                    {"cd4_date": "Invalid. Cannot be before HIV diagnosis"}
                )


class HivInitialReviewForm(
    CareStatusRequiredModelFormMixin,
    CrfModelFormMixin,
    ActionItemFormMixin,
    forms.ModelForm,
):
    form_validator_cls = HivInitialReviewFormValidator

    class Meta:
        model = HivInitialReview
        fields = "__all__"
