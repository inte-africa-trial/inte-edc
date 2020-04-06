from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin

from ...admin_site import inte_subject_admin
from ...forms import HealthRiskAssessmentForm
from ...models import HealthRiskAssessment
from ..modeladmin import CrfModelAdminMixin


@admin.register(HealthRiskAssessment, site=inte_subject_admin)
class HealthRiskAssessmentAdmin(
    CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin
):
    form = HealthRiskAssessmentForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        ("Smoking", {"fields": ("smoking_status", "smoker_quit_ago_str")}),
        ("Alcohol", {"fields": ("alcohol", "alcohol_consumption",)}),
        audit_fieldset_tuple,
    )

    radio_fields = {
        "smoking_status": admin.VERTICAL,
        "alcohol": admin.VERTICAL,
        "alcohol_consumption": admin.VERTICAL,
    }
