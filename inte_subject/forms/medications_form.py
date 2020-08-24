from django import forms
from django.conf import settings
from edc_constants.constants import YES
from edc_form_validators.form_validator import FormValidator
from edc_utils import convert_php_dateformat

from ..models import Medications
from ..morbidity import Morbidities
from .mixins import CrfModelFormMixin, CrfFormValidatorMixin


class MedicationsFormValidator(CrfFormValidatorMixin, FormValidator):
    def clean(self):
        self.validate_diagnosis_before_refill()

    def validate_diagnosis_before_refill(self):
        """Assert subject has been diagnosed for the condition
        for which they require a medication refill."""
        morbidity = Morbidities(
            subject_identifier=self.subject_identifier,
            report_datetime=self.report_datetime,
        )
        options = [
            ("refill_hypertension", morbidity.is_hypertensive, "hypertension"),
            ("refill_diabetes", morbidity.is_diabetic, "diabetes"),
            ("refill_hiv", morbidity.is_hiv_pos, "HIV"),
        ]
        for fld, func, dx in options:
            if self.cleaned_data.get(fld) == YES and not func(
                self.subject_identifier, report_datetime=self.report_datetime
            ):
                formatted_date = self.report_datetime.strftime(
                    convert_php_dateformat(settings.DATETIME_FORMAT)
                )
                raise forms.ValidationError(
                    {
                        fld: f"Invalid. Subject was not diagnosed with {dx} by {formatted_date}."
                    }
                )


class MedicationsForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = MedicationsFormValidator

    class Meta:
        model = Medications
        fields = "__all__"
