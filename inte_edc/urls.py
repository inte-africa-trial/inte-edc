from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls.conf import include, path
from django.views.defaults import page_not_found, server_error  # noqa
from django.views.generic.base import RedirectView
from edc_action_item.admin_site import edc_action_item_admin
from edc_adverse_event.admin_site import edc_adverse_event_admin
from edc_appointment.admin_site import edc_appointment_admin
from edc_crf.admin_site import edc_crf_admin
from edc_dashboard.views import AdministrationView
from edc_data_manager.admin_site import edc_data_manager_admin
from edc_export.admin_site import edc_export_admin
from edc_facility.admin_site import edc_facility_admin
from edc_identifier.admin_site import edc_identifier_admin
from edc_lab.admin_site import edc_lab_admin
from edc_locator.admin_site import edc_locator_admin
from edc_metadata.admin_site import edc_metadata_admin
from edc_notification.admin_site import edc_notification_admin
from edc_offstudy.admin_site import edc_offstudy_admin
from edc_pdutils.admin_site import edc_pdutils_admin
from edc_pharmacy.admin_site import edc_pharmacy_admin
from edc_randomization.admin_site import edc_randomization_admin
from edc_reference.admin_site import edc_reference_admin
from edc_registration.admin_site import edc_registration_admin
from edc_visit_schedule.admin_site import edc_visit_schedule_admin

from inte_ae.admin_site import inte_ae_admin
from inte_consent.admin_site import inte_consent_admin
from inte_export.admin_site import inte_export_admin
from inte_lists.admin_site import inte_lists_admin
from inte_prn.admin_site import inte_prn_admin
from inte_screening.admin_site import inte_screening_admin
from inte_subject.admin_site import inte_subject_admin

from .views import HomeView


def trigger_error(request):
    division_by_zero = 1 / 0  # noqa


handler403 = "edc_dashboard.views.edc_handler403"
handler404 = "edc_dashboard.views.edc_handler404"

if settings.SENTRY_ENABLED:
    handler500 = "edc_dashboard.views.error_handlers.sentry.handler500"
else:
    handler500 = "edc_dashboard.views.edc_handler500"

urlpatterns = [
    path("sentry-debug/", trigger_error),
    path("accounts/", include("edc_auth.urls")),
    path("admin/", include("edc_auth.urls")),
    path("admin/", edc_appointment_admin.urls),
    path("admin/", edc_adverse_event_admin.urls),
    path("admin/", edc_crf_admin.urls),
    path("admin/", edc_randomization_admin.urls),
    path("admin/", inte_consent_admin.urls),
    path("admin/", inte_subject_admin.urls),
    path("admin/", inte_ae_admin.urls),
    path("admin/", inte_lists_admin.urls),
    path("admin/", inte_export_admin.urls),
    path("admin/", inte_prn_admin.urls),
    path("admin/", inte_screening_admin.urls),
    path("admin/", edc_lab_admin.urls),
    path("admin/", edc_data_manager_admin.urls),
    path("admin/", edc_export_admin.urls),
    path("admin/", edc_locator_admin.urls),
    path("admin/", edc_facility_admin.urls),
    path("admin/", edc_identifier_admin.urls),
    path("admin/", edc_metadata_admin.urls),
    path("admin/", edc_notification_admin.urls),
    path("admin/", edc_offstudy_admin.urls),
    path("admin/", edc_registration_admin.urls),
    path("admin/", edc_reference_admin.urls),
    path("admin/", edc_action_item_admin.urls),
    path("admin/", edc_pdutils_admin.urls),
    path("admin/", edc_pharmacy_admin.urls),
    path("admin/", include("defender.urls")),  # defender admin
    path("admin/edc_visit_schedule/", edc_visit_schedule_admin.urls),
    path(
        "admin/inte_subject/",
        RedirectView.as_view(url="admin/inte_subject/"),
        name="subject_models_url",
    ),
    path("admin/", admin.site.urls),
    path("administration/", AdministrationView.as_view(), name="administration_url"),
    path("inte_consent/", include("inte_consent.urls")),
    path("inte_subject/", include("inte_subject.urls")),
    path("inte_ae/", include("inte_ae.urls")),
    path("inte_export/", include("inte_export.urls")),
    path("inte_lists/", include("inte_lists.urls")),
    path("inte_prn/", include("inte_prn.urls")),
    path("inte_screening/", include("inte_screening.urls")),
    path("subject/", include("inte_dashboard.urls")),
    path("edc_adverse_event/", include("edc_adverse_event.urls")),
    path("edc_appointment/", include("edc_appointment.urls")),
    path("edc_action_item/", include("edc_action_item.urls")),
    path("edc_auth/", include("edc_auth.urls")),
    path("edc_crf/", include("edc_crf.urls")),
    path("edc_randomization/", include("edc_randomization.urls")),
    path("edc_facility/", include("edc_facility.urls")),
    path("edc_dashboard/", include("edc_dashboard.urls")),
    path("edc_consent/", include("edc_consent.urls")),
    path("edc_data_manager/", include("edc_data_manager.urls")),
    path("edc_device/", include("edc_device.urls")),
    path("edc_export/", include("edc_export.urls")),
    path("edc_pdutils/", include("edc_pdutils.urls")),
    path("edc_offstudy/", include("edc_offstudy.urls")),
    path("edc_lab/", include("edc_lab.urls")),
    path("edc_lab_dashboard/", include("edc_lab_dashboard.urls")),
    path("edc_locator/", include("edc_locator.urls")),
    path("edc_label/", include("edc_label.urls")),
    path("edc_metadata/", include("edc_metadata.urls")),
    path("edc_notification/", include("edc_notification.urls")),
    path("edc_protocol/", include("edc_protocol.urls")),
    path("edc_pharmacy/", include("edc_pharmacy.urls")),
    path("edc_identifier/", include("edc_identifier.urls")),
    path("edc_reference/", include("edc_reference.urls")),
    path("edc_registration/", include("edc_registration.urls")),
    path("edc_subject_dashboard/", include("edc_subject_dashboard.urls")),
    path("edc_visit_schedule/", include("edc_visit_schedule.urls")),
    path(
        "switch_sites/",
        LogoutView.as_view(next_page=settings.INDEX_PAGE),
        name="switch_sites_url",
    ),
    path("home/", HomeView.as_view(), name="home_url"),
    path("", HomeView.as_view(), name="home_url"),
]
