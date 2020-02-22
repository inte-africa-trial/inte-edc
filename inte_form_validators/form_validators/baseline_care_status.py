from django import forms
from edc_constants.constants import YES, NO, NOT_APPLICABLE
from edc_form_validators.form_validator import FormValidator

from .crf_form_validator_mixin import CrfFormValidatorMixin


class BaselineCareStatusFormValidator(FormValidator):
    def clean(self):

        self.validate_clinic_access("hiv")

        if self.cleaned_data.get(
            "attending_hiv_clinic"
        ) != YES and self.enroled_from_clinic("hiv"):
            raise forms.ValidationError(
                {"attending_hiv_clinic": "Subject was enrolled from an HIV Clinic."}
            )

        self.validate_clinic_access("ncd")

        if self.cleaned_data.get(
            "attending_ncd_clinic"
        ) != YES and self.enroled_from_clinic("ncd"):
            raise forms.ValidationError(
                {"attending_ncd_clinic": "Subject was enrolled from an NCD Clinic."}
            )

    def enroled_from_clinic(self, key):
        return self.cleaned_data.get("enroled_from_clinic") == key

    def validate_clinic_access(self, key):
        self.validate_attending_clinic(key)

        self.applicable_if(
            YES,
            field=f"attending_{key}_clinic",
            field_applicable=f"use_{key}_clinic_nearby",
        )
        self.required_if(
            NO, field=f"use_{key}_clinic_nearby", field_required=f"{key}_clinic_other"
        )
        self.applicable_if(
            NO,
            field=f"use_{key}_clinic_nearby",
            field_applicable=f"{key}_willing_to_transfer",
        )
        self.required_if(YES, field=key, field_required=f"{key}_next_appt_date")

    def validate_attending_clinic(self, key):
        if key == "hiv":
            self.applicable_if(
                YES, field=key, field_applicable=f"attending_{key}_clinic"
            )
        elif key == "ncd":
            if (
                self.cleaned_data.get("diabetic") == YES
                or self.cleaned_data.get("hypertensive") == YES
            ):
                if self.cleaned_data.get("attending_ncd_clinic") == NOT_APPLICABLE:
                    raise forms.ValidationError(
                        {"attending_ncd_clinic": "This field is applicable"}
                    )

            if (
                self.cleaned_data.get("diabetic") == NO
                and self.cleaned_data.get("hypertensive") == NO
                and self.cleaned_data.get("attending_ncd_clinic") != NOT_APPLICABLE
            ):
                raise forms.ValidationError(
                    {"attending_ncd_clinic": "This field is not applicable"}
                )
