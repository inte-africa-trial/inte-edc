import copy

from dateutil.relativedelta import relativedelta
from django.test import TestCase, tag
from edc_constants.constants import INCOMPLETE, NO, NOT_APPLICABLE, YES
from edc_utils import get_utcnow
from pytz import timezone

from inte_screening.constants import (
    DIABETES_CLINIC,
    HIV_CLINIC,
    HYPERTENSION_CLINIC,
    NCD_CLINIC,
)
from inte_subject.forms import ClinicalReviewBaselineForm

from ..inte_test_case_mixin import InteTestCaseMixin


def get_now():
    return get_utcnow().astimezone(timezone("Africa/Kampala"))


@tag("crb")
class TestClinicalReviewBaseline(InteTestCaseMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.baseline_datetime = get_utcnow() - relativedelta(months=1)
        # hiv clinic
        self.subject_screening_hiv = self.get_subject_screening(
            report_datetime=self.baseline_datetime, clinic_type=HIV_CLINIC
        )
        self.subject_consent_hiv = self.get_subject_consent(
            subject_screening=self.subject_screening_hiv,
            clinic_type=HIV_CLINIC,
            consent_datetime=self.baseline_datetime,
        )
        self.subject_visit_hiv = self.get_subject_visit(
            subject_screening=self.subject_screening_hiv,
            subject_consent=self.subject_consent_hiv,
            report_datetime=self.baseline_datetime,
        )

        # htn clinic
        self.subject_screening_htn = self.get_subject_screening(
            report_datetime=self.baseline_datetime,
            clinic_type=HYPERTENSION_CLINIC,
        )
        self.subject_consent_htn = self.get_subject_consent(
            subject_screening=self.subject_screening_htn,
            clinic_type=HYPERTENSION_CLINIC,
            report_datetime=self.baseline_datetime,
        )
        self.subject_visit_htn = self.get_subject_visit(
            subject_screening=self.subject_screening_htn,
            subject_consent=self.subject_consent_htn,
            report_datetime=self.baseline_datetime,
        )

        # diabetes clinic
        self.subject_screening_dm = self.get_subject_screening(
            report_datetime=self.baseline_datetime, clinic_type=DIABETES_CLINIC
        )
        self.subject_consent_dm = self.get_subject_consent(
            subject_screening=self.subject_screening_dm,
            clinic_type=DIABETES_CLINIC,
            report_datetime=self.baseline_datetime,
        )
        self.subject_visit_dm = self.get_subject_visit(
            subject_screening=self.subject_screening_dm,
            subject_consent=self.subject_consent_dm,
            report_datetime=self.baseline_datetime,
        )

        # NCD clinic
        self.subject_screening_ncd = self.get_subject_screening(
            report_datetime=self.baseline_datetime, clinic_type=NCD_CLINIC
        )
        self.subject_consent_ncd = self.get_subject_consent(
            subject_screening=self.subject_screening_ncd,
            clinic_type=NCD_CLINIC,
            report_datetime=self.baseline_datetime,
        )
        self.subject_visit_ncd = self.get_subject_visit(
            subject_screening=self.subject_screening_ncd,
            subject_consent=self.subject_consent_ncd,
            report_datetime=self.baseline_datetime,
        )

    @staticmethod
    def get_valid_form_data(subject_visit):
        return {
            "subject_visit": subject_visit.pk,
            "report_datetime": subject_visit.report_datetime,
            "crf_status": INCOMPLETE,
            "hiv_test": YES,
            "hiv_test_ago": "1y",
            "hiv_dx": YES,
            "dm_test": YES,
            "dm_test_ago": "1y",
            "dm_dx": YES,
            "htn_test": YES,
            "htn_test_ago": "1y",
            "htn_dx": YES,
            "health_insurance": YES,
            "patient_club": YES,
        }

    def test_form_ok_hiv(self):
        data = {
            "subject_visit": self.subject_visit_hiv.pk,
            "report_datetime": self.subject_visit_hiv.report_datetime,
            "crf_status": INCOMPLETE,
            "hiv_test": YES,
            "hiv_test_ago": "5y",
            "hiv_dx": YES,
            "htn_test": NO,
            "htn_dx": NOT_APPLICABLE,
            "dm_test": NO,
            "dm_test_ago": None,
            "dm_dx": NOT_APPLICABLE,
            "health_insurance": YES,
            "patient_club": YES,
        }
        form = ClinicalReviewBaselineForm(data=data)
        form.is_valid()
        self.assertEqual(form._errors, {})

    def test_form_ok_hypertensive(self):
        data = {
            "subject_visit": self.subject_visit_htn.pk,
            "report_datetime": self.subject_visit_htn.report_datetime,
            "crf_status": INCOMPLETE,
            "hiv_test": NO,
            "hiv_test_ago": None,
            "hiv_dx": NOT_APPLICABLE,
            "htn_test": YES,
            "htn_test_ago": "1y1m",
            "htn_dx": YES,
            "dm_test": NO,
            "dm_test_ago": None,
            "dm_dx": NOT_APPLICABLE,
            "health_insurance": YES,
            "patient_club": YES,
        }
        form = ClinicalReviewBaselineForm(data=data)
        form.is_valid()
        self.assertEqual(form._errors, {})

    def test_form_ok_dm(self):
        data = {
            "subject_visit": self.subject_visit_dm.pk,
            "report_datetime": self.subject_visit_dm.report_datetime,
            "crf_status": INCOMPLETE,
            "hiv_test": NO,
            "hiv_test_ago": None,
            "hiv_dx": NOT_APPLICABLE,
            "htn_test": NO,
            "htn_test_ago": None,
            "htn_dx": NOT_APPLICABLE,
            "dm_test": YES,
            "dm_test_ago": "1y1m",
            "dm_dx": YES,
            "health_insurance": YES,
            "patient_club": YES,
        }
        form = ClinicalReviewBaselineForm(data=data)
        form.is_valid()
        self.assertEqual(form._errors, {})

    def test_hiv_if_hiv_clinic(self):
        data = {
            "subject_visit": self.subject_visit_hiv.pk,
            "report_datetime": self.subject_visit_hiv.report_datetime,
            "crf_status": INCOMPLETE,
        }
        data.update(
            hiv_test=NO,
            hiv_test_ago=None,
            hiv_test_date=None,
            hiv_dx=NOT_APPLICABLE,
        )
        form = ClinicalReviewBaselineForm(data=data)
        form.is_valid()
        self.assertIn("hiv_test", form._errors)

        data.update(
            hiv_test=YES,
            hiv_test_ago=None,
            hiv_test_date=None,
            hiv_dx=NOT_APPLICABLE,
            dm_test=NO,
            htn_test=NO,
        )
        form = ClinicalReviewBaselineForm(data=data)
        form.is_valid()
        self.assertNotIn("hiv_test", form._errors)
        self.assertIn("__all__", form._errors)

        data.update(
            hiv_test=YES,
            hiv_test_ago=None,
            hiv_test_date=None,
            hiv_dx=YES,
            dm_test=NO,
            htn_test=NO,
        )
        form = ClinicalReviewBaselineForm(data=data)
        form.is_valid()
        self.assertNotIn("hiv_test", form._errors)
        self.assertIn("__all__", form._errors)

        data.update(
            hiv_test=YES,
            hiv_test_ago=None,
            hiv_test_date=get_utcnow(),
            hiv_dx=YES,
        )
        form = ClinicalReviewBaselineForm(data=data)
        form.is_valid()
        self.assertNotIn("hiv_test", form._errors)
        self.assertNotIn("hiv_dx", form._errors)
        self.assertNotIn("__all__", form._errors)

        data.update(
            hiv_test=YES,
            hiv_test_ago=None,
            hiv_test_date=get_utcnow(),
            hiv_dx=NOT_APPLICABLE,
        )
        form = ClinicalReviewBaselineForm(data=data)
        form.is_valid()
        self.assertNotIn("hiv_test", form._errors)
        self.assertIn("hiv_dx", form._errors)

        data.update(hiv_test=YES, hiv_test_ago="10y", hiv_test_date=None, hiv_dx=YES)
        form = ClinicalReviewBaselineForm(data=data)
        form.is_valid()
        self.assertNotIn("hiv_test", form._errors)
        self.assertNotIn("hiv_dx", form._errors)
        self.assertNotIn("__all__", form._errors)

    def test_htn_if_htn_clinic(self):
        data = {
            "subject_visit": self.subject_visit_htn.pk,
            "report_datetime": self.subject_visit_htn.report_datetime,
            "crf_status": INCOMPLETE,
            "hiv_test": NO,
            "hiv_test_ago": None,
            "hiv_dx": NOT_APPLICABLE,
            "htn_test": NO,
            "htn_test_ago": "1y",
            "htn_dx": NOT_APPLICABLE,
        }
        form = ClinicalReviewBaselineForm(data=data)
        form.is_valid()
        self.assertIn("htn_test", form._errors)

        data.update(
            htn_test=YES,
            htn_dx=NOT_APPLICABLE,
        )
        form = ClinicalReviewBaselineForm(data=data)
        form.is_valid()
        self.assertNotIn("htn_test", form._errors)
        self.assertIn("htn_dx", form._errors)

        data.update(
            htn_test=YES,
            htn_dx=YES,
        )
        form = ClinicalReviewBaselineForm(data=data)
        form.is_valid()
        self.assertNotIn("htn_test", form._errors)
        self.assertNotIn("htn_dx", form._errors)

    def test_dm_if_ncd_clinic(self):
        for cond in ["dm", "htn"]:
            data = {
                "subject_visit": self.subject_visit_ncd.pk,
                "report_datetime": self.subject_visit_ncd.report_datetime,
                "crf_status": INCOMPLETE,
                "hiv_test": NO,
                "hiv_test_ago": None,
                "hiv_dx": NOT_APPLICABLE,
                "dm_test": NO,
                "dm_dx": NOT_APPLICABLE,
                "htn_test": NO,
                "htn_dx": NOT_APPLICABLE,
            }
            with self.subTest(cond=cond):
                form = ClinicalReviewBaselineForm(data=data)
                form.is_valid()
                # expects a test
                self.assertIn("__all__", [k for k in form._errors.keys()])

                data.update(
                    {
                        f"{cond}_test": YES,
                        f"{cond}_test_ago": "1y",
                        f"{cond}_dx": NOT_APPLICABLE,
                    }
                )
                form = ClinicalReviewBaselineForm(data=data)
                form.is_valid()
                # expects a diagnosis
                self.assertIn("__all__", [k for k in form._errors.keys()])

                data.update({f"{cond}_test": YES, f"{cond}_test_ago": "1y", f"{cond}_dx": YES})
                form = ClinicalReviewBaselineForm(data=data)
                form.is_valid()
                self.assertNotIn("__all__", [k for k in form._errors.keys()])
                self.assertNotIn(f"{cond}_test", form._errors)
                self.assertNotIn(cond, form._errors)

    def test_get_valid_form_data_test_helper(self):
        for subject_visit_type in [
            self.subject_visit_hiv,
            self.subject_visit_dm,
            self.subject_visit_htn,
        ]:
            with self.subTest(subject_visit_type=subject_visit_type):
                valid_data = self.get_valid_form_data(subject_visit=subject_visit_type)

                form = ClinicalReviewBaselineForm(data=valid_data)
                form.is_valid()
                self.assertEqual(form._errors, {})

    def test_date_or_est_required_if_cond_tested(self):
        valid_data = self.get_valid_form_data(subject_visit=self.subject_visit_htn)

        # Test as tested, diagnosed, but without any <cond>_test_ago field data
        for cond in ["hiv", "dm", "htn"]:
            with self.subTest(codn=cond):
                subtest_data = copy.deepcopy(valid_data)
                subtest_data.update({f"{cond}_test_ago": None})

                form = ClinicalReviewBaselineForm(data=subtest_data)
                form.is_valid()

                self.assertIn("__all__", form._errors)
                self.assertIn(
                    f"{cond.title()}: When was the subject tested? Either ",
                    str(form._errors.get("__all__")),
                )

    def test_related_test_required_for_vertical_screening_clinics(self):
        for cond, cond_desc, subject_visit in [
            ("hiv", "an HIV", self.subject_visit_hiv),
            ("dm", "a Diabetes", self.subject_visit_dm),
            ("htn", "an Hypertension", self.subject_visit_htn),
        ]:
            with self.subTest(cond=cond):
                subtest_data = self.get_valid_form_data(subject_visit)
                subtest_data.update(
                    {
                        f"{cond}_test": NO,
                        f"{cond}_dx": NOT_APPLICABLE,
                    }
                )

                form = ClinicalReviewBaselineForm(data=subtest_data)
                form.is_valid()

                self.assertIn(f"{cond}_test", form._errors)
                self.assertIn(
                    f"Patient was screened from {cond_desc} clinic, expected `Yes`.",
                    str(form._errors.get(f"{cond}_test")),
                )
                self.assertEqual(len(form._errors), 1, form._errors)

    @tag("crb2")
    def test_positive_cond_dx_not_required_just_because_came_from_cond_clinic(self):
        for cond, subject_visit in [
            ("hiv", self.subject_visit_hiv),
            ("dm", self.subject_visit_dm),
            ("htn", self.subject_visit_htn),
        ]:
            with self.subTest(cond=cond, subject_visit=subject_visit):
                subtest_data = self.get_valid_form_data(subject_visit=subject_visit)
                subtest_data.update({f"{cond}_dx": NO})

                form = ClinicalReviewBaselineForm(data=subtest_data)
                form.is_valid()

                self.assertEqual(form._errors, {})
