from django.test import TestCase, tag
from edc_constants.constants import SMOKER, NONSMOKER, NOT_APPLICABLE, NO
from inte_subject.forms import RiskFactorsForm

from ..inte_test_case_mixin import InteTestCaseMixin


class TestRiskFactors(InteTestCaseMixin, TestCase):
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
        form = RiskFactorsForm(data=self.data)
        form.is_valid()
        self.assertEqual(form._errors, {})

    def test_risk_factors_non_smoker(self):
        self.data.update({"smoking_status": NONSMOKER, "smoker_quit_ago_str": None})
        form = RiskFactorsForm(data=self.data)
        form.is_valid()
        self.assertEqual(form._errors, {})
