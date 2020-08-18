from django.test import TestCase, tag
from edc_appointment.constants import INCOMPLETE_APPT
from edc_metadata import REQUIRED
from edc_metadata.models import CrfMetadata
from edc_utils import get_utcnow
from inte_screening.constants import HIV_CLINIC
from tests.inte_test_case_mixin import InteTestCaseMixin
from model_bakery import baker


class TestIndicators(InteTestCaseMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.subject_screening = self.get_subject_screening(
            report_datetime=get_utcnow(), clinic_type=HIV_CLINIC
        )
        self.subject_consent = self.get_subject_consent(
            subject_screening=self.subject_screening, clinic_type=HIV_CLINIC
        )
        self.subject_visit = self.get_subject_visit(
            subject_screening=self.subject_screening,
            subject_consent=self.subject_consent,
        )

    @tag("fam")
    def test_weight_height_required_at_baseline(self):
        self.fail("see tests")

    @tag("fam")
    def test_weight_height_not_required_if_not_baseline(self):
        self.fail("see tests")
