from django.contrib import admin
from edc_model_admin import SimpleHistoryAdmin

from ..admin_site import inte_prn_admin
from ..models import OffScheduleNcd
from .modeladmin_mixins import EndOfStudyModelAdminMixin


@admin.register(OffScheduleNcd, site=inte_prn_admin)
class OffScheduleNcdAdmin(EndOfStudyModelAdminMixin, SimpleHistoryAdmin):

    pass
