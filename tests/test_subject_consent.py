import uuid

from dateutil.relativedelta import relativedelta
from django import forms
from django.test import TestCase, tag
from edc_constants.constants import MALE, MOBILE_NUMBER, YES, NO, NOT_APPLICABLE
from edc_utils import get_utcnow
from inte_consent.form_validators import SubjectConsentFormValidator
from inte_consent.forms import SubjectConsentForm
from inte_consent.models import InteSubjectConsentError
from inte_screening.constants import HIV_CLINIC, NCD_CLINIC
from pytz import timezone

from .inte_test_case_mixin import InteTestCaseMixin


def get_now():
    return get_utcnow().astimezone(timezone("Africa/Kampala"))


class TestSubjectConsent(InteTestCaseMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.eligibility_datetime = get_utcnow() - relativedelta(days=1)  # yesterday
        self.subject_screening = self.get_subject_screening(
            report_datetime=get_utcnow(), eligibility_datetime=self.eligibility_datetime
        )
        self.screening_identifier = self.subject_screening.screening_identifier

    def test_form_validator_ok(self):
        consent_datetime = get_now()
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

    def test_form_validator_consent_before_eligibility_datetime(self):
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

    def test_form_validator_consent_after_eligibility_datetime(self):
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

    def test_model_consent(self):
        subject_screening = self.get_subject_screening(clinic_type=HIV_CLINIC)
        subject_consent = self.get_subject_consent(
            subject_screening, clinic_type=HIV_CLINIC
        )
        self.assertIsNotNone(subject_consent.subject_identifier)

        subject_screening = self.get_subject_screening(clinic_type=HIV_CLINIC)
        self.assertRaises(
            InteSubjectConsentError,
            self.get_subject_consent,
            subject_screening,
            clinic_type=NCD_CLINIC,
        )

    def test_model_clinic_type_must_match(self):
        subject_screening = self.get_subject_screening(clinic_type=HIV_CLINIC)
        self.assertRaises(
            InteSubjectConsentError,
            self.get_subject_consent,
            subject_screening,
            clinic_type=NCD_CLINIC,
        )

    def test_model_clinic_type_cannot_be_changed(self):
        subject_screening = self.get_subject_screening(clinic_type=HIV_CLINIC)
        subject_consent = self.get_subject_consent(
            subject_screening, clinic_type=HIV_CLINIC
        )

        subject_consent.clinic_type = NCD_CLINIC
        self.assertRaises(InteSubjectConsentError, subject_consent.save)

    def test_form_clinic_type_cannot_be_changed(self):
        subject_screening = self.get_subject_screening(clinic_type=HIV_CLINIC)
        consent_datetime = self.subject_screening.eligibility_datetime + relativedelta(
            minutes=1
        )
        consent_datetime = consent_datetime.astimezone(timezone("Africa/Kampala"))
        data = dict(
            assessment_score=YES,
            citizen=YES,
            clinic_type=HIV_CLINIC,
            confirm_identity="77777777",
            consent_copy=YES,
            consent_datetime=consent_datetime,
            consent_reviewed=YES,
            consent_signature=YES,
            dob=self.subject_screening.report_datetime.date() - relativedelta(years=25),
            first_name="PAT",
            gender=MALE,
            identity="77777777",
            identity_type=MOBILE_NUMBER,
            initials="PM",
            is_dob_estimated="-",
            is_incarcerated=NO,
            is_literate=YES,
            language="en",
            last_name="METHENY",
            legal_marriage=NO,
            marriage_certificate=NOT_APPLICABLE,
            may_store_genetic_samples=YES,
            may_store_samples=YES,
            screening_identifier=subject_screening.screening_identifier,
            study_questions=YES,
            subject_screening=str(subject_screening.id),
            subject_type="subject",
            subject_identifier=str(uuid.uuid4()),
            user_created="erikvw",
        )

        form = SubjectConsentForm(data=data)
        form.is_valid()
        instance = form.save()

        data.update(
            subject_identifier=instance.subject_identifier, clinic_type=NCD_CLINIC,
        )
        form = SubjectConsentForm(data=data, instance=instance)
        form.is_valid()
        self.assertIn("clinic_type", form._errors)
