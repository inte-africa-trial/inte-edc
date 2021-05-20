from datetime import time

from django import forms

from ..models import DailyClosingLogRevised
from .daily_closing_log_form import DailyClosingLogForm


class DailyClosingLogRevisedForm(DailyClosingLogForm):
    def clean(self):
        cleaned_data = super().clean()
        self.raise_if_integrated_and_icc_not_open(cleaned_data)
        clinic_start_time = cleaned_data.get("clinic_start_time")
        if clinic_start_time is not None and clinic_start_time < time(6, 0, 0):
            raise forms.ValidationError(
                {"clinic_start_time": ("Invalid. Cannot be earlier than 06:00")}
            )
        clinic_end_time = cleaned_data.get("clinic_end_time")
        if clinic_end_time is not None and clinic_end_time > time(18, 0, 0):
            raise forms.ValidationError(
                {"clinic_end_time": ("Invalid. Cannot be later than 18:00")}
            )
        if clinic_start_time is not None and clinic_end_time is not None:
            if clinic_start_time > clinic_end_time:
                raise forms.ValidationError(
                    {
                        "clinic_start_time": (
                            "Invalid. cannot " "be greater than clinic end time"
                        )
                    }
                )
        return cleaned_data

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
