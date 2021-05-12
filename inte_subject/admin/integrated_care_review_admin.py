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
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    radio_fields = {
        "receive_health_talk_messages": admin.VERTICAL,
        "additional_health_advice": admin.VERTICAL,
    }

    filter_horizontal = [
        "health_talk_conditions",
        "health_talk_focus",
        "health_talk_presenters",
        "health_advice_advisor",
        "health_advice_focus",
    ]
