from django import forms

from inte_prn.icc_registered import (
    InterventionSiteNotRegistered,
    is_icc_registered_site,
)
from inte_prn.models import IntegratedCareClinicRegistration
from inte_sites.is_intervention_site import NotInterventionSite
from inte_subject.constants import INTEGRATED

from ..models import DailyClosingLog


class DailyClosingLogForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        self.raise_if_integrated_and_icc_not_open(cleaned_data)
        attended = cleaned_data.get("attended")
        approached = cleaned_data.get("approached")
        agreed_to_screen = cleaned_data.get("agreed_to_screen")
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
        return cleaned_data

    @staticmethod
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

    class Meta:
        model = DailyClosingLog
        fields = "__all__"
