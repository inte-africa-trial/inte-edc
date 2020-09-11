from django import forms
from django.conf import settings
from edc_constants.constants import NO, NOT_APPLICABLE, YES
from edc_form_validators.form_validator import FormValidator
from edc_utils import convert_php_dateformat

from ..models import Medications
from ..diagnoses import Diagnoses
from .mixins import CrfModelFormMixin, CrfFormValidatorMixin


class MedicationsFormValidator(CrfFormValidatorMixin, FormValidator):
    def clean(self):
        self.validate_diagnosis_before_refill()

    def validate_diagnosis_before_refill(self):
        """Assert subject has been diagnosed for the condition
        for which they require a medication refill,
        including for the current timepoint."""

        diagnoses = Diagnoses(
            subject_identifier=self.subject_identifier,
            report_datetime=self.report_datetime,
            lte=True,
        )
        options = [
            ("refill_htn", diagnoses.htn, "hypertension"),
            ("refill_dm", diagnoses.dm, "diabetes"),
            ("refill_hiv", diagnoses.hiv, "HIV"),
        ]
        for fld, dx, label in options:
            if self.cleaned_data.get(fld) == NOT_APPLICABLE and dx == YES:
                formatted_date = self.report_datetime.strftime(
                    convert_php_dateformat(settings.DATETIME_FORMAT)
                )
                raise forms.ValidationError(
                    {
                        fld: (
                            "Invalid. Subject was not diagnosed with "
                            f"{label} by {formatted_date}."
                        )
                    }
                )


class MedicationsForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = MedicationsFormValidator

    class Meta:
        model = Medications
        fields = "__all__"
