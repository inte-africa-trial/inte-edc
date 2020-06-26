from django import forms
from edc_constants.constants import NEG, POS, YES
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator
from inte_screening.constants import (
    DIABETES_CLINIC,
    HIV_CLINIC,
    HYPERTENSION_CLINIC,
    NCD_CLINIC,
)

from ..models import CareStatusBaseline
from .crf_form_validator_mixin import CrfFormValidatorMixin


class CareStatusBaselineFormValidator(CrfFormValidatorMixin, FormValidator):
    def clean(self):
        self.raise_if_hiv_clinic_and_not_positive()
        self.required_if(POS, NEG, field="hiv_result", field_required="hiv_result_ago")

        self.raise_if_clinic_and_not_hypertensive()
        self.required_if(
            YES, field="hypertensive_tested", field_required="hypertensive_tested_ago"
        )
        self.required_if(
            YES, field="hypertensive_tested", field_required="hypertensive"
        )

        self.raise_if_clinic_and_not_diabetes()
        self.raise_if_ncd_clinic_and_not_both()
        self.required_if(
            YES, field="diabetic_tested", field_required="diabetic_tested_ago"
        )
        self.required_if(YES, field="diabetic_tested", field_required="diabetic")

    def raise_if_hiv_clinic_and_not_positive(self):
        if (
            self.subject_screening.clinic_type in [HIV_CLINIC]
            and self.cleaned_data.get("hiv_result") != POS
        ):
            raise forms.ValidationError(
                {
                    "hiv_result": (
                        "Patient was screened from an HIV clinic, expected `Positive`."
                    ),
                }
            )

    def raise_if_clinic_and_not_hypertensive(self):
        if (
            self.subject_screening.clinic_type == HYPERTENSION_CLINIC
            and self.cleaned_data.get("hypertensive_tested") != YES
        ):
            raise forms.ValidationError(
                {
                    "hypertensive_tested": (
                        "Patient was screened from an Hypertension clinic, expected `Yes`."
                    ),
                }
            )
        if (
            self.subject_screening.clinic_type == HYPERTENSION_CLINIC
            and self.cleaned_data.get("hypertensive") != YES
        ):
            raise forms.ValidationError(
                {
                    "hypertensive_tested": (
                        "Patient was screened from an Hypertension clinic, expected `Yes`."
                    ),
                }
            )

    def raise_if_clinic_and_not_diabetes(self):
        if (
            self.subject_screening.clinic_type == DIABETES_CLINIC
            and self.cleaned_data.get("diabetic_tested") != YES
        ):
            raise forms.ValidationError(
                {
                    "diabetic_tested": (
                        "Patient was screened from a Diabetes clinic, expected `Yes`."
                    ),
                }
            )
        if (
            self.subject_screening.clinic_type == DIABETES_CLINIC
            and self.cleaned_data.get("diabetic") != YES
        ):
            raise forms.ValidationError(
                {
                    "diabetic_tested": (
                        "Patient was screened from a Diabetes clinic, expected `Yes`."
                    ),
                }
            )

    def raise_if_ncd_clinic_and_not_both(self):
        if (
            self.subject_screening.clinic_type == NCD_CLINIC
            and self.cleaned_data.get("diabetic_tested") != YES
            and self.cleaned_data.get("hypertensive_tested") != YES
        ):
            raise forms.ValidationError(
                "Patient was screened from an NCD clinic, expected to "
                "have tested for either Hypertension and/or Diabetes."
            )
        if (
            self.subject_screening.clinic_type == NCD_CLINIC
            and self.cleaned_data.get("diabetic") != YES
            and self.cleaned_data.get("hypertensive") != YES
        ):
            raise forms.ValidationError(
                "Patient was screened from an NCD clinic, expected to "
                "have been diagnosed with either Hypertension and/or Diabetes."
            )


class CareStatusBaselineForm(CrfModelFormMixin, forms.ModelForm):

    form_validator_cls = CareStatusBaselineFormValidator

    class Meta:
        model = CareStatusBaseline
        fields = "__all__"
