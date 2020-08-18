from django.test import TestCase, tag
from edc_constants.constants import INCOMPLETE, NEG, NEVER, NOT_APPLICABLE, NO, POS, YES
from edc_utils import get_utcnow
from inte_screening.constants import (
    DIABETES_CLINIC,
    HIV_CLINIC,
    HYPERTENSION_CLINIC,
    NCD_CLINIC,
)
from inte_subject.forms import CareStatusBaselineForm
from pytz import timezone

from ..inte_test_case_mixin import InteTestCaseMixin


def get_now():
    return get_utcnow().astimezone(timezone("Africa/Kampala"))


class TestBaselineCareStatus(InteTestCaseMixin, TestCase):
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

    @tag("care")
    def test_form_ok_hiv(self):
        """Assert default data above validates."""
        data = {
            "subject_visit": self.subject_visit_hiv.pk,
            "report_datetime": self.subject_visit_hiv.report_datetime,
            "crf_status": INCOMPLETE,
            "hiv_result": POS,
            "hiv_result_ago": "5y",
            "hypertensive_tested": NO,
            "hypertensive": NOT_APPLICABLE,
            "diabetic_tested": NO,
            "diabetic_tested_ago": None,
            "diabetic": NOT_APPLICABLE,
            "health_insurance": YES,
            "patient_club": YES,
        }
        form = CareStatusBaselineForm(data=data)
        form.is_valid()
        self.assertEqual(form._errors, {})

    @tag("care")
    def test_hiv_if_hiv_clinic(self):
        data = {
            "subject_visit": self.subject_visit_hiv.pk,
            "report_datetime": self.subject_visit_hiv.report_datetime,
            "crf_status": INCOMPLETE,
        }
        data.update(
            hiv_result=NEG, hiv_result_ago=None,
        )
        form = CareStatusBaselineForm(data=data)
        form.is_valid()
        self.assertIn("hiv_result", form._errors)

        data.update(
            hiv_result=NEVER, hiv_result_ago=None,
        )
        form = CareStatusBaselineForm(data=data)
        form.is_valid()
        self.assertIn("hiv_result", form._errors)

        data.update(
            hiv_result=POS, hiv_result_ago=None,
        )
        form = CareStatusBaselineForm(data=data)
        form.is_valid()
        self.assertNotIn("hiv_result", form._errors)
        self.assertIn("hiv_result_ago", form._errors)

        data.update(
            hiv_result=POS, hiv_result_ago="10y",
        )
        form = CareStatusBaselineForm(data=data)
        form.is_valid()
        self.assertNotIn("hiv_result", form._errors)
        self.assertNotIn("hiv_result_ago", form._errors)

    @tag("care")
    def test_hypertension_if_hypertension_clinic(self):
        data = {
            "subject_visit": self.subject_visit_hypertension.pk,
            "report_datetime": self.subject_visit_hypertension.report_datetime,
            "crf_status": INCOMPLETE,
            "hiv_result": NEVER,
            "hiv_result_ago": None,
            "hypertensive_tested": NO,
            "hypertensive": NOT_APPLICABLE,
        }
        form = CareStatusBaselineForm(data=data)
        form.is_valid()
        self.assertIn("hypertensive_tested", form._errors)

        data.update(
            hypertensive_tested=YES, hypertensive=NOT_APPLICABLE,
        )
        form = CareStatusBaselineForm(data=data)
        form.is_valid()
        self.assertNotIn("hypertensive_tested", form._errors)
        self.assertIn("hypertensive", form._errors)

        data.update(
            hypertensive_tested=YES, hypertensive=YES,
        )
        form = CareStatusBaselineForm(data=data)
        form.is_valid()
        self.assertNotIn("hypertensive_tested", form._errors)
        self.assertNotIn("hypertensive", form._errors)

    @tag("care")
    def test_diabetes_if_ncd_clinic(self):
        for cond in ["diabetic", "hypertensive"]:
            data = {
                "subject_visit": self.subject_visit_ncd.pk,
                "report_datetime": self.subject_visit_ncd.report_datetime,
                "crf_status": INCOMPLETE,
                "hiv_result": NEVER,
                "hiv_result_ago": None,
                "diabetic_tested": NO,
                "diabetic": NOT_APPLICABLE,
                "hypertensive_tested": NO,
                "hypertensive": NOT_APPLICABLE,
            }
            with self.subTest(cond=cond):
                form = CareStatusBaselineForm(data=data)
                form.is_valid()
                # expects a test
                self.assertIn("__all__", [k for k in form._errors.keys()])

                data.update({f"{cond}_tested": YES, cond: NOT_APPLICABLE})
                form = CareStatusBaselineForm(data=data)
                form.is_valid()
                # expects a diagnosis
                self.assertIn("__all__", [k for k in form._errors.keys()])

                data.update({f"{cond}_tested": YES, cond: YES})
                form = CareStatusBaselineForm(data=data)
                form.is_valid()
                self.assertNotIn("__all__", [k for k in form._errors.keys()])
                self.assertNotIn(f"{cond}_tested", form._errors)
                self.assertNotIn(cond, form._errors)
