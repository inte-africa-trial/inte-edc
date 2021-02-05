from django.contrib import admin
from edc_model_admin import SimpleHistoryAdmin, audit_fieldset_tuple

from inte_prn.forms import IntegratedCareClinicRegistrationForm
from inte_prn.models import IntegratedCareClinicRegistration

from ..admin_site import inte_prn_admin


@admin.register(IntegratedCareClinicRegistration, site=inte_prn_admin)
class IntegratedCareClinicRegistrationAdmin(SimpleHistoryAdmin):

    form = IntegratedCareClinicRegistrationForm

    fieldsets = (
        [None, {"fields": ("date_opened", "comment")}],
        audit_fieldset_tuple,
    )

    list_display = (
        "site",
        "report_datetime",
        "date_opened",
    )
