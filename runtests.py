#!/usr/bin/env python
import logging
import os
import sys
from os.path import abspath, dirname, join

import django
from django.conf import settings
from django.test.runner import DiscoverRunner
from edc_test_utils import DefaultTestSettings
from edc_utils import get_datetime_from_env, get_utcnow
from multisite import SiteID

app_name = "inte_edc"
base_dir = dirname(abspath(__file__))

DEFAULT_SETTINGS = DefaultTestSettings(
    calling_file=__file__,
    BASE_DIR=base_dir,
    APP_NAME=app_name,
    SITE_ID=SiteID(default=101),
    INTE_SCREENING_DCL_REVISION_DATETIME=get_utcnow(),
    EDC_SITES_MODULE_NAME="inte_sites.sites",
    SUBJECT_VISIT_MODEL="inte_subject.subjectvisit",
    SUBJECT_VISIT_MISSED_MODEL="inte_subject.subjectvisitmissed",
    SUBJECT_CONSENT_MODEL="inte_consent.subjectconsent",
    SUBJECT_REQUISITION_MODEL="inte_subject.subjectrequisition",
    SUBJECT_APP_LABEL=f"{app_name.replace('edc', 'subject')}",
    RESPOND_DIAGNOSIS_LABELS=dict(hiv="HIV", htn="Hypertension", dm="Diabetes"),
    INTE_SUBJECT_HE_REVISION_DATE=get_datetime_from_env(2021, 4, 26, 0, 0, 0, "UTC"),
    EDC_PROTOCOL_STUDY_OPEN_DATETIME=get_datetime_from_env(2019, 6, 30, 0, 0, 0, "UTC"),
    EDC_PROTOCOL_STUDY_CLOSE_DATETIME=get_datetime_from_env(2024, 12, 31, 23, 59, 59, "UTC"),
    ADVERSE_EVENT_ADMIN_SITE="inte_ae_admin",
    ADVERSE_EVENT_APP_LABEL="inte_ae",
    EDC_NAVBAR_DEFAULT="inte_dashboard",
    DASHBOARD_BASE_TEMPLATES=dict(
        edc_base_template="edc_dashboard/base.html",
        listboard_base_template="inte_edc/base.html",
        dashboard_base_template="inte_edc/base.html",
        screening_listboard_template="inte_dashboard/screening/listboard.html",
        subject_listboard_template="inte_dashboard/subject/listboard.html",
        subject_dashboard_template="inte_dashboard/subject/dashboard.html",
        subject_review_listboard_template="edc_review_dashboard/subject_review_listboard.html",
    ),
    ETC_DIR=os.path.join(base_dir, "tests", "etc"),
    EDC_BOOTSTRAP=3,
    EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend",
    EMAIL_CONTACTS={
        "data_request": "someone@example.com",
        "data_manager": "someone@example.com",
    },
    EMAIL_ENABLED=True,
    HOLIDAY_FILE=join(base_dir, "tests", "holidays.csv"),
    LIVE_SYSTEM=False,
    EDC_RANDOMIZATION_LIST_PATH=join(base_dir, "tests", "etc"),
    EDC_RANDOMIZATION_REGISTER_DEFAULT_RANDOMIZER=False,
    DATABASES={
        # required for tests when acting as a server that deserializes
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(base_dir, "db.sqlite3"),
        },
    },
    INSTALLED_APPS=[
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "django.contrib.sites",
        "django_crypto_fields.apps.AppConfig",
        "django_revision.apps.AppConfig",
        "django_extensions",
        "django_celery_results",
        "django_celery_beat",
        "logentry_admin",
        "simple_history",
        "storages",
        "defender",
        "edc_action_item.apps.AppConfig",
        "edc_appointment.apps.AppConfig",
        "edc_adverse_event.apps.AppConfig",
        "edc_auth.apps.AppConfig",
        "edc_consent.apps.AppConfig",
        "edc_crf.apps.AppConfig",
        "edc_lab.apps.AppConfig",
        "edc_visit_schedule.apps.AppConfig",
        "edc_dashboard.apps.AppConfig",
        "edc_data_manager.apps.AppConfig",
        "edc_device.apps.AppConfig",
        "edc_export.apps.AppConfig",
        "edc_fieldsets.apps.AppConfig",
        "edc_form_validators.apps.AppConfig",
        "edc_identifier.apps.AppConfig",
        "edc_lab_dashboard.apps.AppConfig",
        "edc_label.apps.AppConfig",
        "edc_list_data.apps.AppConfig",
        "edc_locator.apps.AppConfig",
        "edc_metadata.apps.AppConfig",
        "edc_model_admin.apps.AppConfig",
        "edc_model_wrapper.apps.AppConfig",
        "edc_navbar.apps.AppConfig",
        "edc_notification.apps.AppConfig",
        "edc_offstudy.apps.AppConfig",
        "edc_pharmacy.apps.AppConfig",
        "edc_pdutils.apps.AppConfig",
        "edc_protocol.apps.AppConfig",
        "edc_prn.apps.AppConfig",
        "edc_randomization.apps.AppConfig",
        "edc_reference.apps.AppConfig",
        "edc_registration.apps.AppConfig",
        "edc_reportable.apps.AppConfig",
        "edc_reports.apps.AppConfig",
        "edc_review_dashboard.apps.AppConfig",
        "edc_sites.apps.AppConfig",
        "edc_subject_dashboard.apps.AppConfig",
        "edc_timepoint.apps.AppConfig",
        "edc_visit_tracking.apps.AppConfig",
        "inte_consent.apps.AppConfig",
        "inte_lists.apps.AppConfig",
        "inte_dashboard.apps.AppConfig",
        "inte_labs.apps.AppConfig",
        "inte_subject.apps.AppConfig",
        "inte_form_validators.apps.AppConfig",
        "inte_visit_schedule.apps.AppConfig",
        "inte_ae.apps.AppConfig",
        "inte_auth.apps.AppConfig",
        "inte_prn.apps.AppConfig",
        "inte_export.apps.AppConfig",
        "inte_screening.apps.AppConfig",
        "inte_sites.apps.AppConfig",
        "inte_edc.apps.EdcFacilityAppConfig",
        # "inte_edc.apps.AppConfigForTests",
        "inte_edc.apps.AppConfig",
    ],
    add_dashboard_middleware=True,
    add_lab_dashboard_middleware=True,
    add_adverse_event_dashboard_middleware=True,
).settings


def main():
    if not settings.configured:
        settings.configure(**DEFAULT_SETTINGS)
    django.setup()
    tags = [t.split("=")[1] for t in sys.argv if t.startswith("--tag")]
    failfast = True if [t for t in sys.argv if t == "--failfast"] else False
    failures = DiscoverRunner(failfast=failfast, tags=tags).run_tests(["tests"])
    sys.exit(bool(failures))


if __name__ == "__main__":
    logging.basicConfig()
    main()
