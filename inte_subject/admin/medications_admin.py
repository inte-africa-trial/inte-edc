from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_crf.admin import crf_status_fieldset_tuple
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin

from ..admin_site import inte_subject_admin
from ..forms import MedicationsForm
from ..models import Medications
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(Medications, site=inte_subject_admin)
class MedicationsAdmin(
    CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin
):
    form = MedicationsForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        ("Prescriptions", {"fields": ("refill_htn", "refill_dm", "refill_hiv")}),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    radio_fields = {
        "refill_htn": admin.VERTICAL,
        "refill_dm": admin.VERTICAL,
        "refill_hiv": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }
