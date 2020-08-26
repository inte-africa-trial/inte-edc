import pdb

from django import forms
from django.test import TestCase, tag
from edc_appointment.constants import INCOMPLETE_APPT
from edc_constants.constants import INCOMPLETE, POS
from edc_utils import get_utcnow
from edc_visit_tracking.constants import UNSCHEDULED
from inte_screening.constants import HIV_CLINIC
from inte_subject.forms.clinical_review_form import (
    ClinicalReviewForm,
    ClinicalReviewFormValidator,
)
from tests.inte_test_case_mixin import InteTestCaseMixin
from model_bakery import baker


class TestClinicalReview(InteTestCaseMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.subject_screening = self.get_subject_screening(
            report_datetime=get_utcnow(), clinic_type=HIV_CLINIC
        )
        self.subject_consent = self.get_subject_consent(
            subject_screening=self.subject_screening, clinic_type=HIV_CLINIC
        )

    @tag("clinical_review")
    def test_clinical_review_requires_cr(self):
        subject_visit = self.get_subject_visit(
            subject_screening=self.subject_screening,
            subject_consent=self.subject_consent,
        )
        subject_visit.appointment.appt_status = INCOMPLETE_APPT
        subject_visit.appointment.save()
        subject_visit.appointment.refresh_from_db()
        subject_visit.refresh_from_db()

        subject_visit = self.get_next_subject_visit(
            subject_visit=subject_visit, reason=UNSCHEDULED
        )

        data = {
            "subject_visit": subject_visit,
            "report_datetime": subject_visit.report_datetime,
            "crf_status": INCOMPLETE,
        }
        form = ClinicalReviewForm(data=data)
        form.is_valid()
        self.assertIn("__all__", form._errors)
