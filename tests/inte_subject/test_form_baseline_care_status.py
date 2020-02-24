from unittest import skip

from dateutil.relativedelta import relativedelta
from django.test import TestCase, tag
from edc_constants.constants import SMOKER, NONSMOKER, NOT_APPLICABLE, NO, YES
from edc_utils import get_utcnow
from inte_subject.forms import BaselineCareStatusForm

from ..inte_test_case_mixin import InteTestCaseMixin


@skip
class TestBaselineCareStatus(InteTestCaseMixin, TestCase):
    def setUp(self):
        super().setUp()
        subject_screening = self.get_subject_screening(report_datetime=get_utcnow())
        self.consent = self.get_subject_consent(subject_screening=subject_screening)

        # set up condition in HIV clinic, no co-morbidity
        self.data = {
            "hiv": YES,
            "attending_hiv_clinic": YES,
            "use_hiv_clinic_nearby": YES,
            "hiv_clinic_other": None,
            "hiv_next_appt_date": None,
            "diabetic": NO,
            "hypertensive": NO,
            "use_ncd_clinic_nearby": NOT_APPLICABLE,
            "attending_ncd_clinic": NOT_APPLICABLE,
            "ncd_clinic_other": None,
            "ncd_next_appt_date": None,
        }

        self.subject_visit = self.get_subject_visit()

        self.data.update(
            subject_visit=self.subject_visit.pk,
            report_datetime=self.subject_visit.report_datetime,
            hiv_next_appt_date=self.subject_visit.report_datetime
                               + relativedelta(months=1),
        )

    def test_ok(self):
        form = BaselineCareStatusForm(data=self.data)
        form.is_valid()
        self.assertEqual(form._errors, {})

    def test_hiv_next_appt_date_applicable(self):
        self.data.update(
            hiv_next_appt_date=(
                    self.subject_visit.report_datetime
                    + relativedelta(months=1))
        )
        form = BaselineCareStatusForm(data=self.data)
        form.is_valid()
        self.assertEqual(form._errors, {})

    def test_ncd_next_appt_date_not_applicable(self):
        self.data.update(
            ncd_next_appt_date=(
                    self.subject_visit.report_datetime
                    + relativedelta(months=1))
        )
        form = BaselineCareStatusForm(data=self.data)
        form.is_valid()
        self.assertIn("ncd_next_appt_date", form._errors)

    def test_hiv_next_appt_date_is_future(self):
        self.data.update(
            hiv_next_appt_date=(
                    self.subject_visit.report_datetime
                    - relativedelta(months=1))
        )
        form = BaselineCareStatusForm(data=self.data)
        form.is_valid()
        self.assertIn("hiv_next_appt_date", form._errors)

    def test_ncd_next_appt_date_is_future(self):
        self.data.update(
            hiv_next_appt_date=(
                    self.subject_visit.report_datetime
                    + relativedelta(months=1)),
            diabetic=YES,
            attending_ncd_clinic=YES,
            use_ncd_clinic_nearby=YES,
            ncd_next_appt_date=self.subject_visit.report_datetime
                               - relativedelta(months=1),
        )
        form = BaselineCareStatusForm(data=self.data)
        form.is_valid()
        self.assertIn("ncd_next_appt_date", form._errors)
