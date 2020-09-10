from django.contrib import admin
from edc_list_data.admin import ListModelAdminMixin

from .admin_site import inte_lists_admin
from .models import (
    ArvDrugs,
    ArvRegimens,
    ClinicServices,
    Conditions,
    DmTreatments,
    HtnTreatments,
    OffstudyReasons,
    VisitReasons,
    HealthServices,
    RxModifications,
    RxModificationReasons,
)


@admin.register(Conditions, site=inte_lists_admin)
class ConditionsAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(OffstudyReasons, site=inte_lists_admin)
class OffstudyReasonsAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(HtnTreatments, site=inte_lists_admin)
class HtnTreatmentsAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(ArvRegimens, site=inte_lists_admin)
class ArvRegimensAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(VisitReasons, site=inte_lists_admin)
class VisitReasonsAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(DmTreatments, site=inte_lists_admin)
class DmTreatmentsAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(HealthServices, site=inte_lists_admin)
class HealthServicesAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(ClinicServices, site=inte_lists_admin)
class ClinicServicesAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(ArvDrugs, site=inte_lists_admin)
class ArvDrugsAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(RxModifications, site=inte_lists_admin)
class RxModificationsAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(RxModificationReasons, site=inte_lists_admin)
class RxModificationReasonsAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass
