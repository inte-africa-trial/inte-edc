from edc_model_admin.admin_site import EdcAdminSite

from .apps import AppConfig

inte_screening_admin = EdcAdminSite(name="inte_screening_admin", app_label=AppConfig.name)
