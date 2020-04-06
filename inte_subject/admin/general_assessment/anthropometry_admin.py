from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin

from ...admin_site import inte_subject_admin
from ...forms import AnthropometryForm
from ...models import Anthropometry
from ..modeladmin import CrfModelAdminMixin


@admin.register(Anthropometry, site=inte_subject_admin)
class AnthropometryAdmin(
    CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin
):
    form = AnthropometryForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        ("Weight and Height", {"fields": ("weight", "height", "bmi")},),
        (
            "Blood Pressure: Reading 1",
            {"fields": ("sys_blood_pressure_r1", "dia_blood_pressure_r1",)},
        ),
        (
            "Blood Pressure: Reading 2",
            {"fields": ("r2_taken", "sys_blood_pressure_r2", "dia_blood_pressure_r2",)},
        ),
        audit_fieldset_tuple,
    )

    radio_fields = {
        "r2_taken": admin.VERTICAL,
    }

    readonly_fields = ["bmi"]
