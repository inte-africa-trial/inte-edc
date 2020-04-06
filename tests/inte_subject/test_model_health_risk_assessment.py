from django.test import TestCase, tag  # noqa
from edc_constants.constants import SMOKER, NONSMOKER, NOT_APPLICABLE, NO
from inte_subject.forms import HealthRiskAssessmentForm

from ..inte_test_case_mixin import InteTestCaseMixin


class TestHealthRiskAssessment(InteTestCaseMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.data = {
            "smoking_status": SMOKER,
            "smoker_quit_ago_str": "1y2m",
            "alcohol": NO,
            "alcohol_consumption": NOT_APPLICABLE,
        }

        self.subject_visit = self.get_subject_visit()

        self.data.update(
            subject_visit=self.subject_visit.pk,
            report_datetime=self.subject_visit.report_datetime,
        )

    def test_ok(self):
        form = HealthRiskAssessmentForm(data=self.data)
        form.is_valid()
        self.assertEqual(form._errors, {})

    def test_health_risk_assessment_non_smoker(self):
        self.data.update({"smoking_status": NONSMOKER, "smoker_quit_ago_str": None})
        form = HealthRiskAssessmentForm(data=self.data)
        form.is_valid()
        self.assertEqual(form._errors, {})
