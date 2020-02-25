from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple

from ..forms import NextAppointmentForm
from ..models import NextAppointment
from ..admin_site import inte_subject_admin
from .modeladmin import CrfModelAdmin


@admin.register(NextAppointment, site=inte_subject_admin)
class NextAppointmentAdmin(CrfModelAdmin):
    form = NextAppointmentForm
    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        ("Part 1: Education", {"fields": ("next_appt_date",)},),
        audit_fieldset_tuple,
    )
