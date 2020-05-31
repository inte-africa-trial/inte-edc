from django.contrib import admin

from edc_action_item import action_fieldset_tuple
from inte_prn.admin_site import inte_prn_admin

from ..forms import FinalClinicalReviewForm
from ..models import FinalClinicalReview


@admin.register(FinalClinicalReview, site=inte_prn_admin)
class FinalClinicalReviewAdmin:
    form = FinalClinicalReviewForm

    additional_instructions = (
        "Note: This form collects baseline data. It should be completed at enrolment. "
    )

    fieldsets = (
        (
            {
                "fields": (
                    "date",
                    "initials"
                    "hiv",
                    "diabetes",
                    "hypertension",
                    "weight",
                    "height",
                    "health_insurance",
                    "club_support",
                ),
            },
        ),
        (
            "Participants with diabetes ",
            {
                "blood_glucose",
                "fasting",
                "hbA1c",
                "fasting_glucose_units",
            }
        ),
        (
            "Participants with Hypertension",
            {
                "sys_blood_pressure_1",
                "dia_blood_pressure_1",
                "sys_blood_pressure_1",
                "dia_blood_pressure_1",
            }
        ),
        (
            "Participants with HIV-infection",
            {
                "viral_load",
                "viral_load_date",
            }
        ),
        (
            "All participants: have you been diagnosed the following today or during the last 5 months",
            {
                "stroke",
                "heart_attack",
                "renal_disease",
                "vision_problem",
                "numbness",
                "foot_ulcers",
                "other_condition",
                "condition_specify",
            }
        ),
        action_fieldset_tuple,
    )

    radio_fields = {
        "hiv": admin.VERTICAL,
        "diabetes": admin.VERTICAL,
        "hypertension": admin.VERTICAL,
        "health_insurance": admin.VERTICAL,
        "club_support": admin.VERTICAL,
        "fasting": admin.VERTICAL,
        "stoke": admin.VERTICAL,
        "heart_attack": admin.VERTICAL,
        "renal_disease": admin.VERTICAL,
        "vision_problem": admin.VERTICAL,
        "numbness": admin.VERTICAL,
        "foot_ulcers": admin.VERTICAL,
        "other_condition": admin.VERTICAL,
        "condition_specify": admin.VERTICAL,
    }
