from django.utils.safestring import mark_safe
from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin


from ...admin_site import inte_subject_admin
from ...forms import HypertensionInitialReviewForm
from ...models import HypertensionInitialReview
from ..modeladmin import CrfModelAdminMixin


@admin.register(HypertensionInitialReview, site=inte_subject_admin)
class HypertensionInitialReviewAdmin(
    CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin
):

    form = HypertensionInitialReviewForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "Diagnosis and Treatment",
            {
                "fields": (
                    "diagnosis_date",
                    "diagnosis_date_estimated",
                    "on_treatment",
                    "treatment",
                    "other_treatment",
                    "family_history",
                ),
            },
        ),
        audit_fieldset_tuple,
    )

    filter_horizontal = ("treatment",)

    radio_fields = {
        "diagnosis_date_estimated": admin.VERTICAL,
        "on_treatment": admin.VERTICAL,
        "family_history": admin.VERTICAL,
    }
