from edc_model_admin.admin_site import EdcAdminSite

from .apps import AppConfig

inte_ae_admin = EdcAdminSite(name="inte_ae_admin", app_label=AppConfig.name)
