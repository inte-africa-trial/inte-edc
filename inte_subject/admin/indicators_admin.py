from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin

from ..admin_site import inte_subject_admin
from ..forms import IndicatorsForm
from ..models import Indicators
from .modeladmin import CrfModelAdminMixin


@admin.register(Indicators, site=inte_subject_admin)
class IndicatorsAdmin(CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin):
    form = IndicatorsForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        ("Weight and Height", {"fields": ("weight", "height")}),
        (
            "Blood Pressure: Reading 1",
            {"fields": ("r1_taken", "sys_blood_pressure_r1", "dia_blood_pressure_r1",)},
        ),
        (
            "Blood Pressure: Reading 2",
            {"fields": ("r2_taken", "sys_blood_pressure_r2", "dia_blood_pressure_r2",)},
        ),
        audit_fieldset_tuple,
    )

    radio_fields = {
        "r1_taken": admin.VERTICAL,
        "r2_taken": admin.VERTICAL,
    }

    readonly_fields = []
