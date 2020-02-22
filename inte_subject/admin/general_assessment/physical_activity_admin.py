from django.contrib import admin
from django.utils.safestring import mark_safe
from django_audit_fields.admin import audit_fieldset_tuple
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin

from ...admin_site import inte_subject_admin
from ...forms import PhysicalActivityForm
from ...models import PhysicalActivity
from ..modeladmin import CrfModelAdminMixin


@admin.register(PhysicalActivity, site=inte_subject_admin)
class PhysicalActivityAdmin(
    CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin
):
    form = PhysicalActivityForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "Physical Activity - Type",
            {
                "description": mark_safe(
                    "Please tell us the type and amount of physical activity "
                    "involved in your work.<BR>"
                    "(Please tick one box that is closest to your present work "
                    "from the following five possibilities)"
                ),
                "fields": ("physical_activity",),
            },
        ),
        (
            "Physical Activity - Hours spent",
            {
                "description": mark_safe(
                    "During the <u>last week</u>, how many hours did you spend on each of "
                    "the following activities? "
                ),
                "fields": (
                    "physical_exercise",
                    "cycling",
                    "walking",
                    "housework",
                    "casual_labour",
                    "physically_active",
                ),
            },
        ),
        audit_fieldset_tuple,
    )

    radio_fields = {
        "physical_activity": admin.VERTICAL,
        "physical_exercise": admin.VERTICAL,
        "cycling": admin.VERTICAL,
        "walking": admin.VERTICAL,
        "housework": admin.VERTICAL,
        "casual_labour": admin.VERTICAL,
        "physically_active": admin.VERTICAL,
    }
