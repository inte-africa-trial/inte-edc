from edc_model_admin.admin_site import EdcAdminSite

from .apps import AppConfig

inte_subject_admin = EdcAdminSite(name="inte_subject_admin", app_label=AppConfig.name)
