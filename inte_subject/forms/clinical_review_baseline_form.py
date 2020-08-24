from django import forms
from edc_constants.constants import NEG, POS, YES
from edc_form_validators.form_validator import FormValidator
from inte_screening.constants import (
    DIABETES_CLINIC,
    HIV_CLINIC,
    HYPERTENSION_CLINIC,
    NCD_CLINIC,
)

from ..models import ClinicalReviewBaseline
from .mixins import (
    EstimatedDateFromAgoFormMixin,
    CrfModelFormMixin,
    CrfFormValidatorMixin,
)


class ClinicalReviewBaselineFormValidator(
    CrfFormValidatorMixin, EstimatedDateFromAgoFormMixin, FormValidator
):
    def clean(self):
        self.raise_if_hiv_clinic_and_not_positive()
        # self.required_if(POS, NEG, field="hiv", field_required="hiv_tested_ago")
        self.estimated_date_from_ago("hiv_tested_ago")
        self.when_tested_required(cond="hiv")

        self.raise_if_clinic_and_not_hypertension()
        self.raise_if_clinic_and_not_diabetes()
        self.raise_if_ncd_clinic_and_not_both()

        # self.required_if(
        #     YES, field="hypertension_tested", field_required="hypertension_tested_ago"
        # )

        self.estimated_date_from_ago("hypertension_tested_ago")

        self.when_tested_required(cond="hypertension")

        self.required_if(
            YES, field="hypertension_tested", field_required="hypertension_dx"
        )

        # self.required_if(
        #     YES, field="diabetes_tested", field_required="diabetes_tested_ago"
        # )
        self.estimated_date_from_ago("diabetes_tested_ago")
        self.when_tested_required(cond="diabetes")
        self.required_if(YES, field="diabetes_tested", field_required="diabetes_dx")

    def when_tested_required(self, cond=None):
        if self.cleaned_data.get(f"{cond}_tested") in [YES, POS]:
            if not self.cleaned_data.get(
                f"{cond}_tested_ago"
            ) and not self.cleaned_data.get(f"{cond}_tested_date"):
                raise forms.ValidationError(
                    f"{cond.title()}: When was the subject tested? Either provide an "
                    "estimated time 'ago' or provide the exact date. See below."
                )

    def raise_if_hiv_clinic_and_not_positive(self):
        if (
            self.subject_screening.clinic_type in [HIV_CLINIC]
            and self.cleaned_data.get("hiv_tested") != POS
        ):
            raise forms.ValidationError(
                {
                    "hiv_tested": (
                        "Patient was screened from an HIV clinic, expected `Positive`."
                    ),
                }
            )

    def raise_if_clinic_and_not_hypertension(self):
        if (
            self.subject_screening.clinic_type == HYPERTENSION_CLINIC
            and self.cleaned_data.get("hypertension_tested") != YES
        ):
            raise forms.ValidationError(
                {
                    "hypertension_tested": (
                        "Patient was screened from an Hypertension clinic, expected `Yes`."
                    ),
                }
            )
        if (
            self.subject_screening.clinic_type == HYPERTENSION_CLINIC
            and self.cleaned_data.get("hypertension_dx") != YES
        ):
            raise forms.ValidationError(
                {
                    "hypertension_dx": (
                        "Patient was screened from an Hypertension clinic, expected `Yes`."
                    ),
                }
            )

    def raise_if_clinic_and_not_diabetes(self):
        if (
            self.subject_screening.clinic_type == DIABETES_CLINIC
            and self.cleaned_data.get("diabetes_tested") != YES
        ):
            raise forms.ValidationError(
                {
                    "diabetes_tested": (
                        "Patient was screened from a Diabetes clinic, expected `Yes`."
                    ),
                }
            )
        if (
            self.subject_screening.clinic_type == DIABETES_CLINIC
            and self.cleaned_data.get("diabetes_dx") != YES
        ):
            raise forms.ValidationError(
                {
                    "diabetes_dx": (
                        "Patient was screened from a Diabetes clinic, expected `Yes`."
                    ),
                }
            )

    def raise_if_ncd_clinic_and_not_both(self):
        if (
            self.subject_screening.clinic_type == NCD_CLINIC
            and self.cleaned_data.get("diabetes_tested") != YES
            and self.cleaned_data.get("hypertension_tested") != YES
        ):
            raise forms.ValidationError(
                "Patient was screened from an NCD clinic, expected to "
                "have tested for either Hypertension and/or Diabetes."
            )

        if (
            self.subject_screening.clinic_type == NCD_CLINIC
            and (
                self.cleaned_data.get("diabetes_tested") == YES
                or self.cleaned_data.get("hypertension_tested") == YES
            )
            and self.cleaned_data.get("diabetes_dx") != YES
            and self.cleaned_data.get("hypertension_dx") != YES
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
