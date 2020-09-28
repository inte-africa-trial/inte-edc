from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_crf.admin import crf_status_fieldset_tuple
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin

from ..admin_site import inte_subject_admin
from ..forms import ComplicationsFollowupForm
from ..models import ComplicationsFollowup
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(ComplicationsFollowup, site=inte_subject_admin)
class ComplicationsFollowupAdmin(
    CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin
):

    form = ComplicationsFollowupForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "Complications",
            {
                "fields": (
                    "stroke",
                    "stroke_date",
                    "heart_attack",
                    "heart_attack_date",
                    "renal_disease",
                    "renal_disease_date",
                    "vision",
                    "vision_date",
                    "numbness",
                    "numbness_date",
                    "foot_ulcers",
                    "foot_ulcers_date",
                    "complications",
                    "complications_other",
                )
            },
        ),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    radio_fields = {
        "crf_status": admin.VERTICAL,
        "heart_attack": admin.VERTICAL,
        "stroke": admin.VERTICAL,
        "renal_disease": admin.VERTICAL,
        "vision": admin.VERTICAL,
        "numbness": admin.VERTICAL,
        "foot_ulcers": admin.VERTICAL,
        "complications": admin.VERTICAL,
    }
