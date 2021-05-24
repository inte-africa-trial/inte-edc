from datetime import time

from django import forms

from ..models import (
    DailyClosingLog,
    DailyClosingLogRevised,
    get_daily_log_revision_date,
)
from .daily_closing_log_form import (
    DailyClosingLogForm,
    raise_if_integrated_and_icc_not_open,
    validate_is_singleton,
)


class DailyClosingLogRevisedForm(DailyClosingLogForm):

    start_time = time(6, 0, 0)
    end_time = time(18, 0, 0)

    def clean(self):
        cleaned_data = super().clean()
        validate_is_singleton(self._meta.model, cleaned_data)
        raise_if_integrated_and_icc_not_open(cleaned_data)
        self.raise_if_incorrect_revision(cleaned_data)
        self.validate_start_time(cleaned_data)
        self.validate_end_time(cleaned_data)
        self.validate_start_before_end(cleaned_data)
        return cleaned_data

    def validate_start_time(self, cleaned_data):
        if (
            cleaned_data.get("clinic_start_time") is not None
            and cleaned_data.get("clinic_start_time") < self.start_time
        ):
            raise forms.ValidationError(
                {
                    "clinic_start_time": (
                        f"Invalid. Cannot be earlier than "
                        f'{self.start_time.strftime("%H:%M")} HRS'
                    )
                }
            )

    def validate_end_time(self, cleaned_data):
        if (
            cleaned_data.get("clinic_end_time") is not None
            and cleaned_data.get("clinic_end_time") > self.end_time
        ):
            raise forms.ValidationError(
                {
                    "clinic_end_time": (
                        f'Invalid. Cannot be after {self.start_time.strftime("%H:%M")} HRS'
                    )
                }
            )

    @staticmethod
    def validate_start_before_end(cleaned_data):
        clinic_start_time = cleaned_data.get("clinic_start_time")
        clinic_end_time = cleaned_data.get("clinic_end_time")
        if clinic_start_time is not None and clinic_end_time is not None:
            if clinic_start_time > clinic_end_time:
                raise forms.ValidationError(
                    {"clinic_start_time": "Invalid. cannot be after clinic end time"}
                )

    @staticmethod
    def raise_if_incorrect_revision(cleaned_data):
        """Raises an exception if log date implies should be using
        previous version of this form.
        """
        revision_date = get_daily_log_revision_date()
        if cleaned_data.get("log_date") and cleaned_data.get("log_date") < revision_date:
            raise forms.ValidationError(
                f"This log is for reports on or after {revision_date}. "
                f"Try {DailyClosingLog._meta.verbose_name} instead."
            )

    class Meta:
        model = DailyClosingLogRevised
        fields = [
            "attended",
            "clinic_end_time",
            "clinic_services",
            "clinic_start_time",
            "comment",
            "log_date",
            "site",
        ]
