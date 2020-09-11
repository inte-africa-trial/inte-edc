from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_crf.admin import crf_status_fieldset_tuple
from edc_form_label import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin

from ..admin_site import inte_subject_admin
from ..forms import HealthEconomicsRevisedForm
from ..models import HealthEconomicsRevised
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(HealthEconomicsRevised, site=inte_subject_admin)
class HealthEconomicsRevisedAdmin(
    CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin
):

    form = HealthEconomicsRevisedForm
    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "Part 1: Education",
            {
                "fields": (
                    "occupation",
                    "education_in_years",
                    "education_certificate",
                    "primary_school",
                    "primary_school_in_years",
                    "secondary_school",
                    "secondary_school_in_years",
                    "higher_education",
                    "higher_education_in_years",
                )
            },
        ),
        (
            "Part 2: Income",
            {
                "fields": (
                    "welfare",
                    "income_per_month",
                    "household_income_per_month",
                    "is_highest_earner",
                    "highest_earner",
                )
            },
        ),
        (
            "Part 3: General Expenses",
            {
                "fields": (
                    "food_per_month",
                    "accomodation_per_month",
                    "large_expenditure_year",
                )
            },
        ),
        (
            "Part 4: Previous Healthcare Expenses: Medication",
            {
                "fields": (
                    "received_rx_month",
                    "rx_dm_month",
                    "rx_dm_paid_month",
                    "rx_dm_cost_month",
                    "rx_htn_month",
                    "rx_htn_paid_month",
                    "rx_htn_cost_month",
                    "rx_hiv_month",
                    "rx_hiv_paid_month",
                    "rx_hiv_cost_month",
                    "rx_other_month",
                    "rx_other_paid_month",
                    "rx_other_cost_month",
                )
            },
        ),
        (
            "Part 5: Previous Healthcare Expenses: Non-medication",
            {
                "fields": (
                    "non_drug_activities_month",
                    "non_drug_activities_detail_month",
                    "non_drug_activities_cost_month",
                    "healthcare_expenditure_total_month",
                )
            },
        ),
        (
            "Part 6: Family Loss of Productivity and Earnings",
            {
                "fields": (
                    "missed_routine_activities",
                    "missed_routine_activities_other",
                    "off_work_days",
                    "travel_time",
                    "hospital_time",
                    "lost_income",
                    "lost_income_amount",
                )
            },
        ),
        (
            "Part 7: Work, Childcare, Transport",
            {
                "fields": (
                    "childcare",
                    "childcare_source",
                    "childcare_source_other",
                    "childcare_source_timeoff",
                    "transport",
                    "transport_other",
                    "transport_cost",
                    "food_cost",
                )
            },
        ),
        (
            "Part 8: Current Visit Healthcare Expenses: Medications",
            {
                "fields": (
                    "received_rx_today",
                    "rx_dm_today",
                    "rx_dm_paid_today",
                    "rx_dm_cost_today",
                    "rx_htn_today",
                    "rx_htn_paid_today",
                    "rx_htn_cost_today",
                    "rx_hiv_today",
                    "rx_hiv_paid_today",
                    "rx_hiv_cost_today",
                    "rx_other_today",
                    "rx_other_paid_today",
                    "rx_other_cost_today",
                )
            },
        ),
        (
            "Part 9: Current Visit Healthcare Expenses: Non-medications",
            {
                "fields": (
                    "non_drug_activities_today",
                    "non_drug_activities_detail_today",
                    "non_drug_activities_cost_today",
                )
            },
        ),
        (
            "Part 10: Health Care Financing",
            {
                "fields": (
                    "finance_by_sale",
                    "finance_by_loan",
                    "health_insurance",
                    "health_insurance_cost",
                    "patient_club",
                    "patient_club_cost",
                )
            },
        ),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    radio_fields = {
        "childcare": admin.VERTICAL,
        "childcare_source": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
        "finance_by_loan": admin.VERTICAL,
        "finance_by_sale": admin.VERTICAL,
        "health_insurance": admin.VERTICAL,
        "higher_education": admin.VERTICAL,
        "is_highest_earner": admin.VERTICAL,
        "lost_income": admin.VERTICAL,
        "missed_routine_activities": admin.VERTICAL,
        "non_drug_activities_month": admin.VERTICAL,
        "non_drug_activities_today": admin.VERTICAL,
        "patient_club": admin.VERTICAL,
        "primary_school": admin.VERTICAL,
        "received_rx_month": admin.VERTICAL,
        "received_rx_today": admin.VERTICAL,
        "rx_dm_month": admin.VERTICAL,
        "rx_dm_today": admin.VERTICAL,
        "rx_hiv_month": admin.VERTICAL,
        "rx_hiv_today": admin.VERTICAL,
        "rx_htn_month": admin.VERTICAL,
        "rx_htn_today": admin.VERTICAL,
        "rx_other_month": admin.VERTICAL,
        "rx_other_today": admin.VERTICAL,
        "transport": admin.VERTICAL,
        "secondary_school": admin.VERTICAL,
        "welfare": admin.VERTICAL,
    }

    filter_horizontal = [
        "rx_dm_paid_month",
        "rx_htn_paid_month",
        "rx_hiv_paid_month",
        "rx_other_paid_month",
        "transport",
        "rx_dm_paid_today",
        "rx_htn_paid_today",
        "rx_hiv_paid_today",
        "rx_other_paid_today",
    ]
