from django.contrib import admin
from edc_action_item import action_fieldset_tuple, action_fields
from edc_model_admin import audit_fieldset_tuple, SimpleHistoryAdmin
from edc_model_admin.dashboard import ModelAdminSubjectDashboardMixin
from inte_prn.models import IntegratedCareClinicRegistration

from ..admin_site import inte_prn_admin
from ..forms import EndOfStudyForm
from ..models import EndOfStudy


@admin.register(IntegratedCareClinicRegistration, site=inte_prn_admin)
class IntegratedCareClinicRegistrationAdmin(SimpleHistoryAdmin):

    form = IntegratedCareClinicRegistrationForm

    fieldsets = (
        [None, {"fields": ("report_datetime", "date_opened", "comment",)},],
        audit_fieldset_tuple,
    )

    list_display = (
        "site",
        "report_datetime",
        "date_opened",
    )
