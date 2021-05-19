from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_crf.admin import crf_status_fieldset_tuple
from edc_form_label import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin

from ..admin_site import inte_subject_admin
from ..forms import IntegratedCareReviewForm
from ..models import IntegratedCareReview
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(IntegratedCareReview, site=inte_subject_admin)
class IntegratedCareReviewAdmin(
    CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin
):

    form = IntegratedCareReviewForm
    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "Part 1a: Counselling - Health Talks",
            {
                "fields": (
                    "receive_health_talk_messages",
                    "health_talk_conditions",
                    "health_talk_conditions_other",
                    "health_talk_focus",
                    "health_talk_focus_other",
                    "health_talk_presenters",
                    "health_talk_presenters_other",
                )
            },
        ),
        (
            "Part 1b: Counselling - Additional Health Advice",
            {
                "fields": (
                    "additional_health_advice",
                    "health_advice_advisor",
                    "health_advice_advisor_other",
                    "health_advice_focus",
                    "health_advice_focus_other",
                )
            },
        ),
        (
            "Part 2: Pharmacy Services",
            {
                "fields": (
                    "receive_prescription_today",
                    "prescription_collection_hcf",
                    "where_drugs_dispensed",
                    "where_drugs_dispensed_other",
                    "who_dispenses_drugs",
                    "who_dispenses_drugs_other",
                )
            },
        ),
        (
            "Part 3: Managing Clinic Records and Appointments",
            {
                "fields": (
                    "hospital_card",
                    "hospital_card_type",
                    "missed_appointment",
                    "missed_appointment_call",
                    "missed_appointment_call_who",
                    "missed_appointment_call_who_other",
                )
            },
        ),
        (
            "Part 4: Laboratory Services",
            {
                "fields": (
                    "laboratory_tests",
                    "pay_for_laboratory_tests",
                    "which_laboratory_tests_charged_for",
                    "which_laboratory_tests_charged_for_other",
                )
            },
        ),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    radio_fields = {
        "receive_health_talk_messages": admin.VERTICAL,
        "additional_health_advice": admin.VERTICAL,
        "receive_prescription_today": admin.VERTICAL,
        "prescription_collection_hcf": admin.VERTICAL,
        "hospital_card": admin.VERTICAL,
        "hospital_card_type": admin.VERTICAL,
        "missed_appointment": admin.VERTICAL,
        "missed_appointment_call": admin.VERTICAL,
        "missed_appointment_call_who": admin.VERTICAL,
        "laboratory_tests": admin.VERTICAL,
        "pay_for_laboratory_tests": admin.VERTICAL,
    }

    filter_horizontal = [
        "health_talk_conditions",
        "health_talk_focus",
        "health_talk_presenters",
        "health_advice_advisor",
        "health_advice_focus",
        "where_drugs_dispensed",
        "who_dispenses_drugs",
        "which_laboratory_tests_charged_for",
    ]
