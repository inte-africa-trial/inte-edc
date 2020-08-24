from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_crf.admin import crf_status_fieldset_tuple
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin

from ..admin_site import inte_subject_admin
from ..forms import ClinicalReviewBaselineForm
from ..models import ClinicalReviewBaseline
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(ClinicalReviewBaseline, site=inte_subject_admin)
class ClinicalReviewBaselineAdmin(
    CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin
):

    form = ClinicalReviewBaselineForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        ("HIV", {"fields": ("hiv_tested", "hiv_tested_ago", "hiv_tested_date")}),
        (
            "Diabetes",
            {
                "fields": (
                    "diabetes_tested",
                    "diabetes_tested_ago",
                    "diabetes_tested_date",
                    "diabetes_dx",
                )
            },
        ),
        (
            "Hypertension",
            {
                "fields": (
                    "hypertension_tested",
                    "hypertension_tested_ago",
                    "hypertension_tested_date",
                    "hypertension_dx",
                ),
            },
        ),
        ("Other", {"fields": ("health_insurance", "patient_club",)}),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    radio_fields = {
        "crf_status": admin.VERTICAL,
        "hiv_tested": admin.VERTICAL,
        "diabetes_tested": admin.VERTICAL,
        "diabetes_dx": admin.VERTICAL,
        "hypertension_tested": admin.VERTICAL,
        "hypertension_dx": admin.VERTICAL,
        "health_insurance": admin.VERTICAL,
        "patient_club": admin.VERTICAL,
    }
