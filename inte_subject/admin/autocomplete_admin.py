from django.contrib import admin
from edc_list_data.admin import ListModelAdminMixin

from inte_lists.models import ArvRegimens

from ..admin_site import inte_subject_admin


@admin.register(ArvRegimens, site=inte_subject_admin)
class ArvRegimensAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass
