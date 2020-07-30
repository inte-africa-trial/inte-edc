from django.test import TestCase, tag
from edc_constants.constants import INCOMPLETE, YES
from inte_subject.constants import SITTING, GTE_3HRS
from inte_subject.forms import ReasonForVisitForm

from ..inte_test_case_mixin import InteTestCaseMixin


@tag("1")
class TestReasonForVisit(InteTestCaseMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.data = {
            "subject_visit": None,
            "report_datetime": None,
            "crf_status": INCOMPLETE,
            "site": None,
            "clinic_services_other": None,
            "refill_hiv": None,
            "refill_diabetes": None,
            "refill_hypertension": None,
        }

        self.subject_visit = self.get_subject_visit()

        self.data.update(
            subject_visit=self.subject_visit.pk,
            report_datetime=self.subject_visit.report_datetime,
        )

    def test_ok(self):
        form = ReasonForVisitForm(data=self.data)
        form.is_valid()
        self.assertEqual(form._errors, {})
