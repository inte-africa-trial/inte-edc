from django.contrib.admin import AdminSite as DjangoAdminSite


class AdminSite(DjangoAdminSite):

    site_title = "INTE Export"
    site_header = "INTE Export"
    index_title = "INTE Export"
    site_url = "/administration/"
    enable_nav_sidebar = False  # DJ 3.1


inte_export_admin = AdminSite(name="inte_export_admin")
