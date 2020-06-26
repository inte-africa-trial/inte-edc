from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_crf.admin import crf_status_fieldset_tuple
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin

from ..admin_site import inte_subject_admin
from ..forms import HypertensionReviewForm
from ..models import HypertensionReview
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(HypertensionReview, site=inte_subject_admin)
class HypertensionReviewAdmin(
    CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin
):

    form = HypertensionReviewForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        ("Testing and Diagnosis", {"fields": ("test_date", "dx")}),
        (
            "Final Blood Pressure Measurement",
            {"fields": ("sys_blood_pressure", "dia_blood_pressure",)},
        ),
        ("Care", {"fields": ("managed_by", "care_start_date")}),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    radio_fields = {
        "dx": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
        "managed_by": admin.VERTICAL,
    }
