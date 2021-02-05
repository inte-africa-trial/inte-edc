from django.test import TestCase, tag
from edc_appointment.constants import INCOMPLETE_APPT
from edc_metadata import REQUIRED
from edc_metadata.models import CrfMetadata
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

    @tag("fam")
    def test_not_required_at_baseline(self):
        crfs = CrfMetadata.objects.filter(
            subject_identifier=self.subject_visit.subject_identifier,
            visit_code=self.subject_visit.visit_code,
            visit_code_sequence=self.subject_visit.visit_code_sequence,
            entry_status=REQUIRED,
        )
        self.assertNotIn("inte_subject.familyhistory", [o.model for o in crfs.all()])
        self.subject_visit.save()
        crfs = CrfMetadata.objects.filter(
            subject_identifier=self.subject_visit.subject_identifier,
            visit_code=self.subject_visit.visit_code,
            visit_code_sequence=self.subject_visit.visit_code_sequence,
            entry_status=REQUIRED,
        )
        self.assertNotIn("inte_subject.familyhistory", [o.model for o in crfs.all()])

    @tag("fam")
    def test_required_at_next_visit(self):
        self.subject_visit.appointment.appt_status = INCOMPLETE_APPT
        self.subject_visit.appointment.save()
        self.subject_visit.appointment.refresh_from_db()

        subject_visit = self.get_subject_visit(
            subject_screening=self.subject_screening,
            subject_consent=self.subject_consent,
            visit_code=self.subject_visit.appointment.next.visit_code,
        )

        crfs = CrfMetadata.objects.filter(
            subject_identifier=subject_visit.subject_identifier,
            visit_code=subject_visit.visit_code,
            visit_code_sequence=subject_visit.visit_code_sequence,
            entry_status=REQUIRED,
        )
        self.assertIn("inte_subject.familyhistory", [o.model for o in crfs.all()])

    @tag("fam")
    def test_required_at_next_visit_if_not_completed_previously(self):
        self.subject_visit.appointment.appt_status = INCOMPLETE_APPT
        self.subject_visit.appointment.save()
        self.subject_visit.appointment.refresh_from_db()

        subject_visit = self.get_subject_visit(
            subject_screening=self.subject_screening,
            subject_consent=self.subject_consent,
            visit_code=self.subject_visit.appointment.next.visit_code,
        )

        baker.make("inte_subject.familyhistory", subject_visit=subject_visit)

        subject_visit.appointment.appt_status = INCOMPLETE_APPT
        subject_visit.appointment.save()
        subject_visit.appointment.refresh_from_db()

        subject_visit = self.get_subject_visit(
            subject_screening=self.subject_screening,
            subject_consent=self.subject_consent,
            visit_code=subject_visit.appointment.next.visit_code,
        )
        crfs = CrfMetadata.objects.filter(
            subject_identifier=subject_visit.subject_identifier,
            visit_code=subject_visit.visit_code,
            visit_code_sequence=subject_visit.visit_code_sequence,
            entry_status=REQUIRED,
        )
        self.assertNotIn("inte_subject.familyhistory", [o.model for o in crfs.all()])
