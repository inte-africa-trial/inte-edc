from django.contrib import admin
from edc_action_item import action_fieldset_tuple
from edc_model_admin import SimpleHistoryAdmin, audit_fieldset_tuple
from edc_model_admin.dashboard import ModelAdminSubjectDashboardMixin

from ..admin_site import inte_prn_admin
from ..forms import UnblindingReviewForm
from ..models import UnblindingReview


@admin.register(UnblindingReview, site=inte_prn_admin)
class UnblindingReviewAdmin(ModelAdminSubjectDashboardMixin, SimpleHistoryAdmin):

    form = UnblindingReviewForm

    fieldsets = (
        ("Request", {"fields": ("subject_identifier", "report_datetime", "reviewer")}),
        ("Approval", {"fields": ("approved", "comment")}),
        action_fieldset_tuple,
        audit_fieldset_tuple,
    )

    autocomplete_fields = ["reviewer"]

    list_display = (
        "subject_identifier",
        "dashboard",
        "report_datetime",
        "reviewer",
        "approved",
        "action_identifier",
        "created",
    )

    radio_fields = {"approved": admin.VERTICAL}
