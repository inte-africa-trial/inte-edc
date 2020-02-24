from django.contrib.admin import AdminSite as DjangoAdminSite


class AdminSite(DjangoAdminSite):

    site_title = "INTE Export"
    site_header = "INTE Export"
    index_title = "INTE Export"
    site_url = "/administration/"


inte_export_admin = AdminSite(name="inte_export_admin")
