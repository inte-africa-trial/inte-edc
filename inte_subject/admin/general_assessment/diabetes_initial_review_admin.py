from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin


from ...admin_site import inte_subject_admin
from ...forms import DiabetesInitialReviewForm
from ...models import DiabetesInitialReview
from ..modeladmin import CrfModelAdminMixin


@admin.register(DiabetesInitialReview, site=inte_subject_admin)
class DiabetesInitialReviewAdmin(
    CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin
):

    form = DiabetesInitialReviewForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            None,
            {
                "fields": (
                    "diagnosis_date",
                    "treatment_start_date",
                    "treatment_start_date_estimated",
                    "lifestyle_management",
                    "on_treatment",
                    "treatment",
                    "visual_problems",
                    "kidney_problems",
                    "foot_ulcers",
                    "numbness",
                    "family_history",
                ),
            },
        ),
        audit_fieldset_tuple,
    )

    filter_horizontal = ("treatment",)

    radio_fields = {
        "lifestyle_management": admin.VERTICAL,
        "treatment_start_date_estimated": admin.VERTICAL,
        "on_treatment": admin.VERTICAL,
        "visual_problems": admin.VERTICAL,
        "kidney_problems": admin.VERTICAL,
        "foot_ulcers": admin.VERTICAL,
        "numbness": admin.VERTICAL,
        "family_history": admin.VERTICAL,
    }
