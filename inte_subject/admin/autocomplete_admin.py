from django.contrib import admin
from edc_list_data.admin import ListModelAdminMixin

from ..admin_site import inte_subject_admin
from ..models import ArvRegimens


@admin.register(ArvRegimens, site=inte_subject_admin)
class ArvRegimensAdmin(ListModelAdminMixin):
    pass
