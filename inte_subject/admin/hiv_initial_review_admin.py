from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_crf.admin import crf_status_fieldset_tuple
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin

from ..admin_site import inte_subject_admin
from ..forms import HivInitialReviewForm
from ..models import HivInitialReview
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(HivInitialReview, site=inte_subject_admin)
class HivInitialReviewAdmin(
    CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin
):
    form = HivInitialReviewForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "Diagnosis and Care",
            {"fields": ("dx_ago", "receives_care", "clinic", "clinic_other")},
        ),
        (
            "Monitoring and Treatment",
            {
                "fields": (
                    "arv_initiation_ago",
                    "has_vl",
                    "vl",
                    "vl_quantifier",
                    "vl_date",
                    "has_cd4",
                    "cd4",
                    "cd4_date",
                ),
            },
        ),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    radio_fields = {
        "clinic": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
        "has_cd4": admin.VERTICAL,
        "has_vl": admin.VERTICAL,
        "receives_care": admin.VERTICAL,
        "vl_quantifier": admin.VERTICAL,
    }
