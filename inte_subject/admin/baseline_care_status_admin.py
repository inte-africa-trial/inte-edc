from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin

from ..admin_site import inte_subject_admin
from ..forms import BaselineCareStatusForm
from ..models import BaselineCareStatus
from .modeladmin import CrfModelAdminMixin


@admin.register(BaselineCareStatus, site=inte_subject_admin)
class BaselineCareStatusAdmin(
    CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin
):
    form = BaselineCareStatusForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "HIV",
            {
                "fields": (
                    "hiv",
                    "attending_hiv_clinic",
                    "use_hiv_clinic_nearby",
                    "hiv_clinic_other",
                    "hiv_clinic_other_is_study_clinic",
                    "hiv_willing_to_transfer",
                    "hiv_next_appt_date",
                ),
            },
        ),
        (
            "NCD",
            {
                "fields": (
                    "diabetic",
                    "hypertensive",
                    "attending_ncd_clinic",
                    "use_ncd_clinic_nearby",
                    "ncd_clinic_other",
                    "ncd_clinic_other_is_study_clinic",
                    "ncd_willing_to_transfer",
                    "ncd_next_appt_date",
                ),
            },
        ),
        audit_fieldset_tuple,
    )

    radio_fields = {
        "hiv": admin.VERTICAL,
        "attending_hiv_clinic": admin.VERTICAL,
        "hiv_clinic_other_is_study_clinic": admin.VERTICAL,
        "use_hiv_clinic_nearby": admin.VERTICAL,
        "diabetic": admin.VERTICAL,
        "hypertensive": admin.VERTICAL,
        "attending_ncd_clinic": admin.VERTICAL,
        "ncd_clinic_other_is_study_clinic": admin.VERTICAL,
        "use_ncd_clinic_nearby": admin.VERTICAL,
        "hiv_willing_to_transfer": admin.VERTICAL,
        "ncd_willing_to_transfer": admin.VERTICAL,
    }
