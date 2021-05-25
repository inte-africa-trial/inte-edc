from edc_model_admin.admin_site import EdcAdminSite

from .apps import AppConfig

inte_prn_admin = EdcAdminSite(name="inte_prn_admin", app_label=AppConfig.name)
