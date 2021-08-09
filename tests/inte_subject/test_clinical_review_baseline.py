import copy
import html

from dateutil.relativedelta import relativedelta
from django.test import TestCase
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
                self.assertIn(
                    (
                        "Patient was screened from an NCD clinic, expected to "
                        "have tested for either Hypertension and/or Diabetes."
                    ),
                    str(form._errors.get("__all__")),
                )

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
                self.assertIn(
                    (
                        "Patient was screened from an NCD clinic, expected "
                        "'Yes' or 'No' diagnosis for Hypertension and/or Diabetes."
                    ),
                    html.unescape(str(form._errors.get("__all__"))),
                )

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
            self.subject_visit_ncd,
        ]:
            with self.subTest(subject_visit_type=subject_visit_type):
                valid_data = self.get_valid_form_data(subject_visit=subject_visit_type)

                form = ClinicalReviewBaselineForm(data=valid_data)
                form.is_valid()
                self.assertEqual(form._errors, {})

    def test_date_or_est_required_if_cond_tested(self):
        valid_data = self.get_valid_form_data(subject_visit=self.subject_visit_htn)

        for cond in ["hiv", "dm", "htn"]:
            with self.subTest(codn=cond):
                subtest_data = copy.deepcopy(valid_data)

                # Test with neither date, nor estimate set
                subtest_data.update({f"{cond}_test_ago": None, f"{cond}_test_date": None})

                form = ClinicalReviewBaselineForm(data=subtest_data)
                form.is_valid()

                self.assertIn("__all__", form._errors)
                self.assertIn(
                    f"{cond.title()}: When was the subject tested? Either ",
                    str(form._errors.get("__all__")),
                )

                # Test is ok with estimate provided
                subtest_data.update({f"{cond}_test_ago": "1y", f"{cond}_test_date": None})
                form = ClinicalReviewBaselineForm(data=subtest_data)
                form.is_valid()
                self.assertEqual(form._errors, {})

                # Test is ok with date provided
                subtest_data.update(
                    {f"{cond}_test_ago": None, f"{cond}_test_date": get_utcnow()}
                )
                form = ClinicalReviewBaselineForm(data=subtest_data)
                form.is_valid()
                self.assertEqual(form._errors, {})

    def test_related_test_required_for_subjects_from_vertical_clinics(self):
        for cond, cond_desc, subject_visit in [
            ("hiv", "HIV", self.subject_visit_hiv),
            ("dm", "Diabetes", self.subject_visit_dm),
            ("htn", "Hypertension", self.subject_visit_htn),
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

    def test_cond_dx_response_required_when_subject_from_same_vertical_cond_clinic(
        self,
    ):
        for cond, cond_desc, subject_visit in [
            ("hiv", "HIV", self.subject_visit_hiv),
            ("dm", "Diabetes", self.subject_visit_dm),
            ("htn", "Hypertension", self.subject_visit_htn),
        ]:
            with self.subTest(cond=cond, cond_desc=cond_desc, subject_visit=subject_visit):
                subtest_data = self.get_valid_form_data(subject_visit=subject_visit)
                subtest_data.update({f"{cond}_dx": NOT_APPLICABLE})

                form = ClinicalReviewBaselineForm(data=subtest_data)
                form.is_valid()

                self.assertIn(f"{cond}_dx", form._errors)
                self.assertIn(
                    (
                        f"Patient was screened from {cond_desc} clinic, "
                        "expected 'Yes' or 'No' diagnosis."
                    ),
                    html.unescape(str(form._errors.get(f"{cond}_dx"))),
                )
                self.assertEqual(len(form._errors), 1, form._errors)

    def test_cond_dx_response_no_for_subject_from_same_vertical_cond_clinic_ok(
        self,
    ):
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

    def test_cond_dx_yes_response_yes_for_subject_from_same_vertical_cond_clinic_ok(
        self,
    ):
        for cond, subject_visit in [
            ("hiv", self.subject_visit_hiv),
            ("dm", self.subject_visit_dm),
            ("htn", self.subject_visit_htn),
        ]:
            with self.subTest(cond=cond, subject_visit=subject_visit):
                subtest_data = self.get_valid_form_data(subject_visit=subject_visit)
                subtest_data.update({f"{cond}_dx": YES})

                form = ClinicalReviewBaselineForm(data=subtest_data)
                form.is_valid()

                self.assertEqual(form._errors, {})

    def test_dm_or_htn_test_required_for_subjects_from_ncd_clinics(self):
        subtest_data = self.get_valid_form_data(self.subject_visit_ncd)

        # Test no dm or htn test
        subtest_data.update(
            {
                "dm_test": NO,
                "dm_dx": NOT_APPLICABLE,
                "htn_test": NO,
                "htn_dx": NOT_APPLICABLE,
            }
        )

        form = ClinicalReviewBaselineForm(data=subtest_data)
        form.is_valid()

        self.assertIn("__all__", form._errors)
        self.assertIn(
            (
                "Patient was screened from an NCD clinic, expected to "
                "have tested for either Hypertension and/or Diabetes."
            ),
            str(form._errors.get("__all__")),
        )
        self.assertEqual(len(form._errors), 1, form._errors)

        # Test dm test only
        subtest_data.update(
            {
                "dm_test": YES,
                "dm_dx": YES,
                "htn_test": NO,
                "htn_dx": NOT_APPLICABLE,
            }
        )
        form = ClinicalReviewBaselineForm(data=subtest_data)
        form.is_valid()
        self.assertEqual(form._errors, {})

        # Test htn test only
        subtest_data.update(
            {
                "dm_test": NO,
                "dm_dx": NOT_APPLICABLE,
                "htn_test": YES,
                "htn_dx": YES,
            }
        )
        form = ClinicalReviewBaselineForm(data=subtest_data)
        form.is_valid()
        self.assertEqual(form._errors, {})

        # Test both dm and htn tests
        subtest_data.update(
            {
                "dm_test": YES,
                "dm_dx": YES,
                "htn_test": YES,
                "htn_dx": NO,
            }
        )
        form = ClinicalReviewBaselineForm(data=subtest_data)
        form.is_valid()
        self.assertEqual(form._errors, {})

    def test_positive_dm_or_htn_dx_not_required_because_subject_from_ncd_clinic(self):
        subtest_data = self.get_valid_form_data(self.subject_visit_ncd)

        # Tested for dm and htn, no dx for either
        subtest_data.update(
            {
                "dm_test": YES,
                "dm_dx": NO,
                "htn_test": YES,
                "htn_dx": NO,
            }
        )
        form = ClinicalReviewBaselineForm(data=subtest_data)
        form.is_valid()
        self.assertEqual(form._errors, {})

        # Tested for dm only, no dx
        subtest_data.update(
            {
                "dm_test": YES,
                "dm_dx": NO,
                "htn_test": NO,
                "htn_dx": NOT_APPLICABLE,
            }
        )
        form = ClinicalReviewBaselineForm(data=subtest_data)
        form.is_valid()
        self.assertEqual(form._errors, {})

        # Tested for htn only, no dx
        subtest_data.update(
            {
                "dm_test": NO,
                "dm_dx": NOT_APPLICABLE,
                "htn_test": YES,
                "htn_dx": NO,
            }
        )
        form = ClinicalReviewBaselineForm(data=subtest_data)
        form.is_valid()
        self.assertEqual(form._errors, {})

    def test_at_least_one_condition_required(self):
        for cond, subject_visit in [
            ("hiv", self.subject_visit_hiv),
            ("dm", self.subject_visit_dm),
            ("htn", self.subject_visit_htn),
            ("dm", self.subject_visit_ncd),
            ("htn", self.subject_visit_ncd),
        ]:
            with self.subTest(cond=cond, subject_visit=subject_visit):
                subtest_data = self.get_valid_form_data(subject_visit=subject_visit)
                subtest_data.update({f"{cond}_dx": YES})

                # Set all conditions to not tested/na diagnosis
                subtest_data.update(
                    {
                        "hiv_test": NO,
                        "hiv_dx": NOT_APPLICABLE,
                        "dm_test": NO,
                        "dm_dx": NOT_APPLICABLE,
                        "htn_test": NO,
                        "htn_dx": NOT_APPLICABLE,
                    }
                )

                # Configure required test (based on clinic type), and negative diagnosis
                subtest_data.update(
                    {
                        f"{cond}_test": YES,
                        f"{cond}_dx": NO,
                    }
                )

                form = ClinicalReviewBaselineForm(data=subtest_data)
                form.is_valid()

                self.assertIn("__all__", form._errors)
                self.assertIn(
                    (
                        "Patient expected to have at least one of the following "
                        "conditions: a positive HIV test, a diagnosis for Hypertension "
                        "or a diagnosis for Diabetes"
                    ),
                    str(form._errors.get("__all__")),
                )
