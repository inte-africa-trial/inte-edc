from django.contrib import admin
from edc_ltfu.modeladmin_mixin import LossToFollowupModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin
from edc_model_admin.dashboard import ModelAdminSubjectDashboardMixin

from ..admin_site import inte_prn_admin
from ..forms import LossToFollowupForm
from ..models import LossToFollowup, LossToFollowupHiv, LossToFollowupNcd


@admin.register(LossToFollowup, site=inte_prn_admin)
class LossToFollowupAdmin(
    LossToFollowupModelAdminMixin, ModelAdminSubjectDashboardMixin, SimpleHistoryAdmin
):

    form = LossToFollowupForm


@admin.register(LossToFollowupHiv, site=inte_prn_admin)
class LossToFollowupHivAdmin(
    LossToFollowupModelAdminMixin, ModelAdminSubjectDashboardMixin, SimpleHistoryAdmin
):

    form = LossToFollowupForm


@admin.register(LossToFollowupNcd, site=inte_prn_admin)
class LossToFollowupNcdAdmin(
    LossToFollowupModelAdminMixin, ModelAdminSubjectDashboardMixin, SimpleHistoryAdmin
):

    form = LossToFollowupForm
