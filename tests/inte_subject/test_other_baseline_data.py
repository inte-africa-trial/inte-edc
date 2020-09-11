from django.test import TestCase, tag  # noqa
from edc_constants.constants import COMPLETE, SMOKER, NONSMOKER, NOT_APPLICABLE, NO
from inte_subject.forms import OtherBaselineDataForm
from model_bakery import baker

from ..inte_test_case_mixin import InteTestCaseMixin


class TestOtherBaselineData(InteTestCaseMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.data = {
            "crf_status": COMPLETE,
            "smoking_status": SMOKER,
            "smoker_quit_ago_str": "1y2m",
            "alcohol": NO,
            "alcohol_consumption": NOT_APPLICABLE,
            "employment_status": "professional",
            "education": "primary",
            "marital_status": "married",
        }

        self.subject_visit = self.get_subject_visit()

        baker.make(
            "inte_subject.clinicalreviewbaseline", subject_visit=self.subject_visit
        )

        self.data.update(
            subject_visit=self.subject_visit.pk,
            report_datetime=self.subject_visit.report_datetime,
        )

    @tag("other_baseline")
    def test_ok(self):
        form = OtherBaselineDataForm(data=self.data)
        form.is_valid()
        self.assertEqual(form._errors, {})

    @tag("other_baseline")
    def test_non_smoker(self):
        self.data.update({"smoking_status": NONSMOKER, "smoker_quit_ago_str": None})
        form = OtherBaselineDataForm(data=self.data)
        form.is_valid()
        self.assertEqual(form._errors, {})
