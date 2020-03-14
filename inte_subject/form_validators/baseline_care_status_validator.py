from django import forms
from edc_constants.constants import YES, NO, NOT_APPLICABLE
from edc_form_validators.form_validator import FormValidator
from inte_screening.constants import NCD_CLINIC, HIV_CLINIC

from .crf_form_validator_mixin import CrfFormValidatorMixin


class BaselineCareStatusFormValidator(CrfFormValidatorMixin, FormValidator):
    def clean(self):
        # HIV
        if not self.is_hiv_pos and self.primary_enrolment_clinic_type == HIV_CLINIC:
            raise forms.ValidationError(
                {
                    "hiv": (
                        f"Subject was enrolled from an {self.clinic_title(HIV_CLINIC)}. "
                        "Expected YES."
                    )
                }
            )
        if self.primary_enrolment_clinic_type == HIV_CLINIC:
            self.validate_care_against_primary_enrolment_clinic(HIV_CLINIC)
        self.validate_care_and_clinic_attendance(HIV_CLINIC)
        self.required_if(
            YES,
            field=f"receives_care_at_{HIV_CLINIC}",
            field_required=f"{HIV_CLINIC}_next_appt_date",
        )
        # NCD
        if (
            not self.is_diabetic_or_hypertensive
            and self.primary_enrolment_clinic_type == NCD_CLINIC
        ):
            raise forms.ValidationError(
                {
                    f"Subject was enrolled from an {self.clinic_title(NCD_CLINIC)}. "
                    "Expected patient to be diabetic or hypertensive (or both)"
                }
            )
        if self.primary_enrolment_clinic_type == NCD_CLINIC:
            self.validate_care_against_primary_enrolment_clinic()
        self.applicable_if_true(
            (
                self.cleaned_data.get("diabetic") == YES
                or self.cleaned_data.get("hypertensive") == YES
            ),
            field_applicable="receives_care_at_ncd_clinic",
        )
        self.validate_care_and_clinic_attendance(NCD_CLINIC)

        self.required_if(
            YES,
            field=f"receives_care_at_{NCD_CLINIC}",
            field_required=f"{NCD_CLINIC}_next_appt_date",
        )

    def clinic_title(self, clinic_type):
        return f"{clinic_type.split('_')[0].upper()} Clinic"

    def validate_care_against_primary_enrolment_clinic(self, clinic_type):

        if clinic_type == HIV_CLINIC:
            clinic_title = self.clinic_title(HIV_CLINIC)
            condition = "is_hiv_pos"

        if clinic_type == NCD_CLINIC:
            clinic_title = self.clinic_title(NCD_CLINIC)
            condition = "is_diabetic_or_hypertensive"

        if self.cleaned_data.get(f"receives_care_at_{clinic_type}") != YES:
            raise forms.ValidationError(
                {
                    f"receives_care_at_{clinic_type}": (
                        f"Invalid. Subject was enrolled from this {clinic_title} (1)."
                    )
                }
            )
        if self.cleaned_data.get(f"attends_this_{clinic_type}") != YES:
            raise forms.ValidationError(
                {
                    f"attends_this_{clinic_type}": (
                        f"Invalid. Subject was enrolled from this {clinic_title}. (2)"
                    )
                }
            )
        if self.cleaned_data.get(f"{clinic_type}_other"):
            raise forms.ValidationError(
                {f"{clinic_type}_other": f"This field is not required."}
            )

        if (
            self.cleaned_data.get(f"{clinic_type}_other_is_study_clinic")
            != NOT_APPLICABLE
        ):
            raise forms.ValidationError(
                {
                    f"{clinic_type}_other_is_study_clinic": "This field is not applicable."
                }
            )
        if getattr(self, condition):
            self.applicable_if(
                NO,
                field=f"attends_this_{clinic_type}",
                field_applicable=f"{clinic_type}_willing_to_transfer",
            )

    @property
    def is_hiv_pos(self):
        return self.cleaned_data.get("hiv") == YES

    @property
    def is_diabetic_or_hypertensive(self):
        return (
            self.cleaned_data.get("diabetes") == YES
            or self.cleaned_data.get("hypertension") == YES
        )

    def validate_care_and_clinic_attendance(self, clinic_type):
        self.applicable_if(
            YES,
            field=f"receives_care_at_{clinic_type}",
            field_applicable=f"attends_this_{clinic_type}",
        )
        self.required_if(
            NO,
            field=f"attends_this_{clinic_type}",
            field_required=f"{clinic_type}_other",
        )
        self.applicable_if_true(
            self.cleaned_data.get(f"{clinic_type}_other") is not None,
            field_applicable=f"{clinic_type}_other_is_study_clinic",
        )
        self.applicable_if(
            NO,
            field=f"attends_this_{clinic_type}",
            field_applicable=f"{clinic_type}_willing_to_transfer",
        )
