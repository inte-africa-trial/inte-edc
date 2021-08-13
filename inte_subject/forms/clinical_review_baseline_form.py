from django import forms
from edc_constants.constants import NOT_APPLICABLE, YES
from edc_form_validators.form_validator import FormValidator

from inte_screening.constants import (
    DIABETES_CLINIC,
    HIV_CLINIC,
    HYPERTENSION_CLINIC,
    NCD_CLINIC,
)

from ..models import ClinicalReviewBaseline
from .mixins import (
    CrfFormValidatorMixin,
    CrfModelFormMixin,
    EstimatedDateFromAgoFormMixin,
)


class ClinicalReviewBaselineFormValidator(
    CrfFormValidatorMixin, EstimatedDateFromAgoFormMixin, FormValidator
):
    def clean(self):
        self.raise_if_ncd_clinic_and_no_ncd_test()
        self.raise_if_ncd_clinic_and_no_ncd_dx_result()

        self.clean_condition_section(clinic_type=HIV_CLINIC, cond="hiv", clinic_desc="HIV")

        self.clean_condition_section(
            clinic_type=DIABETES_CLINIC, cond="dm", clinic_desc="Diabetes"
        )

        self.clean_condition_section(
            clinic_type=HYPERTENSION_CLINIC, cond="htn", clinic_desc="Hypertension"
        )

        self.raise_if_no_hiv_or_ncd_conditions()

    def clean_condition_section(self, clinic_type, cond, clinic_desc=""):
        self.raise_if_vertical_clinic_with_no_related_cond_test(
            clinic_type=clinic_type, cond=cond, clinic_desc=clinic_desc
        )

        self.estimated_date_from_ago(f"{cond}_test_ago")
        self.raise_if_tested_but_no_est_or_exact_test_date(cond=cond)

        self.raise_if_vertical_clinic_with_no_related_cond_dx_result(
            clinic_type=clinic_type, cond=cond, clinic_desc=clinic_desc
        )
        self.required_if(YES, field=f"{cond}_test", field_required=f"{cond}_dx")

    def raise_if_vertical_clinic_with_no_related_cond_test(
        self, clinic_type, cond, clinic_desc=""
    ):
        if (
            self.subject_screening.clinic_type == clinic_type
            and self.cleaned_data.get(f"{cond}_test") != YES
        ):
            raise forms.ValidationError(
                {
                    f"{cond}_test": (
                        f"Patient was screened from {clinic_desc} clinic, expected `Yes`."
                    ),
                }
            )

    def raise_if_tested_but_no_est_or_exact_test_date(self, cond=None):
        if self.cleaned_data.get(f"{cond}_test") == YES:
            if not self.cleaned_data.get(f"{cond}_test_ago") and not self.cleaned_data.get(
                f"{cond}_test_date"
            ):
                raise forms.ValidationError(
                    f"{cond.title()}: When was the subject tested? Either provide an "
                    "estimated time 'ago' or provide the exact date. See below."
                )

    def raise_if_vertical_clinic_with_no_related_cond_dx_result(
        self, clinic_type, cond, clinic_desc=""
    ):
        if (
            self.subject_screening.clinic_type == clinic_type
            and self.cleaned_data.get(f"{cond}_dx") == NOT_APPLICABLE
        ):
            raise forms.ValidationError(
                {
                    f"{cond}_dx": (
                        f"Patient was screened from {clinic_desc} clinic, "
                        "expected 'Yes' or 'No' diagnosis."
                    ),
                }
            )

    def raise_if_ncd_clinic_and_no_ncd_test(self):
        if (
            self.subject_screening.clinic_type == NCD_CLINIC
            and self.cleaned_data.get("dm_test") != YES
            and self.cleaned_data.get("htn_test") != YES
        ):
            raise forms.ValidationError(
                "Patient was screened from an NCD clinic, expected to "
                "have tested for either Hypertension and/or Diabetes."
            )

    def raise_if_ncd_clinic_and_no_ncd_dx_result(self):
        if (
            self.subject_screening.clinic_type == NCD_CLINIC
            and self.cleaned_data.get("dm_dx") == NOT_APPLICABLE
            and self.cleaned_data.get("htn_dx") == NOT_APPLICABLE
        ):
            raise forms.ValidationError(
                "Patient was screened from an NCD clinic, expected "
                "'Yes' or 'No' diagnosis for Hypertension and/or Diabetes."
            )

    def raise_if_no_hiv_or_ncd_conditions(self):
        if not (
            self.cleaned_data.get("hiv_dx") == YES
            or self.cleaned_data.get("dm_dx") == YES
            or self.cleaned_data.get("htn_dx") == YES
        ):
            raise forms.ValidationError(
                "Patient expected to have at least one of the following "
                "conditions: a positive HIV test, a diagnosis for Hypertension "
                "or a diagnosis for Diabetes"
            )


class ClinicalReviewBaselineForm(CrfModelFormMixin, forms.ModelForm):

    form_validator_cls = ClinicalReviewBaselineFormValidator

    class Meta:
        model = ClinicalReviewBaseline
        fields = "__all__"
