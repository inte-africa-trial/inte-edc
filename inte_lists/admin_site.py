from edc_model_admin.admin_site import EdcAdminSite

from .apps import AppConfig

inte_lists_admin = EdcAdminSite(name="inte_lists_admin", app_label=AppConfig.name)
