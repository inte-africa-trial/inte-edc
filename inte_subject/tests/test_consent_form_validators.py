from dateutil.relativedelta import relativedelta
from django import forms
from django.test import TestCase, tag
from edc_consent.constants import MOBILE_NUMBER
from edc_constants.constants import MALE
from edc_utils.date import get_utcnow
from inte_form_validators.form_validators import SubjectConsentFormValidator
from inte_screening.tests.inte_test_case_mixin import InteTestCaseMixin
from pytz import timezone


class TestFormValidators(InteTestCaseMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.eligibility_datetime = get_utcnow() - relativedelta(days=1)  # yesterday
        self.subject_screening = self.get_subject_screening(
            report_datetime=get_utcnow(), eligibility_datetime=self.eligibility_datetime
        )
        self.screening_identifier = self.subject_screening.screening_identifier

    def get_now(self):
        return get_utcnow().astimezone(timezone("Africa/Kampala"))

    def test_subject_consent_form_validator_ok(self):
        consent_datetime = self.get_now()
        cleaned_data = dict(
            screening_identifier=self.screening_identifier,
            dob=self.subject_screening.report_datetime.date() - relativedelta(years=25),
            consent_datetime=consent_datetime,
            identity_type=MOBILE_NUMBER,
            identity="77777777",
            confirm_identity="77777777",
            gender=MALE,
        )
        validator = SubjectConsentFormValidator(cleaned_data=cleaned_data,)
        validator.clean()

    def test_consent_before_eligibility_datetime(self):
        consent_datetime = self.subject_screening.eligibility_datetime - relativedelta(
            minutes=1
        )
        consent_datetime = consent_datetime.astimezone(timezone("Africa/Kampala"))
        cleaned_data = dict(
            screening_identifier=self.screening_identifier,
            dob=self.subject_screening.report_datetime.date() - relativedelta(years=25),
            consent_datetime=consent_datetime,
            identity_type=MOBILE_NUMBER,
            identity="77777777",
            confirm_identity="77777777",
            gender=MALE,
        )
        validator = SubjectConsentFormValidator(cleaned_data=cleaned_data,)
        self.assertRaises(forms.ValidationError, validator.clean)
        with self.assertRaises(forms.ValidationError) as cm:
            validator.clean()
        self.assertIn("consent_datetime", str(cm.exception))

    def test_consent_after_eligibility_datetime(self):
        consent_datetime = self.subject_screening.eligibility_datetime + relativedelta(
            minutes=1
        )
        consent_datetime = consent_datetime.astimezone(timezone("Africa/Kampala"))
        cleaned_data = dict(
            screening_identifier=self.screening_identifier,
            dob=self.subject_screening.report_datetime.date() - relativedelta(years=25),
            consent_datetime=consent_datetime,
            identity_type=MOBILE_NUMBER,
            identity="77777777",
            confirm_identity="77777777",
            gender=MALE,
        )
        validator = SubjectConsentFormValidator(cleaned_data=cleaned_data,)
        try:
            validator.clean()
        except forms.ValidationError:
            self.fail("ValidationError unexpectedly raised")
