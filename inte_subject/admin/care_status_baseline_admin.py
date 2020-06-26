from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_crf.admin import crf_status_fieldset_tuple
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin

from ..admin_site import inte_subject_admin
from ..forms import CareStatusBaselineForm
from ..models import CareStatusBaseline
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(CareStatusBaseline, site=inte_subject_admin)
class CareStatusBaselineAdmin(
    CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin
):

    form = CareStatusBaselineForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        ("HIV", {"fields": ("hiv_result", "hiv_result_ago",)}),
        (
            "Diabetes",
            {"fields": ("diabetic_tested", "diabetic_tested_ago", "diabetic")},
        ),
        (
            "Hypertension",
            {
                "fields": (
                    "hypertensive_tested",
                    "hypertensive_tested_ago",
                    "hypertensive",
                ),
            },
        ),
        ("Other", {"fields": ("health_insurance", "patient_club",)}),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    radio_fields = {
        "crf_status": admin.VERTICAL,
        "hiv_result": admin.VERTICAL,
        "diabetic_tested": admin.VERTICAL,
        "diabetic": admin.VERTICAL,
        "hypertensive_tested": admin.VERTICAL,
        "hypertensive": admin.VERTICAL,
        "health_insurance": admin.VERTICAL,
        "patient_club": admin.VERTICAL,
    }
