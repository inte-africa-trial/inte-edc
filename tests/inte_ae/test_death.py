from django.test import override_settings, TestCase, tag
from edc_utils import get_utcnow
from inte_screening.constants import HIV_CLINIC
from tests.inte_test_case_mixin import InteTestCaseMixin


class TestDeath(InteTestCaseMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.subject_screening = self.get_subject_screening(
            report_datetime=get_utcnow(), clinic_type=HIV_CLINIC
        )
        self.subject_consent = self.get_subject_consent(
            subject_screening=self.subject_screening, clinic_type=HIV_CLINIC
        )

    def test_death(self):
        pass
