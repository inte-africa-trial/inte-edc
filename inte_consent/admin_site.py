from django.contrib.admin import AdminSite as DjangoAdminSite
from django.contrib.sites.shortcuts import get_current_site
from edc_sites.models import SiteProfile


class AdminSite(DjangoAdminSite):

    site_title = "INTE: Consents"
    site_header = "INTE: Consents"
    index_title = "INTE: Consents"
    site_url = "/administration/"

    def each_context(self, request):
        context = super().each_context(request)
        title = SiteProfile.objects.get(site=get_current_site(request)).title
        context.update(global_site=get_current_site(request))
        label = f"INTE: {title.title()} - Consents"
        context.update(site_title=label, site_header=label, index_title=label)
        return context


inte_consent_admin = AdminSite(name="inte_consent_admin")
inte_consent_admin.disable_action("delete_selected")
