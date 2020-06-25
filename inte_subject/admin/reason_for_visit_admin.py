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
        (
            "Hypertension",
            {"fields": ("hypertension_services", "hypertension_services_other")},
        ),
        ("Diabetes", {"fields": ("diabetes_services", "diabetes_services_other")}),
        ("HIV", {"fields": ("hiv_services", "hiv_services_other")}),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    filter_horizontal = [
        "health_services",
        "hypertension_services",
        "diabetes_services",
        "hiv_services",
    ]
