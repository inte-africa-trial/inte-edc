from django.test import TestCase, tag
from edc_utils import get_utcnow
from edc_visit_schedule.constants import DAY1
from edc_visit_tracking.constants import SCHEDULED, UNSCHEDULED

from inte_screening.constants import HIV_CLINIC

from ..inte_test_case_mixin import InteTestCaseMixin


class TestVisitSchedule(InteTestCaseMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.subject_screening = self.get_subject_screening(
            report_datetime=get_utcnow(), clinic_type=HIV_CLINIC
        )
        self.subject_consent = self.get_subject_consent(
            subject_screening=self.subject_screening, clinic_type=HIV_CLINIC
        )

    @tag("vs")
    def test_baseline(self):
        subject_visit = self.get_subject_visit(
            subject_screening=self.subject_screening,
            subject_consent=self.subject_consent,
            visit_code=DAY1,
            reason=SCHEDULED,
        )
        self.assertEqual("1000", subject_visit.appointment.visit_code)
        self.assertEqual(0, subject_visit.appointment.visit_code_sequence)

    @tag("vs")
    def test_next_is_6m_12m(self):
        subject_visit = self.get_subject_visit(
            subject_screening=self.subject_screening,
            subject_consent=self.subject_consent,
            visit_code=DAY1,
            reason=SCHEDULED,
        )

        subject_visit = self.get_next_subject_visit(
            subject_visit=subject_visit,
            reason=SCHEDULED,
        )

        self.assertEqual("1060", subject_visit.appointment.visit_code)
        self.assertEqual(0, subject_visit.appointment.visit_code_sequence)

        subject_visit = self.get_next_subject_visit(
            subject_visit=subject_visit,
            reason=SCHEDULED,
        )

        self.assertEqual("1120", subject_visit.appointment.visit_code)
        self.assertEqual(0, subject_visit.appointment.visit_code_sequence)

    @tag("vs")
    def test_next_unscheduled(self):
        subject_visit = self.get_subject_visit(
            subject_screening=self.subject_screening,
            subject_consent=self.subject_consent,
            visit_code=DAY1,
            reason=SCHEDULED,
        )

        subject_visit = self.get_next_subject_visit(
            subject_visit=subject_visit,
            reason=UNSCHEDULED,
        )
        self.assertEqual("1000", subject_visit.appointment.visit_code)
        self.assertEqual(1, subject_visit.appointment.visit_code_sequence)

        subject_visit = self.get_next_subject_visit(
            subject_visit=subject_visit,
            reason=UNSCHEDULED,
        )

        self.assertEqual("1000", subject_visit.appointment.visit_code)
        self.assertEqual(2, subject_visit.appointment.visit_code_sequence)

        subject_visit = self.get_next_subject_visit(
            subject_visit=subject_visit,
            reason=SCHEDULED,
        )

        self.assertEqual("1060", subject_visit.appointment.visit_code)
        self.assertEqual(0, subject_visit.appointment.visit_code_sequence)
