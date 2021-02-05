from django.contrib import admin
from edc_model_admin import SimpleHistoryAdmin
from edc_model_admin.dashboard import ModelAdminSubjectDashboardMixin

from ..admin_site import inte_prn_admin
from ..models import OnScheduleHiv, OnScheduleNcd


@admin.register(OnScheduleNcd, site=inte_prn_admin)
class OnScheduleNcdAdmin(ModelAdminSubjectDashboardMixin, SimpleHistoryAdmin):
    instructions = None
    fields = ("subject_identifier", "onschedule_datetime")

    list_display = ("subject_identifier", "dashboard", "onschedule_datetime")

    list_filter = ("onschedule_datetime",)

    def get_readonly_fields(self, request, obj=None):
        return ["subject_identifier", "onschedule_datetime"]


@admin.register(OnScheduleHiv, site=inte_prn_admin)
class OnScheduleHivAdmin(ModelAdminSubjectDashboardMixin, SimpleHistoryAdmin):
    instructions = None
    fields = ("subject_identifier", "onschedule_datetime")

    list_display = ("subject_identifier", "dashboard", "onschedule_datetime")

    list_filter = ("onschedule_datetime",)

    def get_readonly_fields(self, request, obj=None):
        return ["subject_identifier", "onschedule_datetime"]
