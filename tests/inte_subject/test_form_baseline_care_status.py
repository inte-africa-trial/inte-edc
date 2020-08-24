from pprint import pprint

from django.test import TestCase, tag
from edc_constants.constants import INCOMPLETE, NEG, NEVER, NOT_APPLICABLE, NO, POS, YES
from edc_utils import get_utcnow
from inte_screening.constants import (
    DIABETES_CLINIC,
    HIV_CLINIC,
    HYPERTENSION_CLINIC,
    NCD_CLINIC,
)
from inte_subject.forms import ClinicalReviewBaselineForm
from pytz import timezone

from ..inte_test_case_mixin import InteTestCaseMixin


def get_now():
    return get_utcnow().astimezone(timezone("Africa/Kampala"))


class TestBaselineClinicalReview(InteTestCaseMixin, TestCase):
    def setUp(self):
        super().setUp()
        # hiv clinic
        self.subject_screening_hiv = self.get_subject_screening(
            report_datetime=get_utcnow(), clinic_type=HIV_CLINIC
        )
        self.subject_consent_hiv = self.get_subject_consent(
            subject_screening=self.subject_screening_hiv, clinic_type=HIV_CLINIC
        )
        self.subject_visit_hiv = self.get_subject_visit(
            subject_screening=self.subject_screening_hiv,
            subject_consent=self.subject_consent_hiv,
        )

        # hypertension clinic
        self.subject_screening_hypertension = self.get_subject_screening(
            report_datetime=get_utcnow(), clinic_type=HYPERTENSION_CLINIC
        )
        self.subject_consent_hypertension = self.get_subject_consent(
            subject_screening=self.subject_screening_hypertension,
            clinic_type=HYPERTENSION_CLINIC,
        )
        self.subject_visit_hypertension = self.get_subject_visit(
            subject_screening=self.subject_screening_hypertension,
            subject_consent=self.subject_consent_hypertension,
        )

        # diabetes clinic
        self.subject_screening_diabetes = self.get_subject_screening(
            report_datetime=get_utcnow(), clinic_type=DIABETES_CLINIC
        )
        self.subject_consent_diabetes = self.get_subject_consent(
            subject_screening=self.subject_screening_diabetes,
            clinic_type=DIABETES_CLINIC,
        )
        self.subject_visit_diabetes = self.get_subject_visit(
            subject_screening=self.subject_screening_diabetes,
            subject_consent=self.subject_consent_diabetes,
        )

        # NCD clinic
        self.subject_screening_ncd = self.get_subject_screening(
            report_datetime=get_utcnow(), clinic_type=NCD_CLINIC
        )
        self.subject_consent_ncd = self.get_subject_consent(
            subject_screening=self.subject_screening_ncd, clinic_type=NCD_CLINIC,
        )
        self.subject_visit_ncd = self.get_subject_visit(
            subject_screening=self.subject_screening_ncd,
            subject_consent=self.subject_consent_ncd,
        )

    @tag("cr")
    def test_form_ok_hiv(self):
        data = {
            "subject_visit": self.subject_visit_hiv.pk,
            "report_datetime": self.subject_visit_hiv.report_datetime,
            "crf_status": INCOMPLETE,
            "hiv": POS,
            "hiv_tested_ago": "5y",
            "hypertension_tested": NO,
            "hypertension_dx": NOT_APPLICABLE,
            "diabetes_tested": NO,
            "diabetes_tested_ago": None,
            "diabetes_dx": NOT_APPLICABLE,
            "health_insurance": YES,
            "patient_club": YES,
        }
        form = ClinicalReviewBaselineForm(data=data)
        form.is_valid()
        self.assertEqual(form._errors, {})

    @tag("cr")
    def test_form_ok_hypertensive(self):
        data = {
            "subject_visit": self.subject_visit_hypertension.pk,
            "report_datetime": self.subject_visit_hypertension.report_datetime,
            "crf_status": INCOMPLETE,
            "hiv": NEVER,
            "hiv_tested_ago": None,
            "hypertension_tested": YES,
            "hypertension_tested_ago": "1y1m",
            "hypertension_dx": YES,
            "diabetes_tested": NO,
            "diabetes_tested_ago": None,
            "diabetes_dx": NOT_APPLICABLE,
            "health_insurance": YES,
            "patient_club": YES,
        }
        form = ClinicalReviewBaselineForm(data=data)
        form.is_valid()
        pprint(form._errors)
        self.assertEqual(form._errors, {})

    @tag("cr")
    def test_form_ok_diabetes(self):
        data = {
            "subject_visit": self.subject_visit_diabetes.pk,
            "report_datetime": self.subject_visit_diabetes.report_datetime,
            "crf_status": INCOMPLETE,
            "hiv": NEVER,
            "hiv_tested_ago": None,
            "hypertension_tested": NO,
            "hypertension_tested_ago": None,
            "hypertension_dx": NOT_APPLICABLE,
            "diabetes_tested": YES,
            "diabetes_tested_ago": "1y1m",
            "diabetes_dx": YES,
            "health_insurance": YES,
            "patient_club": YES,
        }
        form = ClinicalReviewBaselineForm(data=data)
        form.is_valid()
        self.assertEqual(form._errors, {})

    @tag("cr")
    def test_hiv_if_hiv_clinic(self):
        data = {
            "subject_visit": self.subject_visit_hiv.pk,
            "report_datetime": self.subject_visit_hiv.report_datetime,
            "crf_status": INCOMPLETE,
        }
        data.update(
            hiv=NEG, hiv_tested_ago=None,
        )
        form = ClinicalReviewBaselineForm(data=data)
        form.is_valid()
        self.assertIn("hiv", form._errors)

        data.update(
            hiv=NEVER, hiv_tested_ago=None,
        )
        form = ClinicalReviewBaselineForm(data=data)
        form.is_valid()
        self.assertIn("hiv", form._errors)

        data.update(
            hiv=POS, hiv_tested_ago=None,
        )
        form = ClinicalReviewBaselineForm(data=data)
        form.is_valid()
        self.assertNotIn("hiv", form._errors)
        self.assertIn("hiv_tested_ago", form._errors)

        data.update(
            hiv=POS, hiv_tested_ago="10y",
        )
        form = ClinicalReviewBaselineForm(data=data)
        form.is_valid()
        self.assertNotIn("hiv", form._errors)
        self.assertNotIn("hiv_tested_ago", form._errors)

    @tag("cr")
    def test_hypertension_if_hypertension_clinic(self):
        data = {
            "subject_visit": self.subject_visit_hypertension.pk,
            "report_datetime": self.subject_visit_hypertension.report_datetime,
            "crf_status": INCOMPLETE,
            "hiv": NEVER,
            "hiv_tested_ago": None,
            "hypertension_tested": NO,
            "hypertension_dx": NOT_APPLICABLE,
        }
        form = ClinicalReviewBaselineForm(data=data)
        form.is_valid()
        self.assertIn("hypertension_tested", form._errors)

        data.update(
            hypertension_tested=YES, hypertension_dx=NOT_APPLICABLE,
        )
        form = ClinicalReviewBaselineForm(data=data)
        form.is_valid()
        self.assertNotIn("hypertension_tested", form._errors)
        self.assertIn("hypertension_dx", form._errors)

        data.update(
            hypertension_tested=YES, hypertension_dx=YES,
        )
        form = ClinicalReviewBaselineForm(data=data)
        form.is_valid()
        self.assertNotIn("hypertension_tested", form._errors)
        self.assertNotIn("hypertension_dx", form._errors)

    @tag("cr")
    def test_diabetes_if_ncd_clinic(self):
        for cond in ["diabetes", "hypertension"]:
            data = {
                "subject_visit": self.subject_visit_ncd.pk,
                "report_datetime": self.subject_visit_ncd.report_datetime,
                "crf_status": INCOMPLETE,
                "hiv": NEVER,
                "hiv_tested_ago": None,
                "diabetes_tested": NO,
                "diabetes_dx": NOT_APPLICABLE,
                "hypertension_tested": NO,
                "hypertension_dx": NOT_APPLICABLE,
            }
            with self.subTest(cond=cond):
                form = ClinicalReviewBaselineForm(data=data)
                form.is_valid()
                # expects a test
                self.assertIn("__all__", [k for k in form._errors.keys()])

                data.update({f"{cond}_tested": YES, f"{cond}_dx": NOT_APPLICABLE})
                form = ClinicalReviewBaselineForm(data=data)
                form.is_valid()
                # expects a diagnosis
                self.assertIn("__all__", [k for k in form._errors.keys()])

                data.update({f"{cond}_tested": YES, f"{cond}_dx": YES})
                form = ClinicalReviewBaselineForm(data=data)
                form.is_valid()
                self.assertNotIn("__all__", [k for k in form._errors.keys()])
                self.assertNotIn(f"{cond}_tested", form._errors)
                self.assertNotIn(cond, form._errors)
