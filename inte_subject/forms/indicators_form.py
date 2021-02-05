from django import forms
from django.core.exceptions import ObjectDoesNotExist
from edc_constants.constants import NO, NOT_REQUIRED, YES
from edc_form_validators.form_validator import FormValidator

from inte_subject.models import HtnInitialReview
from inte_visit_schedule.is_baseline import is_baseline

from ..models import Indicators
from .mixins import (
    BPFormValidatorMixin,
    CrfFormValidatorMixin,
    CrfModelFormMixin,
    raise_if_clinical_review_does_not_exist,
)


class IndicatorsFormValidator(BPFormValidatorMixin, CrfFormValidatorMixin, FormValidator):
    def clean(self):

        raise_if_clinical_review_does_not_exist(self.cleaned_data.get("subject_visit"))
        self.required_if_true(
            is_baseline(self.cleaned_data.get("subject_visit")),
            field_required="weight",
            inverse=False,
        )
        self.required_if_true(
            is_baseline(self.cleaned_data.get("subject_visit")),
            field_required="height",
            inverse=False,
        )
        self.required_if(YES, field="r1_taken", field_required="sys_blood_pressure_r1")
        self.required_if(NO, field="r1_taken", field_required="r1_reason_not_taken")
        self.required_if(YES, field="r1_taken", field_required="dia_blood_pressure_r1")
        self.validate_bp_reading(
            "sys_blood_pressure_r1",
            "dia_blood_pressure_r1",
        )
        if self.cleaned_data.get("r2_taken") == NOT_REQUIRED and self.htn_initial_review:
            raise forms.ValidationError(
                {"r2_taken": "Invalid. Expected YES or NO. Patient is hypertensive."}
            )
        self.required_if(NO, field="r2_taken", field_required="r2_reason_not_taken")
        self.required_if(YES, field="r2_taken", field_required="sys_blood_pressure_r2")
        self.required_if(YES, field="r2_taken", field_required="dia_blood_pressure_r2")
        self.validate_bp_reading(
            "sys_blood_pressure_r2",
            "dia_blood_pressure_r2",
        )

    @property
    def htn_initial_review(self):
        try:
            return HtnInitialReview.objects.get(
                subject_visit__subject_identifier=self.cleaned_data.get(
                    "subject_visit"
                ).subject_identifier,
                report_datetime__lte=self.cleaned_data.get("report_datetime"),
            )
        except ObjectDoesNotExist:
            return None


class IndicatorsForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = IndicatorsFormValidator

    class Meta:
        model = Indicators
        fields = "__all__"
