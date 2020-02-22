from django.contrib.admin import AdminSite as DjangoAdminSite
from django.contrib.sites.shortcuts import get_current_site
from edc_sites.models import SiteProfile


class AdminSite(DjangoAdminSite):

    site_title = "INTE Subject CRFs"
    site_header = "INTE Subject CRFs"
    index_title = "INTE Subject CRFs"
    site_url = "/administration/"

    def each_context(self, request):
        context = super().each_context(request)
        title = SiteProfile.objects.get(site=get_current_site(request)).title
        context.update(global_site=get_current_site(request))
        label = f"INTE: {title.title()} - Subject CRFs"
        context.update(site_title=label, site_header=label, index_title=label)
        return context


inte_subject_admin = AdminSite(name="inte_subject_admin")
inte_subject_admin.disable_action("delete_selected")
