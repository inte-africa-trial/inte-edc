from django import forms
from edc_consent.form_validators import SubjectConsentFormValidatorMixin
from edc_consent.modelform_mixins import ConsentModelFormMixin
from edc_form_validators import FormValidator, FormValidatorMixin
from edc_sites.forms import SiteModelFormMixin

from ..models import SubjectConsent


class SubjectConsentFormValidator(SubjectConsentFormValidatorMixin, FormValidator):
    subject_screening_model = "inte_screening.subjectscreening"

    def clean(self):
        super().clean()
        if self.cleaned_data.get("clinic_type") != self.subject_screening.clinic_type:
            raise forms.ValidationError(
                {
                    "clinic_type": (
                        f"Invalid clinic type. Expected "
                        f"`{self.subject_screening.get_clinic_type_display()}` as reported "
                        f"on the screening form."
                    )
                }
            )


class SubjectConsentForm(
    SiteModelFormMixin, FormValidatorMixin, ConsentModelFormMixin, forms.ModelForm
):
    form_validator_cls = SubjectConsentFormValidator

    screening_identifier = forms.CharField(
        label="Screening identifier",
        widget=forms.TextInput(attrs={"readonly": "readonly"}),
    )

    def clean_gender_of_consent(self):
        """Limited by options on form."""
        return None

    def clean_guardian_and_dob(self):
        """Minors not included in this trial"""
        return None

    class Meta:
        model = SubjectConsent
        fields = "__all__"
        help_texts = {
            "identity": (
                "Use Country ID Number, Passport number, driver's license "
                "number, Mobile, etc"
            ),
            "witness_name": (
                "Required only if participant is illiterate. "
                "Format is 'LASTNAME, FIRSTNAME'. "
                "All uppercase separated by a comma."
            ),
        }
