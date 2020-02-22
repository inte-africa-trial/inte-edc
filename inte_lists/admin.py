from django.contrib import admin
from edc_list_data.admin import ListModelAdminMixin

from .admin_site import inte_lists_admin
from .models import (
    Conditions,
    OffstudyReasons,
)


@admin.register(Conditions, site=inte_lists_admin)
class ConditionsAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(OffstudyReasons, site=inte_lists_admin)
class OffstudyReasonsAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass
