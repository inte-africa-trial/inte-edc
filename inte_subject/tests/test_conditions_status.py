from pprint import pprint

from django.test import TestCase, tag
from edc_constants.constants import YES, NO, NOT_APPLICABLE
from inte_screening.tests.inte_test_case_mixin import InteTestCaseMixin

from ..forms import GeneralAssessmentInitialForm


class TestConditionStatus(InteTestCaseMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.subject_visit = self.get_subject_visit()
        self.data = {
            "hiv": YES,
            "attending_hiv_clinic": YES,
            "use_hiv_clinic_nearby": YES,
            "diabetic": YES,
            "hypertensive": YES,
            "attending_ncd_clinic": YES,
            "use_ncd_clinic_nearby": YES,
            "hiv_next_appt_date": self.subject_visit.report_datetime.date(),
            "ncd_next_appt_date": self.subject_visit.report_datetime.date(),
        }

        self.data.update(
            subject_visit=self.subject_visit.pk,
            report_datetime=self.subject_visit.report_datetime,
        )

    def test_ok(self):
        form = GeneralAssessmentInitialForm(data=self.data)
        form.is_valid()
        self.assertEqual(form._errors, {})

    def test_hiv_only(self):
        self.data.update(
            {
                "hiv": YES,
                "attending_hiv_clinic": YES,
                "use_hiv_clinic_nearby": YES,
                "diabetic": NO,
                "hypertensive": NO,
                "attending_ncd_clinic": NOT_APPLICABLE,
                "use_ncd_clinic_nearby": NOT_APPLICABLE,
                "hiv_next_appt_date": self.subject_visit.report_datetime.date(),
                "ncd_next_appt_date": None,
            }
        )
        form = GeneralAssessmentInitialForm(data=self.data)
        form.is_valid()
        self.assertEqual(form._errors, {})

    def test_ncd_only(self):
        self.data.update(
            {
                "hiv": NO,
                "attending_hiv_clinic": NOT_APPLICABLE,
                "use_hiv_clinic_nearby": NOT_APPLICABLE,
                "diabetic": YES,
                "hypertensive": YES,
                "attending_ncd_clinic": YES,
                "use_ncd_clinic_nearby": YES,
                "ncd_next_appt_date": self.subject_visit.report_datetime.date(),
                "hiv_next_appt_date": None,
            }
        )
        form = GeneralAssessmentInitialForm(data=self.data)
        form.is_valid()
        self.assertEqual(form._errors, {})

    def test_ncd_diabetes_only(self):
        self.data.update(
            {
                "hiv": NO,
                "attending_hiv_clinic": NOT_APPLICABLE,
                "use_hiv_clinic_nearby": NOT_APPLICABLE,
                "diabetic": YES,
                "hypertensive": NO,
                "attending_ncd_clinic": YES,
                "use_ncd_clinic_nearby": YES,
                "hiv_next_appt_date": None,
                "ncd_next_appt_date": self.subject_visit.report_datetime.date(),
            }
        )
        form = GeneralAssessmentInitialForm(data=self.data)
        form.is_valid()
        self.assertEqual(form._errors, {})

    def test_ncd_hypertensive_only(self):
        self.data.update(
            {
                "hiv": NO,
                "attending_hiv_clinic": NOT_APPLICABLE,
                "use_hiv_clinic_nearby": NOT_APPLICABLE,
                "diabetic": NO,
                "hypertensive": YES,
                "attending_ncd_clinic": YES,
                "use_ncd_clinic_nearby": YES,
                "ncd_next_appt_date": self.subject_visit.report_datetime.date(),
                "hiv_next_appt_date": None,
            }
        )
        form = GeneralAssessmentInitialForm(data=self.data)
        form.is_valid()
        self.assertEqual(form._errors, {})
