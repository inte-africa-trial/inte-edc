from edc_crf.admin import CrfStatusModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin
from edc_model_admin.dashboard import (
    ModelAdminSubjectDashboardMixin,
    ModelAdminCrfDashboardMixin,
)


class ModelAdminMixin(ModelAdminSubjectDashboardMixin):
    pass


class CrfModelAdminMixin(CrfStatusModelAdminMixin, ModelAdminCrfDashboardMixin):

    pass


class CrfModelAdmin(ModelAdminCrfDashboardMixin, SimpleHistoryAdmin):

    pass


class DrugSupplyInlineMixin:

    extra = 1
    view_on_site = False

    fieldsets = (
        [
            "Drug Supply",
            {
                "description": (
                    "For each drug, please state for many days supply "
                    "did the participant receive from the pharmacy "
                    "and/or purchase themselves"
                ),
                "fields": ("drug", "clinic_days", "club_days", "purchased_days"),
            },
        ],
    )
