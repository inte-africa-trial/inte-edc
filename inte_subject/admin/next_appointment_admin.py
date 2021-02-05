from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple
from edc_crf.admin import crf_status_fieldset_tuple
from edc_form_label import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin

from ..admin_site import inte_subject_admin
from ..forms import NextAppointmentForm
from ..models import NextAppointment
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(NextAppointment, site=inte_subject_admin)
class NextAppointmentAdmin(CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin):
    form = NextAppointmentForm
    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "HIV",
            {"fields": ("hiv_clinic_appt_date",)},
        ),
        (
            "NCD (Joint Diabetes/Hypertension)",
            {"fields": ("ncd_clinic_appt_date",)},
        ),
        (
            "Diabetes-only",
            {"fields": ("dm_clinic_appt_date",)},
        ),
        (
            "Hypertension-only",
            {"fields": ("htn_clinic_appt_date",)},
        ),
        (
            "Integrated Clinic",
            {"fields": ("integrated_clinic_appt_date",)},
        ),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    radio_fields = {
        "crf_status": admin.VERTICAL,
    }
