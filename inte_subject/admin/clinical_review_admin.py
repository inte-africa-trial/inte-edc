from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_crf.admin import crf_status_fieldset_tuple
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin

from ..admin_site import inte_subject_admin
from ..forms import ClinicalReviewForm
from ..models import ClinicalReview
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(ClinicalReview, site=inte_subject_admin)
class ClinicalReviewAdmin(
    CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin
):
    form = ClinicalReviewForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "HYPERTENSION",
            {
                "fields": (
                    "htn_test",
                    "htn_test_date",
                    "htn_reason",
                    "htn_reason_other",
                    "htn_dx",
                )
            },
        ),
        (
            "DIABETES",
            {
                "fields": (
                    "dm_test",
                    "dm_test_date",
                    "dm_reason",
                    "dm_reason_other",
                    "dm_dx",
                )
            },
        ),
        (
            "HIV",
            {
                "fields": (
                    "hiv_test",
                    "hiv_test_date",
                    "hiv_reason",
                    "hiv_reason_other",
                    "hiv_dx",
                )
            },
        ),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    radio_fields = {
        "htn_test": admin.VERTICAL,
        "dm_test": admin.VERTICAL,
        "hiv_test": admin.VERTICAL,
        "htn_dx": admin.VERTICAL,
        "dm_dx": admin.VERTICAL,
        "hiv_dx": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }

    filter_horizontal = [
        "htn_reason",
        "dm_reason",
        "hiv_reason",
    ]
