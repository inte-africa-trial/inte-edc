from copy import copy
from django.contrib import admin
from edc_action_item import action_fieldset_tuple, action_fields
from edc_model_admin import audit_fieldset_tuple
from edc_model_admin.dashboard import ModelAdminSubjectDashboardMixin

from ..forms import EndOfStudyForm


class EndOfStudyModelAdminMixin(ModelAdminSubjectDashboardMixin):

    form = EndOfStudyForm

    additional_instructions = (
        "Note: if the patient is deceased, complete the Death Report "
        "before completing this form. "
    )

    fieldsets = (
        [
            "Part 1:",
            {
                "fields": (
                    "subject_identifier",
                    "offschedule_datetime",
                    "offschedule_reason",
                    "other_offschedule_reason",
                    "ltfu_date",
                    "death_date",
                    "comment",
                )
            },
        ],
        action_fieldset_tuple,
        audit_fieldset_tuple,
    )

    list_display = (
        "subject_identifier",
        "dashboard",
        "offschedule_datetime",
        "tracking_identifier",
        "action_identifier",
    )

    list_filter = ("offschedule_datetime",)

    radio_fields = {"offschedule_reason": admin.VERTICAL}

    search_fields = ("subject_identifier", "action_identifier", "tracking_identifier")

    def get_readonly_fields(self, request, obj=None):
        fields = super().get_readonly_fields(request, obj)
        action_flds = copy(list(action_fields))
        fields = list(action_flds) + list(fields)
        return fields
