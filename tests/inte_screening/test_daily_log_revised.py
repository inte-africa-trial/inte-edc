from dateutil.relativedelta import relativedelta
from django.contrib.sites.models import Site
from django.test import override_settings, tag
from django.urls import reverse
from django_webtest import WebTest
from edc_auth import AUDITOR, EVERYONE, SCREENING
from edc_utils import get_utcnow

from inte_prn.models import IntegratedCareClinicRegistration
from inte_screening.forms import DailyClosingLogRevisedForm
from inte_subject.constants import INTEGRATED
from tests.inte_test_case_mixin import InteTestCaseMixin


class TestDailyLogRevised(InteTestCaseMixin, WebTest):
    def setUp(self):
        super().setUp()

        self.data = {
            "site": Site.objects.get_current(),
            "log_date": get_utcnow().date(),
            "clinic_services": INTEGRATED,
            "attended": 10,
            "clinic_start_time": "08:00",
            "clinic_end_time": "18:00",
        }

    @tag("daily")
    @override_settings(
        SITE_ID=103,
        INTE_SCREENING_DCL_REVISION_DATETIME=get_utcnow().date() - relativedelta(days=10),
    )
    def test_integrated_for_intervention_site(self):
        form = DailyClosingLogRevisedForm(data=self.data)
        form.is_valid()
        self.assertIn("clinic_services", form._errors)

        # register the site
        IntegratedCareClinicRegistration.objects.create(date_opened=get_utcnow().date())
        form = DailyClosingLogRevisedForm(data=self.data)
        form.is_valid()
        self.assertNotIn("clinic_services", form._errors)

    @tag("daily")
    @override_settings(
        SITE_ID=101,
        INTE_SCREENING_DCL_REVISION_DATETIME=get_utcnow().date() - relativedelta(days=10),
    )
    def test_integrated_for_control_site(self):
        form = DailyClosingLogRevisedForm(data=self.data)
        form.is_valid()
        self.assertIn("clinic_services", form._errors)

    @tag("daily")
    @override_settings(
        SITE_ID=103,
        INTE_SCREENING_DCL_REVISION_DATETIME=get_utcnow().date() - relativedelta(days=10),
    )
    def test_clinic_start_time(self):
        IntegratedCareClinicRegistration.objects.create(date_opened=get_utcnow().date())
        data = {
            "site": Site.objects.get_current(),
            "log_date": get_utcnow(),
            "clinic_services": INTEGRATED,
            "attended": 10,
            "clinic_start_time": "08:00",
            "clinic_end_time": "18:00",
        }
        form = DailyClosingLogRevisedForm(data=data)
        form.is_valid()
        self.assertDictEqual({}, form._errors)

        data.update(clinic_start_time="19:00")

        form = DailyClosingLogRevisedForm(data=data)
        form.is_valid()
        self.assertIn("clinic_start_time", form._errors)

        data.update(clinic_start_time="09:00", clinic_end_time="08:00")

        form = DailyClosingLogRevisedForm(data=data)
        form.is_valid()
        self.assertIn("clinic_start_time", form._errors)

    @tag("webtest1")
    @override_settings(
        INTE_SCREENING_DCL_REVISION_DATETIME=get_utcnow() + relativedelta(days=1)
    )
    def test_response_has_closing_log_url(self):
        closing_log_url = reverse(
            "inte_screening_admin:inte_screening_dailyclosinglog_changelist"
        )
        closing_log_revise_url = reverse(
            "inte_screening_admin:inte_screening_dailyclosinglogrevised_changelist"
        )
        self.login(superuser=False, groups=[EVERYONE, AUDITOR, SCREENING])
        response = self.app.get("/", user=self.user, status=200)
        self.assertNotIn(closing_log_revise_url, response)
        self.assertIn(closing_log_url, response)

    @tag("webtest1")
    @override_settings(
        INTE_SCREENING_DCL_REVISION_DATETIME=get_utcnow() - relativedelta(days=1)
    )
    def test_response_has_closing_log_revised_url(self):
        closing_log_url = reverse(
            "inte_screening_admin:inte_screening_dailyclosinglog_changelist"
        )
        closing_log_revise_url = reverse(
            "inte_screening_admin:inte_screening_dailyclosinglogrevised_changelist"
        )
        response = self.app.get("/", user=self.user, status=200)
        self.assertNotIn(closing_log_url, response)
        self.assertIn(closing_log_revise_url, response)
