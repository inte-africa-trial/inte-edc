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
        ("HIV", {"fields": ("hiv_test", "hiv_test_ago", "hiv_test_date", "hiv_dx")}),
        ("Diabetes", {"fields": ("dm_test", "dm_test_ago", "dm_test_date", "dm_dx")}),
        (
            "Hypertension",
            {"fields": ("htn_test", "htn_test_ago", "htn_test_date", "htn_dx")},
        ),
        ("Other", {"fields": ("health_insurance", "patient_club")}),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    radio_fields = {
        "crf_status": admin.VERTICAL,
        "dm_dx": admin.VERTICAL,
        "dm_test": admin.VERTICAL,
        "health_insurance": admin.VERTICAL,
        "hiv_dx": admin.VERTICAL,
        "hiv_test": admin.VERTICAL,
        "htn_dx": admin.VERTICAL,
        "htn_test": admin.VERTICAL,
        "patient_club": admin.VERTICAL,
    }
