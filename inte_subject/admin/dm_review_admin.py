from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_crf.admin import crf_status_fieldset_tuple
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin

from ..admin_site import inte_subject_admin
from ..forms import DmReviewForm
from ..models import DmReview
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(DmReview, site=inte_subject_admin)
class DmReviewAdmin(CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin):

    form = DmReviewForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        ("Care", {"fields": ("managed_by", "care_delivery", "care_delivery_other")}),
        (
            "Blood Sugar Measurement",
            {
                "fields": (
                    "glucose_fasted",
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
        "dx": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
        "care_delivery": admin.VERTICAL,
        "managed_by": admin.VERTICAL,
        "glucose_fasted": admin.VERTICAL,
        "glucose_units": admin.VERTICAL,
    }
