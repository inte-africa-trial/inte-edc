from dateutil.relativedelta import relativedelta
from django.forms import forms
from django.test import TestCase, tag
from edc_constants.constants import NOT_APPLICABLE, NO, YES
from edc_utils import get_utcnow
from inte_screening.constants import HIV_CLINIC, NCD_CLINIC
from inte_subject.form_validators import BaselineCareStatusFormValidator
from inte_subject.forms import BaselineCareStatusForm
from pytz import timezone

from ..inte_test_case_mixin import InteTestCaseMixin


def get_now():
    return get_utcnow().astimezone(timezone("Africa/Kampala"))


class TestBaselineCareStatus(InteTestCaseMixin, TestCase):
    def setUp(self):
        super().setUp()
        subject_screening = self.get_subject_screening(
            report_datetime=get_utcnow(), clinic_type=HIV_CLINIC
        )
        self.consent = self.get_subject_consent(
            subject_screening=subject_screening, clinic_type=HIV_CLINIC
        )

        # set up condition in HIV clinic, no co-morbidity
        self.data = {
            "hiv": YES,
            "receives_care_at_hiv_clinic": YES,
            "attends_this_hiv_clinic": YES,
            "hiv_clinic_willing_to_transfer": NOT_APPLICABLE,
            "hiv_clinic_other_is_study_clinic": NOT_APPLICABLE,
            "hiv_clinic_other": None,
            "hiv_clinic_next_appt_date": None,
            "diabetic": NO,
            "hypertensive": NO,
            "receives_care_at_ncd_clinic": NOT_APPLICABLE,
            "attends_this_ncd_clinic": NOT_APPLICABLE,
            "ncd_clinic_willing_to_transfer": NOT_APPLICABLE,
            "ncd_clinic_other_is_study_clinic": NOT_APPLICABLE,
            "ncd_clinic_other": None,
            "ncd_clinic_next_appt_date": None,
        }

        self.subject_visit = self.get_subject_visit()

        self.data.update(
            subject_visit=self.subject_visit.pk,
            report_datetime=self.subject_visit.report_datetime,
            hiv_clinic_next_appt_date=(
                self.subject_visit.report_datetime + relativedelta(months=1)
            ),
        )

    def test_form_ok(self):
        """Assert default data above validates."""
        form = BaselineCareStatusForm(data=self.data)
        form.is_valid()
        self.assertEqual(form._errors, {})

    def test_form_hiv_next_appt_date_required(self):
        self.data.update(
            hiv_clinic_next_appt_date=(
                self.subject_visit.report_datetime + relativedelta(months=1)
            )
        )
        form = BaselineCareStatusForm(data=self.data)
        form.is_valid()
        self.assertEqual(form._errors, {})

    def test_form_ncd_next_appt_date_not_required(self):
        self.data.update(
            ncd_clinic_next_appt_date=(
                self.subject_visit.report_datetime + relativedelta(months=1)
            )
        )
        form = BaselineCareStatusForm(data=self.data)
        form.is_valid()
        self.assertIn("ncd_clinic_next_appt_date", form._errors)

    def test_form_hiv_next_appt_date_is_future(self):
        self.data.update(
            hiv_clinic_next_appt_date=(
                self.subject_visit.report_datetime - relativedelta(months=1)
            )
        )
        form = BaselineCareStatusForm(data=self.data)
        form.is_valid()
        self.assertIn("hiv_clinic_next_appt_date", form._errors)

    def test_form_ncd_next_appt_date_is_future(self):
        self.data.update(
            hiv_clinic_next_appt_date=(
                self.subject_visit.report_datetime + relativedelta(months=1)
            ),
            diabetic=YES,
            receives_care_at_ncd_clinic=YES,
            attends_this_ncd_clinic=YES,
            ncd_clinic_willing_to_transfer=NOT_APPLICABLE,
            ncdh_clinic_other_is_study_clinic=NOT_APPLICABLE,
            ncd_clinic_other=None,
            ncd_next_appt_date=(
                self.subject_visit.report_datetime - relativedelta(months=1)
            ),
        )
        form = BaselineCareStatusForm(data=self.data)
        form.is_valid()
        self.assertIn("ncd_clinic_next_appt_date", form._errors)

    def test_validator_ok(self):
        user_input = {
            "subject_visit": self.subject_visit,
            "hiv": YES,
            "receives_care_at_hiv_clinic": YES,
            "attends_this_hiv_clinic": YES,
            "hiv_clinic_other_is_study_clinic": NOT_APPLICABLE,
            "hiv_clinic_next_appt_date": get_now(),
            "diabetic": NO,
            "hypertensive": NO,
            "receives_care_at_ncd_clinic": NOT_APPLICABLE,
            "attends_this_ncd_clinic": NOT_APPLICABLE,
            "ncd_clinic_other_is_study_clinic": NOT_APPLICABLE,
            "ncd_clinic_next_appt_date": None,
        }

        form_validator = BaselineCareStatusFormValidator(cleaned_data=user_input)
        form_validator.validate()
        self.assertEqual(form_validator._errors, {})

    def test_validator_hiv_pos_attending(self):
        user_input = {
            "subject_visit": self.subject_visit,
            "hiv": YES,
            "receives_care_at_hiv_clinic": YES,
            "attends_this_hiv_clinic": YES,
            "hiv_clinic_other_is_study_clinic": NOT_APPLICABLE,
            "hiv_clinic_next_appt_date": get_now(),
        }
        form_validator = BaselineCareStatusFormValidator(cleaned_data=user_input)
        form_validator.validate()
        self.assertEqual(form_validator._errors, {})

    def test_validator_ncd_attending_must_have_one_condition(self):
        subject_screening = self.get_subject_screening(
            report_datetime=get_utcnow(), clinic_type=NCD_CLINIC
        )
        subject_consent = self.get_subject_consent(
            subject_screening=subject_screening, clinic_type=NCD_CLINIC
        )
        subject_visit = self.get_subject_visit(
            subject_screening=subject_screening, subject_consent=subject_consent
        )

        user_input = {
            "subject_visit": subject_visit,
            "hiv": NO,
            "receives_care_at_hiv_clinic": NOT_APPLICABLE,
            "attends_this_hiv_clinic": NOT_APPLICABLE,
            "hiv_clinic_other_is_study_clinic": NOT_APPLICABLE,
            "hiv_clinic_other": None,
            "hiv_clinic_willing_to_transfer": NOT_APPLICABLE,
            "hiv_clinic_next_appt_date": None,
            "diabetic": NO,
            "hypertensive": NO,
            "receives_care_at_ncd_clinic": NOT_APPLICABLE,
            "attends_this_ncd_clinic": NOT_APPLICABLE,
            "ncd_clinic_other_is_study_clinic": NOT_APPLICABLE,
            "ncd_clinic_other": None,
            "ncd_clinic_willing_to_transfer": NOT_APPLICABLE,
            "ncd_clinic_next_appt_date": None,
        }
        form_validator = BaselineCareStatusFormValidator(cleaned_data=user_input)
        self.assertRaises(forms.ValidationError, form_validator.validate)
        self.assertIn("__all__", form_validator._errors)

    def test_validator_hiv_but_also_attending_ncd(self):
        user_input = {
            "subject_visit": self.subject_visit,
            "hiv": YES,
            "receives_care_at_hiv_clinic": YES,
            "attends_this_hiv_clinic": YES,
            "hiv_clinic_other_is_study_clinic": NOT_APPLICABLE,
            "hiv_clinic_other": None,
            "hiv_clinic_willing_to_transfer": NOT_APPLICABLE,
            "hiv_clinic_next_appt_date": get_now() + relativedelta(months=3),
            "diabetic": YES,
            "hypertensive": NO,
            "receives_care_at_ncd_clinic": YES,
            "attends_this_ncd_clinic": NO,
            "ncd_clinic_other_is_study_clinic": NO,
            "ncd_clinic_other": None,
            "ncd_clinic_willing_to_transfer": NO,
            "ncd_clinic_next_appt_date": None,
        }
        user_input.update(ncd_clinic_other=None)
        form_validator = BaselineCareStatusFormValidator(cleaned_data=user_input)
        self.assertRaises(forms.ValidationError, form_validator.validate)
        self.assertIn("ncd_clinic_other", form_validator._errors)

        user_input.update(ncd_clinic_other="kinoni")
        user_input.update(ncd_clinic_willing_to_transfer=NOT_APPLICABLE)
        form_validator = BaselineCareStatusFormValidator(cleaned_data=user_input)
        self.assertRaises(forms.ValidationError, form_validator.validate)
        self.assertIn("ncd_clinic_willing_to_transfer", form_validator._errors)

        user_input.update(ncd_clinic_willing_to_transfer=YES)
        form_validator = BaselineCareStatusFormValidator(cleaned_data=user_input)
        self.assertRaises(forms.ValidationError, form_validator.validate)
        self.assertIn("ncd_clinic_next_appt_date", form_validator._errors)

        user_input.update(ncd_clinic_next_appt_date=get_now() + relativedelta(months=1))
        form_validator = BaselineCareStatusFormValidator(cleaned_data=user_input)
        form_validator.validate()
        self.assertEqual(form_validator._errors, {})
