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
        self.raise_if_vertical_clinic_with_no_related_cond_test(
            clinic=HIV_CLINIC, cond="hiv", clinic_desc="HIV"
        )
        self.estimated_date_from_ago("hiv_test_ago")
        self.when_tested_required(cond="hiv")
        self.raise_if_vertical_clinic_with_no_related_cond_dx_result(
            clinic=HIV_CLINIC, cond="hiv", clinic_desc="HIV"
        )
        self.required_if(YES, field="hiv_test", field_required="hiv_dx")

        self.raise_if_vertical_clinic_with_no_related_cond_test(
            clinic=HYPERTENSION_CLINIC, cond="htn", clinic_desc="Hypertension"
        )
        self.raise_if_vertical_clinic_with_no_related_cond_test(
            clinic=DIABETES_CLINIC, cond="dm", clinic_desc="Diabetes"
        )
        self.raise_if_ncd_clinic_and_no_ncd_test()
        self.raise_if_ncd_clinic_and_no_ncd_dx_result()

        self.estimated_date_from_ago("htn_test_ago")
        self.when_tested_required(cond="htn")
        self.raise_if_vertical_clinic_with_no_related_cond_dx_result(
            clinic=HYPERTENSION_CLINIC, cond="htn", clinic_desc="Hypertension"
        )
        self.required_if(YES, field="htn_test", field_required="htn_dx")

        self.estimated_date_from_ago("dm_test_ago")
        self.when_tested_required(cond="dm")
        self.raise_if_vertical_clinic_with_no_related_cond_dx_result(
            clinic=DIABETES_CLINIC, cond="dm", clinic_desc="Diabetes"
        )
        self.required_if(YES, field="dm_test", field_required="dm_dx")

    def raise_if_vertical_clinic_with_no_related_cond_test(self, clinic, cond, clinic_desc=""):
        if (
            self.subject_screening.clinic_type == clinic
            and self.cleaned_data.get(f"{cond}_test") != YES
        ):
            raise forms.ValidationError(
                {
                    f"{cond}_test": (
                        f"Patient was screened from {clinic_desc} clinic, expected `Yes`."
                    ),
                }
            )

    def when_tested_required(self, cond=None):
        if self.cleaned_data.get(f"{cond}_test") == YES:
            if not self.cleaned_data.get(f"{cond}_test_ago") and not self.cleaned_data.get(
                f"{cond}_test_date"
            ):
                raise forms.ValidationError(
                    f"{cond.title()}: When was the subject tested? Either provide an "
                    "estimated time 'ago' or provide the exact date. See below."
                )

    def raise_if_vertical_clinic_with_no_related_cond_dx_result(
        self, clinic, cond, clinic_desc=""
    ):
        if (
            self.subject_screening.clinic_type == clinic
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


class ClinicalReviewBaselineForm(CrfModelFormMixin, forms.ModelForm):

    form_validator_cls = ClinicalReviewBaselineFormValidator

    class Meta:
        model = ClinicalReviewBaseline
        fields = "__all__"
