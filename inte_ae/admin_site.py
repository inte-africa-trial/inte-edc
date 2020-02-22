from django.contrib.admin import AdminSite as DjangoAdminSite
from django.contrib.sites.shortcuts import get_current_site


class AdminSite(DjangoAdminSite):
    site_title = "INTE: Adverse Events"
    site_header = "INTE: Adverse Events"
    index_title = "INTE: Adverse Events"
    site_url = "/administration/"

    def each_context(self, request):
        context = super().each_context(request)
        context.update(global_site=get_current_site(request))
        label = f"Inte {get_current_site(request).name.title()}: Adverse Events"
        context.update(site_title=label, site_header=label, index_title=label)
        return context


inte_ae_admin = AdminSite(name="inte_ae_admin")
inte_ae_admin.disable_action("delete_selected")
