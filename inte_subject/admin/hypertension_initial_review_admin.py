from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin

from ..admin_site import inte_subject_admin
from ..forms import HypertensionInitialReviewForm
from ..models import HypertensionInitialReview
from .modeladmin import CrfModelAdminMixin


@admin.register(HypertensionInitialReview, site=inte_subject_admin)
class HypertensionInitialReviewAdmin(
    CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin
):

    form = HypertensionInitialReviewForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "Diagnosis and Treatment",
            {"fields": ("dx_ago", "managed_by", "med_start_ago")},
        ),
        audit_fieldset_tuple,
    )

    radio_fields = {
        "managed_by": admin.VERTICAL,
    }
