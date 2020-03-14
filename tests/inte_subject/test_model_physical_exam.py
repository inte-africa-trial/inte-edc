from django.test import TestCase, tag
from edc_constants.constants import YES
from inte_subject.constants import SITTING, GTE_3HRS
from inte_subject.forms import PhysicalActivityForm

from ..inte_test_case_mixin import InteTestCaseMixin


class TestPhysicalActivity(InteTestCaseMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.data = {
            "subject_visit": None,
            "report_datetime": None,
            "physical_activity": SITTING,
            "physical_exercise": GTE_3HRS,
            "cycling": GTE_3HRS,
            "walking": GTE_3HRS,
            "housework": GTE_3HRS,
            "casual_labour": GTE_3HRS,
            "physically_active": YES,
        }

        self.subject_visit = self.get_subject_visit()

        self.data.update(
            subject_visit=self.subject_visit.pk,
            report_datetime=self.subject_visit.report_datetime,
        )

    def test_ok(self):
        form = PhysicalActivityForm(data=self.data)
        form.is_valid()
        self.assertEqual(form._errors, {})
