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
                    "receives_care_at_hiv_clinic",
                    "attends_this_hiv_clinic",
                    "hiv_clinic_other",
                    "hiv_clinic_other_is_study_clinic",
                    "hiv_clinic_willing_to_transfer",
                    "hiv_clinic_next_appt_date",
                ),
            },
        ),
        (
            "NCD",
            {
                "fields": (
                    "diabetic",
                    "hypertensive",
                    "receives_care_at_ncd_clinic",
                    "attends_this_ncd_clinic",
                    "ncd_clinic_other",
                    "ncd_clinic_other_is_study_clinic",
                    "ncd_clinic_willing_to_transfer",
                    "ncd_clinic_next_appt_date",
                ),
            },
        ),
        audit_fieldset_tuple,
    )

    radio_fields = {
        "diabetic": admin.VERTICAL,
        "hiv": admin.VERTICAL,
        "hiv_clinic_other_is_study_clinic": admin.VERTICAL,
        "hiv_clinic_willing_to_transfer": admin.VERTICAL,
        "hypertensive": admin.VERTICAL,
        "ncd_clinic_other_is_study_clinic": admin.VERTICAL,
        "ncd_clinic_willing_to_transfer": admin.VERTICAL,
        "receives_care_at_hiv_clinic": admin.VERTICAL,
        "receives_care_at_ncd_clinic": admin.VERTICAL,
        "attends_this_hiv_clinic": admin.VERTICAL,
        "attends_this_ncd_clinic": admin.VERTICAL,
    }
