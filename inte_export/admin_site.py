from edc_model_admin.admin_site import EdcAdminSite

from .apps import AppConfig

inte_export_admin = EdcAdminSite(name="inte_export_admin", app_label=AppConfig.name)
