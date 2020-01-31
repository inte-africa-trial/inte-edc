from django.conf import settings
from datetime import datetime
from dateutil.relativedelta import MO, TU, WE, TH, FR, SA, SU
from dateutil.tz import gettz
from django.apps import AppConfig as DjangoAppConfig
from django.apps import apps as django_apps
from django.core.checks import register
from django.core.management.color import color_style
from django.db.models.signals import post_migrate
from edc_appointment.appointment_config import AppointmentConfig
from edc_appointment.apps import AppConfig as BaseEdcAppointmentAppConfig
from edc_device.apps import AppConfig as BaseEdcDeviceAppConfig
from edc_device.constants import CENTRAL_SERVER
from edc_facility.apps import AppConfig as BaseEdcFacilityAppConfig
from edc_identifier.apps import AppConfig as BaseEdcIdentifierAppConfig
from edc_metadata.apps import AppConfig as BaseEdcMetadataAppConfig
from edc_protocol.apps import AppConfig as BaseEdcProtocolAppConfig
from edc_visit_tracking.apps import AppConfig as BaseEdcVisitTrackingAppConfig
from edc_auth.group_permissions_updater import GroupPermissionsUpdater

style = color_style()

protocol_number = "102"


def post_migrate_update_edc_auth(sender=None, **kwargs):
    from inte_auth.codenames_by_group import get_codenames_by_group

    GroupPermissionsUpdater(
        codenames_by_group=get_codenames_by_group(), verbose=True, apps=django_apps
    )


class AppConfig(DjangoAppConfig):
    name = "inte_edc"

    def ready(self):
        post_migrate.connect(post_migrate_update_edc_auth, sender=self)

        from edc_randomization.system_checks import randomization_list_check

        register(randomization_list_check)(["inte_edc"])
        # register(inte_check)


class EdcProtocolAppConfig(BaseEdcProtocolAppConfig):
    institution = "Liverpool School of Tropical Medicine (LSTM)"
    project_name = "INTE"
    project_repo = "https://github.com/inte-africa-trail"
    protocol = "INTE"
    protocol_name = "INTE"
    protocol_number = protocol_number
    protocol_title = "INTE Africa Trial"
    study_open_datetime = datetime(2019, 7, 31, 0, 0, 0, tzinfo=gettz("UTC"))
    study_close_datetime = datetime(
        2022, 12, 31, 23, 59, 59, tzinfo=gettz("UTC"))


class EdcDeviceAppConfig(BaseEdcDeviceAppConfig):
    device_role = CENTRAL_SERVER
    device_id = "99"


class EdcVisitTrackingAppConfig(BaseEdcVisitTrackingAppConfig):
    visit_models = {"inte_subject": (
        "subject_visit", "inte_subject.subjectvisit")}


class EdcIdentifierAppConfig(BaseEdcIdentifierAppConfig):
    identifier_prefix = protocol_number
    subject_identifier_pattern = f"{protocol_number}\-[0-9\-]+"


class EdcMetadataAppConfig(BaseEdcMetadataAppConfig):
    reason_field = {"inte_subject.subjectvisit": "reason"}


class EdcAppointmentAppConfig(BaseEdcAppointmentAppConfig):
    configurations = [
        AppointmentConfig(
            model="edc_appointment.appointment",
            related_visit_model="inte_subject.subjectvisit",
            appt_type="hospital",
        )
    ]


class EdcFacilityAppConfig(BaseEdcFacilityAppConfig):
    country = settings.COUNTRY
    definitions = {
        "7-day-clinic": dict(
            days=[MO, TU, WE, TH, FR, SA, SU], slots=[
                100, 100, 100, 100, 100, 100, 100]
        ),
        "5-day-clinic": dict(
            days=[MO, TU, WE, TH, FR], slots=[100, 100, 100, 100, 100]
        ),
    }
