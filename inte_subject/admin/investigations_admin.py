from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_crf.admin import crf_status_fieldset_tuple
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin

from ..admin_site import inte_subject_admin
from ..forms import InvestigationsForm
from ..models import Investigations
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(Investigations, site=inte_subject_admin)
class InvestigationsAdmin(
    CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin
):
    form = InvestigationsForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "Investigations",
            {
                "fields": (
                    "hypertension_tested",
                    "diabetes_tested",
                    "hiv_tested",
                    "reason",
                    "reason_other",
                    "test_date",
                )
            },
        ),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    radio_fields = {
        "hypertension_tested": admin.VERTICAL,
        "diabetes_tested": admin.VERTICAL,
        "hiv_tested": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }

    filter_horizontal = ["reason"]
