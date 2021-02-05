from copy import copy

from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_action_item import ModelAdminActionItemMixin
from edc_action_item.fieldsets import action_fields, action_fieldset_tuple
from edc_model_admin import SimpleHistoryAdmin
from edc_model_admin.dashboard import ModelAdminSubjectDashboardMixin

from ..admin_site import inte_ae_admin
from ..forms import DeathReportForm
from ..models import DeathReport


@admin.register(DeathReport, site=inte_ae_admin)
class DeathReportAdmin(
    ModelAdminSubjectDashboardMixin, ModelAdminActionItemMixin, SimpleHistoryAdmin
):

    form = DeathReportForm

    fieldsets = (
        (None, {"fields": ("subject_identifier", "report_datetime", "death_date")}),
        (
            "Location of death",
            {
                "fields": (
                    "death_location",
                    "death_location_other",
                    "hospital_death",
                    "hospital_name",
                )
            },
        ),
        (
            "Informant",
            {
                "fields": (
                    "informant",
                    "informant_other",
                    "confirmed_by",
                    "confirmed_by_other",
                )
            },
        ),
        ("Comment", {"fields": ("narrative",)}),
        action_fieldset_tuple,
        audit_fieldset_tuple,
    )

    radio_fields = {
        "death_location": admin.VERTICAL,
        "hospital_death": admin.VERTICAL,
        "informant": admin.VERTICAL,
        "confirmed_by": admin.VERTICAL,
    }

    list_display = (
        "subject_identifier",
        "dashboard",
        "death_date",
        "action_item",
        "parent_action_item",
    )

    list_filter = ("report_datetime", "death_date")

    search_fields = ["subject_identifier", "action_identifier", "tracking_identifier"]

    def get_readonly_fields(self, request, obj=None):
        fields = super().get_readonly_fields(request, obj)
        action_flds = copy(list(action_fields))
        action_flds.remove("action_identifier")
        fields = list(action_flds) + list(fields)
        return fields
