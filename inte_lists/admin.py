from django.contrib import admin
from edc_list_data.admin import ListModelAdminMixin

from .admin_site import inte_lists_admin
from .models import (
    ArvRegimens,
    Conditions,
    DiabetesTreatment,
    HypertensionTreatment,
    OffstudyReasons,
    VisitReasons,
)


@admin.register(Conditions, site=inte_lists_admin)
class ConditionsAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(OffstudyReasons, site=inte_lists_admin)
class OffstudyReasonsAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(HypertensionTreatment, site=inte_lists_admin)
class HypertensionTreatmentAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(ArvRegimens, site=inte_lists_admin)
class ArvRegimensAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(VisitReasons, site=inte_lists_admin)
class VisitReasonsAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(DiabetesTreatment, site=inte_lists_admin)
class DiabetesTreatmentAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass
