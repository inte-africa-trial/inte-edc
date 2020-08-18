from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_crf.admin import crf_status_fieldset_tuple
from edc_form_label import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin

from ..admin_site import inte_subject_admin
from ..forms import FamilyHistoryForm
from ..models import FamilyHistory
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(FamilyHistory, site=inte_subject_admin)
class FamilyHistoryAdmin(
    CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin
):

    form = FamilyHistoryForm
    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "Part 1",
            {
                "fields": (
                    "hypertension_in_household",
                    "diabetes_in_household",
                    "hiv_in_household",
                )
            },
        ),
        (
            "Part 2",
            {
                "fields": (
                    "high_bp_bs_tf",
                    "overweight_tf",
                    "salty_foods_tf",
                    "excercise_tf",
                    "take_medicine_tf",
                    "stop_hypertension_meds_tf",
                    "traditional_hypertension_tf",
                    "stop_diabetes_meds_tf",
                    "traditional_diabetes_tf",
                    "diabetes_cause_tf",
                )
            },
        ),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    radio_fields = {
        "hypertension_in_household": admin.VERTICAL,
        "diabetes_in_household": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
        "hiv_in_household": admin.VERTICAL,
        "high_bp_bs_tf": admin.VERTICAL,
        "overweight_tf": admin.VERTICAL,
        "salty_foods_tf": admin.VERTICAL,
        "excercise_tf": admin.VERTICAL,
        "take_medicine_tf": admin.VERTICAL,
        "stop_hypertension_meds_tf": admin.VERTICAL,
        "traditional_hypertension_tf": admin.VERTICAL,
        "stop_diabetes_meds_tf": admin.VERTICAL,
        "traditional_diabetes_tf": admin.VERTICAL,
        "diabetes_cause_tf": admin.VERTICAL,
    }
