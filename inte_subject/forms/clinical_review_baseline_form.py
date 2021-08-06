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
        self.raise_if_hiv_clinic_and_no_hiv_test()
        self.estimated_date_from_ago("hiv_test_ago")
        self.when_tested_required(cond="hiv")
        self.raise_if_hiv_clinic_and_no_hiv_dx_result()
        self.required_if(YES, field="hiv_test", field_required="hiv_dx")

        self.raise_if_htn_clinic_and_no_htn_test()
        self.raise_if_dm_clinic_and_no_dm_test()
        self.raise_if_ncd_clinic_and_no_ncd_test()
        self.raise_if_ncd_clinic_and_no_ncd_dx_result()

        self.estimated_date_from_ago("htn_test_ago")
        self.when_tested_required(cond="htn")
        self.raise_if_htn_clinic_and_no_htn_dx_result()
        self.required_if(YES, field="htn_test", field_required="htn_dx")

        self.estimated_date_from_ago("dm_test_ago")
        self.when_tested_required(cond="dm")
        self.raise_if_dm_clinic_and_no_dm_dx_result()
        self.required_if(YES, field="dm_test", field_required="dm_dx")

    def when_tested_required(self, cond=None):
        if self.cleaned_data.get(f"{cond}_test") == YES:
            if not self.cleaned_data.get(f"{cond}_test_ago") and not self.cleaned_data.get(
                f"{cond}_test_date"
            ):
                raise forms.ValidationError(
                    f"{cond.title()}: When was the subject tested? Either provide an "
                    "estimated time 'ago' or provide the exact date. See below."
                )

    def raise_if_hiv_clinic_and_no_hiv_test(self):
        if (
            self.subject_screening.clinic_type == HIV_CLINIC
            and self.cleaned_data.get("hiv_test") != YES
        ):
            raise forms.ValidationError(
                {
                    "hiv_test": ("Patient was screened from an HIV clinic, expected `Yes`."),
                }
            )

    def raise_if_hiv_clinic_and_no_hiv_dx_result(self):
        if (
            self.subject_screening.clinic_type == HIV_CLINIC
            and self.cleaned_data.get("hiv_dx") == NOT_APPLICABLE
        ):
            raise forms.ValidationError(
                {
                    "hiv_dx": (
                        "Patient was screened from an HIV clinic, "
                        "expected 'Yes' or 'No' diagnosis."
                    ),
                }
            )

    def raise_if_htn_clinic_and_no_htn_test(self):
        if (
            self.subject_screening.clinic_type == HYPERTENSION_CLINIC
            and self.cleaned_data.get("htn_test") != YES
        ):
            raise forms.ValidationError(
                {
                    "htn_test": (
                        "Patient was screened from an Hypertension clinic, expected `Yes`."
                    ),
                }
            )

    def raise_if_htn_clinic_and_no_htn_dx_result(self):
        if (
            self.subject_screening.clinic_type == HYPERTENSION_CLINIC
            and self.cleaned_data.get("htn_dx") == NOT_APPLICABLE
        ):
            raise forms.ValidationError(
                {
                    "htn_dx": (
                        "Patient was screened from an Hypertension clinic, "
                        "expected 'Yes' or 'No' diagnosis."
                    ),
                }
            )

    def raise_if_dm_clinic_and_no_dm_test(self):
        if (
            self.subject_screening.clinic_type == DIABETES_CLINIC
            and self.cleaned_data.get("dm_test") != YES
        ):
            raise forms.ValidationError(
                {
                    "dm_test": (
                        "Patient was screened from a Diabetes clinic, expected `Yes`."
                    ),
                }
            )

    def raise_if_dm_clinic_and_no_dm_dx_result(self):
        if (
            self.subject_screening.clinic_type == DIABETES_CLINIC
            and self.cleaned_data.get("dm_dx") == NOT_APPLICABLE
        ):
            raise forms.ValidationError(
                {
                    "dm_dx": (
                        "Patient was screened from a Diabetes clinic, "
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
