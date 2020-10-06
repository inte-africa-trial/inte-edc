from django.contrib import admin
from django.utils.safestring import mark_safe
from django_audit_fields import audit_fieldset_tuple
from edc_crf.admin import crf_status_fieldset_tuple, CrfStatusModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin
from edc_model_admin.dashboard import (
    ModelAdminSubjectDashboardMixin,
    ModelAdminCrfDashboardMixin,
)

medication_adherence_description = """
<H5><B><font color="orange">Interviewer to read</font></B></H5>
<p>Drag the slider on the line below at
the point showing your best guess about how much medication
you have taken in the last 28 days:<BR><BR>
<B>0%</B> means you have taken no medication<BR>
<B>50%</B> means you have taken half of your medication<BR>
<B>100%</B> means you have taken all your medication<BR>
</p>
"""


class ModelAdminMixin(ModelAdminSubjectDashboardMixin):
    pass


class CrfModelAdminMixin(CrfStatusModelAdminMixin, ModelAdminCrfDashboardMixin):

    pass


class CrfModelAdmin(ModelAdminCrfDashboardMixin, SimpleHistoryAdmin):

    pass


class DrugSupplyInlineMixin:

    extra = 1
    view_on_site = False

    fieldsets = (
        [
            "Drug Supply",
            {
                "description": (
                    "For each drug, please state for many days supply "
                    "did the participant receive from the pharmacy "
                    "and/or purchase themselves"
                ),
                "fields": ("drug", "clinic_days", "club_days", "purchased_days"),
            },
        ],
    )


class MedicationAdherenceAdminMixin:

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "Visual Score",
            {
                "description": mark_safe(medication_adherence_description),
                "fields": ("visual_score_slider", "visual_score_confirmed"),
            },
        ),
        (
            "Missed Medications",
            {
                "fields": (
                    "last_missed_pill",
                    "missed_pill_reason",
                    "other_missed_pill_reason",
                )
            },
        ),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    filter_horizontal = ["missed_pill_reason"]

    radio_fields = {
        "last_missed_pill": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }
