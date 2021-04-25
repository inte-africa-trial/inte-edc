from dateutil.relativedelta import relativedelta
from django.test import TestCase
from edc_constants.constants import COMPLETE, NO, NONSMOKER, NOT_APPLICABLE, SMOKER
from edc_utils import get_utcnow
from model_bakery import baker

from inte_screening.constants import HIV_CLINIC
from inte_subject.forms import OtherBaselineDataForm

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

        self.baseline_datetime = get_utcnow() - relativedelta(months=1)
        self.subject_screening = self.get_subject_screening(
            report_datetime=self.baseline_datetime, clinic_type=HIV_CLINIC
        )
        self.subject_consent = self.get_subject_consent(
            subject_screening=self.subject_screening,
            clinic_type=HIV_CLINIC,
            report_datetime=self.baseline_datetime,
        )

        self.subject_visit = self.get_subject_visit(
            subject_screening=self.subject_screening,
            subject_consent=self.subject_consent,
            report_datetime=self.baseline_datetime,
        )

        baker.make(
            "inte_subject.clinicalreviewbaseline",
            subject_visit=self.subject_visit,
            report_datetime=self.subject_visit.report_datetime,
        )

        self.data.update(
            subject_visit=self.subject_visit.pk,
            report_datetime=self.subject_visit.report_datetime,
        )

    def test_ok(self):
        form = OtherBaselineDataForm(data=self.data)
        form.is_valid()
        self.assertEqual(form._errors, {})

    def test_non_smoker(self):
        self.data.update({"smoking_status": NONSMOKER, "smoker_quit_ago_str": None})
        form = OtherBaselineDataForm(data=self.data)
        form.is_valid()
        self.assertEqual(form._errors, {})
