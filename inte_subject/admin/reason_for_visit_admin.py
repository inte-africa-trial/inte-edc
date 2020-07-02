from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_crf.admin import crf_status_fieldset_tuple
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin

from ..admin_site import inte_subject_admin
from ..forms import ReasonForVisitForm
from ..models import ReasonForVisit
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(ReasonForVisit, site=inte_subject_admin)
class ReasonForVisitAdmin(
    CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin
):
    form = ReasonForVisitForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        ("Health Services", {"fields": ("health_services",)}),
        ("Clinic Services", {"fields": ("clinic_services", "clinic_services_other")}),
        (
            "Drug Refills",
            {"fields": ("refill_hypertension", "refill_diabetes", "refill_hiv")},
        ),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    filter_horizontal = [
        "health_services",
        "clinic_services",
    ]

    radio_fields = {
        "crf_status": admin.VERTICAL,
        "refill_hypertension": admin.VERTICAL,
        "refill_diabetes": admin.VERTICAL,
        "refill_hiv": admin.VERTICAL,
    }
