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
                    "hypertension_tested",
                    "hypertension_test_date",
                    "hypertension_reason",
                    "hypertension_reason_other",
                    "hypertension_dx",
                )
            },
        ),
        (
            "DIABETES",
            {
                "fields": (
                    "diabetes_tested",
                    "diabetes_test_date",
                    "diabetes_reason",
                    "diabetes_reason_other",
                    "diabetes_dx",
                )
            },
        ),
        (
            "HIV",
            {
                "fields": (
                    "hiv_tested",
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
        "hypertension_tested": admin.VERTICAL,
        "diabetes_tested": admin.VERTICAL,
        "hiv_tested": admin.VERTICAL,
        "hypertension_dx": admin.VERTICAL,
        "diabetes_dx": admin.VERTICAL,
        "hiv_dx": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }

    filter_horizontal = [
        "hypertension_reason",
        "diabetes_reason",
        "hiv_reason",
    ]
