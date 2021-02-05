from django.test import TestCase, tag
from django.test.utils import override_settings
from edc_utils import get_utcnow

from inte_prn.forms import IntegratedCareClinicRegistrationForm

from ..inte_test_case_mixin import InteTestCaseMixin


class TestIccRegistrationLog(InteTestCaseMixin, TestCase):
    @override_settings(SITE_ID=103)
    def test_icc_registration_intervention(self):
        cleaned_data = {
            "report_datetime": get_utcnow(),
            "date_open": get_utcnow(),
            "comment": "",
        }
        form = IntegratedCareClinicRegistrationForm(data=cleaned_data)
        form.is_valid()
        self.assertNotIn("__all__", [k for k in form._errors.keys()])

    @override_settings(SITE_ID=101)
    def test_icc_registration_control(self):
        cleaned_data = {
            "report_datetime": get_utcnow(),
            "date_open": get_utcnow(),
            "comment": "",
        }
        form = IntegratedCareClinicRegistrationForm(data=cleaned_data)
        form.is_valid()
        self.assertIn("__all__", [k for k in form._errors.keys()])
