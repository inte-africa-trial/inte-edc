from copy import copy

from django.contrib import admin
from edc_action_item import action_fields, action_fieldset_tuple
from edc_model_admin import SimpleHistoryAdmin, audit_fieldset_tuple
from edc_model_admin.dashboard import ModelAdminSubjectDashboardMixin

from ..admin_site import inte_prn_admin
from ..forms import UnblindingRequestForm
from ..models import UnblindingRequest


@admin.register(UnblindingRequest, site=inte_prn_admin)
class UnblindingRequestAdmin(ModelAdminSubjectDashboardMixin, SimpleHistoryAdmin):

    form = UnblindingRequestForm

    additional_instructions = (
        "Note: if the patient is deceased, complete the Death Report "
        "before completing this form. "
    )

    fieldsets = (
        (
            "Request",
            {
                "fields": (
                    "report_datetime",
                    "subject_identifier",
                    "initials",
                    "requestor",
                    "unblinding_reason",
                )
            },
        ),
        ("Approval", {"fields": ("approved", "approved_datetime")}),
        action_fieldset_tuple,
        audit_fieldset_tuple,
    )

    autocomplete_fields = ["requestor"]

    readonly_fields = ("approved", "approved_datetime")

    radio_fields = {"approved": admin.VERTICAL}

    list_display = (
        "subject_identifier",
        "dashboard",
        "requestor",
        "approved",
        "approved_datetime",
        "action_identifier",
        "created",
    )
