from django import forms
from django.core.exceptions import ObjectDoesNotExist
from edc_action_item.forms.action_item_form_mixin import ActionItemFormMixin
from edc_constants.constants import NO, NOT_REQUIRED, YES
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator
from inte_subject.models import HypertensionInitialReview

from ..models import Indicators
from .care_status_modelform_mixin import CareStatusRequiredModelFormMixin
from .mixins import BPFormValidatorMixin


class IndicatorsFormValidator(BPFormValidatorMixin, FormValidator):
    def clean(self):
        self.required_if(YES, field="r1_taken", field_required="sys_blood_pressure_r1")
        self.required_if(NO, field="r1_taken", field_required="r1_reason_not_taken")
        self.required_if(YES, field="r1_taken", field_required="dia_blood_pressure_r1")
        self.validate_bp_reading(
            "sys_blood_pressure_r1", "dia_blood_pressure_r1",
        )
        if (
            self.cleaned_data.get("r2_taken") == NOT_REQUIRED
            and self.hypertension_initial_review
        ):
            raise forms.ValidationError(
                {"r2_taken": "Invalid. Expected YES or NO. Patient is hypertensive."}
            )
        self.required_if(NO, field="r2_taken", field_required="r2_reason_not_taken")
        self.required_if(YES, field="r2_taken", field_required="sys_blood_pressure_r2")
        self.required_if(YES, field="r2_taken", field_required="dia_blood_pressure_r2")
        self.validate_bp_reading(
            "sys_blood_pressure_r2", "dia_blood_pressure_r2",
        )

    @property
    def hypertension_initial_review(self):
        try:
            return HypertensionInitialReview.objects.get(
                subject_visit__subject_identifier=self.cleaned_data.get(
                    "subject_visit"
                ).subject_identifier,
                report_datetime__lte=self.cleaned_data.get("report_datetime"),
            )
        except ObjectDoesNotExist:
            return None


class IndicatorsForm(
    CareStatusRequiredModelFormMixin,
    CrfModelFormMixin,
    ActionItemFormMixin,
    forms.ModelForm,
):
    form_validator_cls = IndicatorsFormValidator

    class Meta:
        model = Indicators
        fields = "__all__"
