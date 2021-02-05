from pprint import pprint

from dateutil.relativedelta import relativedelta
from django.forms import ValidationError
from django.test import TestCase, tag
from edc_constants.constants import NO, NOT_APPLICABLE, OTHER, YES
from edc_prn.constants import DEVIATION, MEDICATION_NONCOMPLIANCE, VIOLATION
from edc_utils import get_utcnow
from model_bakery import baker

from inte_prn.form_validators import ProtocolDeviationViolationFormValidator
from inte_screening.constants import HIV_CLINIC

from ..inte_test_case_mixin import InteTestCaseMixin


class TestProtocolViolation(InteTestCaseMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.subject_screening = None
        self.subject_consent = None
        self.subject_visit = None

    def prepare(self):
        self.subject_screening = self.get_subject_screening(
            report_datetime=get_utcnow(), clinic_type=HIV_CLINIC
        )
        self.subject_consent = self.get_subject_consent(
            subject_screening=self.subject_screening, clinic_type=HIV_CLINIC
        )
        self.subject_visit = self.get_subject_visit(
            subject_screening=self.subject_screening,
            subject_consent=self.subject_consent,
        )
        baker.make(
            "inte_subject.clinicalreviewbaseline",
            subject_visit=self.subject_visit,
            hiv_test=YES,
            hiv_dx=YES,
            hiv_test_ago="5y",
        )
        baker.make(
            "inte_subject.hivinitialreview",
            subject_visit=self.subject_visit,
            dx_date=get_utcnow() - relativedelta(years=5),
            arv_initiation_ago="4y",
        )

    @tag("pv")
    def test_protocol_violation(self):
        self.prepare()
        cleaned_data = {
            "subject_idenfifier": self.subject_consent.subject_identifier,
            "report_datetime": get_utcnow(),
            "date_open": get_utcnow(),
            "comment": "",
        }
        form_validator = ProtocolDeviationViolationFormValidator(cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            pprint(form_validator._errors)
            self.fail("ValidationError unexpectedly raised.")

    @tag("pv")
    def test_report_type_deviation(self):
        """If deviation, safety_impact and safety_impact_details
        are not applicable.
        """

        cleaned_data = {
            "violation_datetime": get_utcnow(),
            "violation_type": MEDICATION_NONCOMPLIANCE,
            "violation_description": "test description",
            "violation_reason": "test violation reason",
            "report_type": DEVIATION,
        }

        cleaned_data.update({"safety_impact": NO, "safety_impact_details": NO})

        form_validator = ProtocolDeviationViolationFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn("safety_impact", form_validator._errors)

        cleaned_data.update({"safety_impact": NOT_APPLICABLE, "safety_impact_details": NO})

        form_validator = ProtocolDeviationViolationFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn("safety_impact_details", form_validator._errors)

    @tag("pv")
    def test_report_type(self):
        """violation_datetime is not required if it's
        a protocol deviation
        """
        field_required_list = [
            ("violation_datetime", get_utcnow()),
            ("violation_type", MEDICATION_NONCOMPLIANCE),
            ("violation_description", "test description"),
            ("violation_reason", "test violation reason"),
        ]
        for field_item in field_required_list:
            field, value = field_item
            cleaned_data = {"report_type": DEVIATION, field: value}
            form_validator = ProtocolDeviationViolationFormValidator(cleaned_data=cleaned_data)
            self.assertRaises(ValidationError, form_validator.validate)
            self.assertIn(field, form_validator._errors)

    @tag("pv")
    def test_report_type1(self):
        """report_type is DEVIATION then
        (violation_datetime, violation_type, etc) should be None.
        """
        field_required_list = [
            ("violation_datetime", None),
            ("violation_type", None),
            ("violation_description", None),
            ("violation_reason", None),
        ]
        for field_item in field_required_list:
            field, value = field_item
            cleaned_data = {"report_type": DEVIATION, field: value}
            form_validator = ProtocolDeviationViolationFormValidator(cleaned_data=cleaned_data)
            self.assertFalse(form_validator._errors)

    @tag("pv")
    def test_violation(self):
        """violation_datetime is not required if it's
        a protocol deviation
        """
        field_required_list = [
            ("violation_datetime", get_utcnow()),
            ("violation_type", MEDICATION_NONCOMPLIANCE),
            ("violation_description", "test description"),
            ("violation_reason", "test violation reason"),
        ]
        for field_item in field_required_list:
            field, value = field_item
            cleaned_data = {"report_type": VIOLATION, field: value}
            form_validator = ProtocolDeviationViolationFormValidator(cleaned_data=cleaned_data)
            self.assertFalse(form_validator._errors)

    @tag("pv")
    def test_yes_safety_impact_none_details(self):
        """Asserts safety_impact has valid
        safety_impact_details provided.
        """
        cleaned_data = {"safety_impact": YES, "safety_impact_details": None}
        form_validator = ProtocolDeviationViolationFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn("safety_impact_details", form_validator._errors)

    @tag("pv")
    def test_yes_safety_impact_with_details(self):
        """Asserts safety_impact has valid
        safety_impact_details provided.
        """
        cleaned_data = {"safety_impact": YES, "safety_impact_details": "explanation"}
        protocol_dev = ProtocolDeviationViolationFormValidator(cleaned_data=cleaned_data)
        try:
            protocol_dev.validate()
        except ValidationError as e:
            self.fail(f"ValidationError unexpectedly raised. Got{e}")

    @tag("pv")
    def test_no_safety_impact_none_details(self):
        """Asserts safety_impact has valid
        safety_impact_details provided.
        """
        cleaned_data = {"safety_impact": NO, "safety_impact_details": None}
        protocol_dev = ProtocolDeviationViolationFormValidator(cleaned_data=cleaned_data)
        try:
            protocol_dev.validate()
        except ValidationError as e:
            self.fail(f"ValidationError unexpectedly raised. Got{e}")

    @tag("pv")
    def test_no_safety_impact_with_details(self):
        """Asserts safety_impact has valid
        safety_impact_details provided.
        """
        cleaned_data = {"safety_impact": NO, "safety_impact_details": "details"}
        form_validator = ProtocolDeviationViolationFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn("safety_impact_details", form_validator._errors)

    @tag("pv")
    def test_study_outcomes_impact_with_details(self):
        """Asserts study_outcomes_impact has valid
        safety_impact_details provided.
        """
        cleaned_data = {
            "study_outcomes_impact": YES,
            "study_outcomes_impact_details": None,
        }
        form_validator = ProtocolDeviationViolationFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn("study_outcomes_impact_details", form_validator._errors)

    @tag("pv")
    def test_yes_study_outcomes_impact_with_details(self):
        """Asserts study_outcomes_impact has valid
        safety_impact_details provided.
        """
        cleaned_data = {
            "study_outcomes_impact": YES,
            "study_outcomes_impact_details": "explanation",
        }
        protocol_dev = ProtocolDeviationViolationFormValidator(cleaned_data=cleaned_data)
        try:
            protocol_dev.validate()
        except ValidationError as e:
            self.fail(f"ValidationError unexpectedly raised. Got{e}")

    @tag("pv")
    def test_no_study_outcomes_impact_none_details(self):
        cleaned_data = {
            "study_outcomes_impact": NO,
            "study_outcomes_impact_details": None,
        }
        protocol_dev = ProtocolDeviationViolationFormValidator(cleaned_data=cleaned_data)
        try:
            protocol_dev.validate()
        except ValidationError as e:
            self.fail(f"ValidationError unexpectedly raised. Got{e}")

    @tag("pv")
    def test_no_study_outcomes_impact_with_details(self):
        cleaned_data = {
            "study_outcomes_impact": NO,
            "study_outcomes_impact_details": "details",
        }
        form_validator = ProtocolDeviationViolationFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn("study_outcomes_impact_details", form_validator._errors)

    @tag("pv")
    def test_other_protocol_violation_none_other_protocol_violation(self):
        cleaned_data = {"violation_type": OTHER, "violation_type_other": None}
        form_validator = ProtocolDeviationViolationFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn("violation_type_other", form_validator._errors)

    @tag("pv")
    def test_other_protocol_violation_other_protocol_violation(self):
        cleaned_data = {
            "violation_type": OTHER,
            "violation_type_other": "some_violation",
        }
        protocol_dev = ProtocolDeviationViolationFormValidator(cleaned_data=cleaned_data)
        try:
            protocol_dev.validate()
        except ValidationError as e:
            self.fail(f"ValidationError unexpectedly raised. Got{e}")

    @tag("pv")
    def test_corrective_action_datetime(self):
        cleaned_data = {
            "corrective_action_datetime": get_utcnow(),
            "corrective_action": None,
        }
        form_validator = ProtocolDeviationViolationFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn("corrective_action", form_validator._errors)

        cleaned_data = {"corrective_action_datetime": None, "corrective_action": "blah"}
        form_validator = ProtocolDeviationViolationFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn("corrective_action", form_validator._errors)
