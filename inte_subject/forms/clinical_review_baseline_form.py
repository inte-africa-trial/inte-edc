from django import forms
from edc_constants.constants import YES
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
        self.raise_if_hiv_clinic_and_hiv_pos()
        self.estimated_date_from_ago("hiv_test_ago")
        self.when_tested_required(cond="hiv")

        self.raise_if_clinic_and_not_htn()
        self.raise_if_clinic_and_not_diabetes()
        self.raise_if_ncd_clinic_and_not_both()

        self.estimated_date_from_ago("htn_test_ago")
        self.when_tested_required(cond="htn")
        self.required_if(YES, field="htn_test", field_required="htn_dx")

        self.estimated_date_from_ago("dm_test_ago")
        self.when_tested_required(cond="diabetes")
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

    def raise_if_hiv_clinic_and_hiv_pos(self):
        if (
            self.subject_screening.clinic_type == HIV_CLINIC
            and self.cleaned_data.get("hiv_test") != YES
        ):
            raise forms.ValidationError(
                {
                    "hiv_test": ("Patient was screened from an HIV clinic, expected `Yes`."),
                }
            )

        if (
            self.subject_screening.clinic_type == HIV_CLINIC
            and self.cleaned_data.get("hiv_dx") != YES
        ):
            raise forms.ValidationError(
                {
                    "hiv_dx": ("Patient was screened from an HIV clinic, expected `Yes`."),
                }
            )

    def raise_if_clinic_and_not_htn(self):
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
        if (
            self.subject_screening.clinic_type == HYPERTENSION_CLINIC
            and self.cleaned_data.get("htn_dx") != YES
        ):
            raise forms.ValidationError(
                {
                    "htn_dx": (
                        "Patient was screened from an Hypertension clinic, expected `Yes`."
                    ),
                }
            )

    def raise_if_clinic_and_not_diabetes(self):
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
        if (
            self.subject_screening.clinic_type == DIABETES_CLINIC
            and self.cleaned_data.get("dm_dx") != YES
        ):
            raise forms.ValidationError(
                {
                    "dm_dx": ("Patient was screened from a Diabetes clinic, expected `Yes`."),
                }
            )

    def raise_if_ncd_clinic_and_not_both(self):
        if (
            self.subject_screening.clinic_type == NCD_CLINIC
            and self.cleaned_data.get("dm_test") != YES
            and self.cleaned_data.get("htn_test") != YES
        ):
            raise forms.ValidationError(
                "Patient was screened from an NCD clinic, expected to "
                "have tested for either Hypertension and/or Diabetes."
            )

        if (
            self.subject_screening.clinic_type == NCD_CLINIC
            and (
                self.cleaned_data.get("dm_test") == YES
                or self.cleaned_data.get("htn_test") == YES
            )
            and self.cleaned_data.get("dm_dx") != YES
            and self.cleaned_data.get("htn_dx") != YES
        ):
            raise forms.ValidationError(
                "Patient was screened from an NCD clinic, expected to "
                "have a diagnosis for either Hypertension and/or Diabetes."
            )


class ClinicalReviewBaselineForm(CrfModelFormMixin, forms.ModelForm):

    form_validator_cls = ClinicalReviewBaselineFormValidator

    class Meta:
        model = ClinicalReviewBaseline
        fields = "__all__"
