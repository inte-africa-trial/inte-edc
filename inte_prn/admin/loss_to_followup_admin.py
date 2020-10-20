from django.contrib import admin
from edc_ltfu.modeladmin_mixin import LossToFollowupModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin
from edc_model_admin.dashboard import ModelAdminSubjectDashboardMixin

from ..admin_site import inte_prn_admin
from ..forms import LossToFollowupForm
from ..models import LossToFollowup


@admin.register(LossToFollowup, site=inte_prn_admin)
class LossToFollowupAdmin(
    LossToFollowupModelAdminMixin, ModelAdminSubjectDashboardMixin, SimpleHistoryAdmin
):

    form = LossToFollowupForm
