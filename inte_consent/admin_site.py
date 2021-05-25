from edc_model_admin.admin_site import EdcAdminSite

from .apps import AppConfig

inte_consent_admin = EdcAdminSite(name="inte_consent_admin", app_label=AppConfig.name)
