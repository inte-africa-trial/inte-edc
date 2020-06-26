from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_crf.admin import crf_status_fieldset_tuple
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin

from ..admin_site import inte_subject_admin
from ..forms import HivReviewForm
from ..models import HivReview
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(HivReview, site=inte_subject_admin)
class HivReviewAdmin(CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin):

    form = HivReviewForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        ("Testing and Diagnosis", {"fields": ("test_date", "dx")}),
        ("Care", {"fields": ("care_start_date",)}),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    radio_fields = {
        "dx": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }
