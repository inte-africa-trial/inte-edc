from django.test import TestCase
from edc_appointment.constants import INCOMPLETE_APPT
from edc_utils import get_utcnow
from model_bakery import baker

from inte_screening.constants import HIV_CLINIC
from tests.inte_test_case_mixin import InteTestCaseMixin


class TestFamilyHistory(InteTestCaseMixin, TestCase):
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

    def test_not_required_at_baseline(self):
        crfs = self.get_crf_metadata(self.subject_visit)
        self.assertNotIn("inte_subject.familyhistory", [o.model for o in crfs.all()])
        self.subject_visit.save()

        crfs = self.get_crf_metadata(self.subject_visit)
        self.assertNotIn("inte_subject.familyhistory", [o.model for o in crfs.all()])

    def test_required_at_next_visit(self):
        self.subject_visit.appointment.appt_status = INCOMPLETE_APPT
        self.subject_visit.appointment.save()
        self.subject_visit.appointment.refresh_from_db()

        subject_visit = self.get_subject_visit(
            subject_screening=self.subject_screening,
            subject_consent=self.subject_consent,
            visit_code=self.subject_visit.appointment.next.visit_code,
        )

        crfs = self.get_crf_metadata(subject_visit)
        self.assertIn("inte_subject.familyhistory", [o.model for o in crfs.all()])

    def test_required_at_next_visit_if_not_completed_previously(self):

        self.subject_visit.appointment.appt_status = INCOMPLETE_APPT
        self.subject_visit.appointment.save()
        self.subject_visit.appointment.refresh_from_db()

        subject_visit = self.get_subject_visit(
            subject_screening=self.subject_screening,
            subject_consent=self.subject_consent,
            visit_code=self.subject_visit.appointment.next.visit_code,
        )

        family_history = baker.make("inte_subject.familyhistory", subject_visit=subject_visit)
        family_history.save()

        subject_visit.appointment.appt_status = INCOMPLETE_APPT
        subject_visit.appointment.save()
        subject_visit.appointment.refresh_from_db()

        subject_visit = self.get_subject_visit(
            subject_screening=self.subject_screening,
            subject_consent=self.subject_consent,
            visit_code=subject_visit.appointment.next.visit_code,
        )
        crfs = self.get_crf_metadata(subject_visit)
        self.assertNotIn("inte_subject.familyhistory", [o.model for o in crfs.all()])
