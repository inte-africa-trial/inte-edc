from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_crf.admin import crf_status_fieldset_tuple
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin

from ..admin_site import inte_subject_admin
from ..forms import DiabetesInitialReviewForm
from ..models import DiabetesInitialReview
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(DiabetesInitialReview, site=inte_subject_admin)
class DiabetesInitialReviewAdmin(
    CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin
):

    form = DiabetesInitialReviewForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "Diagnosis and Treatment",
            {"fields": ("dx_ago", "managed_by", "med_start_ago")},
        ),
        (
            "Blood Sugar Measurement",
            {
                "fields": (
                    "glucose_performed",
                    "glucose_date",
                    "glucose",
                    "glucose_quantifier",
                    "glucose_units",
                ),
            },
        ),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    radio_fields = {
        "crf_status": admin.VERTICAL,
        "managed_by": admin.VERTICAL,
        "glucose_performed": admin.VERTICAL,
        # "glucose_quantifier": admin.VERTICAL,
        "glucose_units": admin.VERTICAL,
    }
