from django import forms
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from edc_utils import convert_php_dateformat

from inte_prn.icc_registered import (
    InterventionSiteNotRegistered,
    is_icc_registered_site,
)
from inte_prn.models import IntegratedCareClinicRegistration
from inte_screening.models.daily_closing_log_revised import (
    DailyClosingLogRevised,
    get_daily_log_revision_date,
)
from inte_sites.is_intervention_site import NotInterventionSite
from inte_subject.constants import INTEGRATED

from ..models import DailyClosingLog


def validate_is_singleton(model_cls, cleaned_data):
    try:
        model_cls.objects.get(
            log_date=cleaned_data.get("log_date"), site=cleaned_data.get("site")
        )
    except ObjectDoesNotExist:
        pass
    else:
        formatted_date = cleaned_data.get("log_date").strftime(
            convert_php_dateformat(settings.SHORT_DATE_FORMAT)
        )
        raise forms.ValidationError(
            f"A report for {formatted_date} has already been submitted."
        )


def raise_if_integrated_and_icc_not_open(cleaned_data):
    if cleaned_data.get("clinic_services") == INTEGRATED:
        try:
            is_icc_registered_site(report_date=cleaned_data.get("log_date"))
        except NotInterventionSite:
            raise forms.ValidationError(
                {
                    "clinic_services": (
                        "Invalid. This site is NOT have an integrated care clinic."
                    )
                }
            )
        except InterventionSiteNotRegistered:
            verbose_name = IntegratedCareClinicRegistration._meta.verbose_name
            raise forms.ValidationError(
                {
                    "clinic_services": (
                        "Invalid. This site has not opened the "
                        f"integrated care clinic. See '{verbose_name}'."
                    )
                }
            )


class DailyClosingLogForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        validate_is_singleton(self._meta.model, cleaned_data)
        raise_if_integrated_and_icc_not_open(cleaned_data)
        self.raise_if_incorrect_revision(cleaned_data)
        self.validate_approached_less_than_attended(cleaned_data)
        self.validate_screened_less_than_approached(cleaned_data)
        return cleaned_data

    @staticmethod
    def raise_if_incorrect_revision(cleaned_data):
        """Raises an exception if log date implies should be using
        newer version of this form.
        """
        if (
            cleaned_data.get("log_date")
            and cleaned_data.get("log_date") >= get_daily_log_revision_date()
        ):
            raise forms.ValidationError(
                f"This log is for reports before {get_daily_log_revision_date()}. "
                f"Try {DailyClosingLogRevised._meta.verbose_name} instead."
            )

    @staticmethod
    def validate_approached_less_than_attended(cleaned_data):
        attended = cleaned_data.get("attended")
        approached = cleaned_data.get("approached")
        if attended is not None and approached is not None:
            if approached > attended:
                raise forms.ValidationError(
                    {
                        "approached": (
                            "Invalid. Number approached cannot be greater "
                            "than number attended"
                        )
                    }
                )

    @staticmethod
    def validate_screened_less_than_approached(cleaned_data):
        approached = cleaned_data.get("approached")
        agreed_to_screen = cleaned_data.get("agreed_to_screen")
        if approached is not None and agreed_to_screen is not None:
            if agreed_to_screen > approached:
                raise forms.ValidationError(
                    {
                        "agreed_to_screen": (
                            "Invalid. Number who agreed to be screened cannot "
                            "be greater than number approached"
                        )
                    }
                )

    class Meta:
        model = DailyClosingLog
        fields = [
            "agreed_to_screen",
            "approached",
            "attended",
            "clinic_services",
            "comment",
            "log_date",
            "selection_method",
            "site",
        ]
