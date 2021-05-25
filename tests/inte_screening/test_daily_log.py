import pdb

from dateutil.relativedelta import relativedelta
from django.contrib.sites.models import Site
from django.test import TestCase, override_settings, tag
from edc_utils import get_utcnow

from inte_prn.models import IntegratedCareClinicRegistration
from inte_screening.constants import SEQUENTIAL
from inte_screening.forms import DailyClosingLogForm
from inte_subject.constants import INTEGRATED
from tests.inte_test_case_mixin import InteTestCaseMixin


class TestDailyLog(InteTestCaseMixin, TestCase):
    def setUp(self):
        super().setUp()

        self.data = {
            "site": Site.objects.get_current(),
            "log_date": get_utcnow().date(),
            "clinic_services": INTEGRATED,
            "selection_method": SEQUENTIAL,
            "attended": 10,
            "approached": 10,
            "agreed_to_screen": 10,
        }

    @tag("daily")
    @override_settings(
        SITE_ID=103,
        INTE_SCREENING_DCL_REVISION_DATETIME=get_utcnow().date() + relativedelta(days=1),
    )
    def test_integrated_for_intervention_site(self):
        form = DailyClosingLogForm(data=self.data)
        form.is_valid()
        self.assertIn("clinic_services", form._errors)

        # register the site
        IntegratedCareClinicRegistration.objects.create(date_opened=get_utcnow().date())
        form = DailyClosingLogForm(data=self.data)
        form.is_valid()
        self.assertNotIn("clinic_services", form._errors)

    @tag("daily")
    @override_settings(
        SITE_ID=101,
        INTE_SCREENING_DCL_REVISION_DATETIME=get_utcnow().date() + relativedelta(days=1),
    )
    def test_integrated_for_control_site(self):
        form = DailyClosingLogForm(data=self.data)
        form.is_valid()
        self.assertIn("clinic_services", form._errors)

    @tag("daily")
    @override_settings(
        SITE_ID=103,
        INTE_SCREENING_DCL_REVISION_DATETIME=get_utcnow().date() + relativedelta(days=1),
    )
    def test_numbers(self):
        IntegratedCareClinicRegistration.objects.create(date_opened=get_utcnow().date())
        data = {
            "site": Site.objects.get_current(),
            "log_date": get_utcnow(),
            "clinic_services": INTEGRATED,
            "selection_method": SEQUENTIAL,
            "attended": 10,
            "approached": 10,
            "agreed_to_screen": 10,
        }
        form = DailyClosingLogForm(data=data)
        form.is_valid()
        self.assertDictEqual({}, form._errors)

        data.update(approached=11)

        form = DailyClosingLogForm(data=data)
        form.is_valid()
        self.assertIn("approached", form._errors)

        data.update(approached=10, agreed_to_screen=11)

        form = DailyClosingLogForm(data=data)
        form.is_valid()
        self.assertIn("agreed_to_screen", form._errors)
