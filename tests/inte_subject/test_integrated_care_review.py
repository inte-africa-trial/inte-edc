from dateutil.relativedelta import relativedelta
from django import forms
from django.test import TestCase, tag
from edc_appointment.constants import COMPLETE_APPT, INCOMPLETE_APPT
from edc_appointment.creators import UnscheduledAppointmentCreator
from edc_constants.constants import HIV, NO, OTHER, YES
from edc_metadata import REQUIRED
from edc_metadata.models import CrfMetadata
from edc_utils import get_utcnow
from edc_visit_schedule.constants import MONTH6, MONTH12
from edc_visit_tracking.constants import UNSCHEDULED
from model_bakery import baker

from inte_lists.models import (
    HealthAdvisors,
    HealthInterventionTypes,
    HealthTalkConditions,
)
from inte_screening.constants import HIV_CLINIC
from inte_subject.forms.integrated_care_review_form import (
    IntegratedCareReviewFormValidator,
)
from tests.inte_test_case_mixin import InteTestCaseMixin


@tag("icr")
class TestIntegratedCareReview(InteTestCaseMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.baseline_datetime = get_utcnow()
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

    # TODO: Extract to InteTestCaseMixin
    @staticmethod
    def get_crf_metadata(subject_visit):
        return CrfMetadata.objects.filter(
            subject_identifier=subject_visit.subject_identifier,
            visit_code=subject_visit.visit_code,
            visit_code_sequence=subject_visit.visit_code_sequence,
            entry_status=REQUIRED,
        )

    @staticmethod
    def create_unscheduled(appointment):
        return UnscheduledAppointmentCreator(
            subject_identifier=appointment.subject_identifier,
            visit_schedule_name=appointment.visit_schedule_name,
            schedule_name=appointment.schedule_name,
            visit_code=appointment.visit_code,
            facility=appointment.facility,
        ).appointment

    def test_not_required_at_baseline(self):
        crfs = self.get_crf_metadata(self.subject_visit)
        self.assertNotIn("inte_subject.integratedcarereview", [o.model for o in crfs.all()])
        self.subject_visit.save()
        crfs = self.get_crf_metadata(self.subject_visit)
        self.assertNotIn("inte_subject.integratedcarereview", [o.model for o in crfs.all()])

    def test_required_at_6m_visit(self):
        subject_visit = self.get_subject_visit(
            subject_screening=self.subject_screening,
            subject_consent=self.subject_consent,
            visit_code=MONTH6,
        )
        crfs = self.get_crf_metadata(subject_visit)
        self.assertIn("inte_subject.integratedcarereview", [o.model for o in crfs.all()])

    def test_required_at_12m_visit(self):

        # Baseline visit
        self.subject_visit.appointment.appt_status = INCOMPLETE_APPT
        self.subject_visit.appointment.save()
        self.subject_visit.appointment.refresh_from_db()

        # Scheduled 6m visit
        subject_visit = self.get_subject_visit(
            subject_screening=self.subject_screening,
            subject_consent=self.subject_consent,
            visit_code=MONTH6,
        )
        integrated_care_review_6m = baker.make(
            "inte_subject.integratedcarereview", subject_visit=subject_visit
        )
        integrated_care_review_6m.save()

        subject_visit.appointment.appt_status = COMPLETE_APPT
        subject_visit.appointment.save()
        subject_visit.appointment.refresh_from_db()

        # Unscheduled visit (after 6m visit)
        subject_visit = self.get_subject_visit(
            appointment=self.create_unscheduled(subject_visit.appointment),
            reason=UNSCHEDULED,
            report_datetime=self.baseline_datetime + relativedelta(months=7),
        )
        crfs = self.get_crf_metadata(subject_visit)
        self.assertNotIn("inte_subject.integratedcarereview", [o.model for o in crfs.all()])

        subject_visit.appointment.appt_status = COMPLETE_APPT
        subject_visit.appointment.save()
        subject_visit.appointment.refresh_from_db()

        # Scheduled 12m visit
        subject_visit = self.get_subject_visit(
            subject_screening=self.subject_screening,
            subject_consent=self.subject_consent,
            visit_code=MONTH12,
        )
        crfs = self.get_crf_metadata(subject_visit)
        self.assertIn("inte_subject.integratedcarereview", [o.model for o in crfs.all()])
        integrated_care_review_12m = baker.make(
            "inte_subject.integratedcarereview", subject_visit=subject_visit
        )
        integrated_care_review_12m.save()

        subject_visit.appointment.appt_status = COMPLETE_APPT
        subject_visit.appointment.save()
        subject_visit.appointment.refresh_from_db()

        # Unscheduled visit (after 12m visit)
        subject_visit = self.get_subject_visit(
            appointment=self.create_unscheduled(subject_visit.appointment),
            reason=UNSCHEDULED,
            report_datetime=self.baseline_datetime + relativedelta(months=13),
        )
        crfs = self.get_crf_metadata(subject_visit)
        self.assertNotIn("inte_subject.integratedcarereview", [o.model for o in crfs.all()])


@tag("icr")
class TestIntegratedCareReviewFormValidation(InteTestCaseMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.subject_screening = self.get_subject_screening()
        self.subject_consent = self.get_subject_consent(self.subject_screening)
        self.subject_visit = self.get_subject_visit(
            subject_screening=self.subject_screening,
            subject_consent=self.subject_consent,
        )
        baker.make(
            "inte_subject.clinicalreviewbaseline",
            subject_visit=self.subject_visit,
            hiv_dx=YES,
        )

    def test_follow_up_questions_required_if_received_health_talk_messages(self):
        cleaned_data = {
            "subject_visit": self.subject_visit,
            "report_datetime": self.subject_visit.report_datetime,
            "receive_health_talk_messages": YES,
        }

        for (field_name, valid_qs) in [
            ("health_talk_conditions", HealthTalkConditions.objects.filter(name=HIV)),
            ("health_talk_focus", HealthInterventionTypes.objects.filter(name="lifestyle")),
            ("health_talk_presenters", HealthAdvisors.objects.filter(name="nurse")),
        ]:
            with self.subTest(
                f"Testing '{field_name}' is required",
                field_name=field_name,
                valid_qs=valid_qs,
            ):
                form_validator = IntegratedCareReviewFormValidator(cleaned_data=cleaned_data)
                try:
                    form_validator.validate()
                except forms.ValidationError:
                    pass
                self.assertIn(field_name, form_validator._errors)
                self.assertIn(
                    "This field is required",
                    str(form_validator._errors.get(field_name)),
                )
                self.assertEqual(len(form_validator._errors), 1, form_validator._errors)

                # Complete field, and move onto testing next one is required
                cleaned_data.update({field_name: valid_qs})

    def test_follow_up_questions_not_required_if_no_health_talk_messages_received(self):
        cleaned_data = {
            "subject_visit": self.subject_visit,
            "report_datetime": self.subject_visit.report_datetime,
            "receive_health_talk_messages": NO,
            "health_talk_conditions": HealthTalkConditions.objects.filter(name=HIV),
            "health_talk_focus": HealthInterventionTypes.objects.filter(name="lifestyle"),
            "health_talk_presenters": HealthAdvisors.objects.filter(name="nurse"),
        }

        for field_name in [
            "health_talk_conditions",
            "health_talk_focus",
            "health_talk_presenters",
        ]:
            with self.subTest(
                f"Testing '{field_name}' is not required",
                field_name=field_name,
            ):
                form_validator = IntegratedCareReviewFormValidator(cleaned_data=cleaned_data)
                try:
                    form_validator.validate()
                except forms.ValidationError:
                    pass
                self.assertIn(field_name, form_validator._errors)
                self.assertIn(
                    "This field is not required",
                    str(form_validator._errors.get(field_name)),
                )
                self.assertEqual(len(form_validator._errors), 1, form_validator._errors)

                # Remove field entry, and move onto testing next field is not required
                cleaned_data[field_name] = None

    def test_follow_up_questions_required_if_additional_health_advice(self):
        cleaned_data = {
            "subject_visit": self.subject_visit,
            "report_datetime": self.subject_visit.report_datetime,
            "receive_health_talk_messages": NO,
            "additional_health_advice": YES,
        }

        for (field_name, valid_qs) in [
            ("health_advice_advisor", HealthAdvisors.objects.filter(name="nurse")),
            ("health_advice_focus", HealthInterventionTypes.objects.filter(name="lifestyle")),
        ]:
            with self.subTest(
                f"Testing '{field_name}' is required",
                field_name=field_name,
                valid_qs=valid_qs,
            ):
                form_validator = IntegratedCareReviewFormValidator(cleaned_data=cleaned_data)
                try:
                    form_validator.validate()
                except forms.ValidationError:
                    pass
                self.assertIn(field_name, form_validator._errors, form_validator._errors)
                self.assertIn(
                    "This field is required",
                    str(form_validator._errors.get(field_name)),
                )
                self.assertEqual(len(form_validator._errors), 1, form_validator._errors)

                # Complete field, and move onto testing next one is required
                cleaned_data.update({field_name: valid_qs})

    def test_follow_up_questions_not_required_if_no_additional_health_advice(self):
        cleaned_data = {
            "subject_visit": self.subject_visit,
            "report_datetime": self.subject_visit.report_datetime,
            "additional_health_advice": NO,
            "health_advice_advisor": HealthAdvisors.objects.filter(name="nurse"),
            "health_advice_focus": HealthInterventionTypes.objects.filter(name="lifestyle"),
        }

        for field_name in [
            "health_advice_advisor",
            "health_advice_focus",
        ]:
            with self.subTest(
                f"Testing '{field_name}' is not required",
                field_name=field_name,
            ):
                form_validator = IntegratedCareReviewFormValidator(cleaned_data=cleaned_data)
                try:
                    form_validator.validate()
                except forms.ValidationError:
                    pass
                self.assertIn(field_name, form_validator._errors)
                self.assertIn(
                    "This field is not required",
                    str(form_validator._errors.get(field_name)),
                )
                self.assertEqual(len(form_validator._errors), 1, form_validator._errors)

                # Remove field entry, and move onto testing next field is not required
                cleaned_data[field_name] = None

    def test_other_field_required_if_other_specified(self):
        cleaned_data = {
            "subject_visit": self.subject_visit,
            "report_datetime": self.subject_visit.report_datetime,
            "receive_health_talk_messages": YES,
            "additional_health_advice": YES,
        }
        other_condition = HealthTalkConditions.objects.filter(name=OTHER)
        other_category = HealthInterventionTypes.objects.filter(name=OTHER)
        other_presenter = HealthAdvisors.objects.filter(name=OTHER)

        for (field_name, valid_qs) in [
            ("health_talk_conditions", other_condition),
            ("health_talk_focus", other_category),
            ("health_talk_presenters", other_presenter),
            ("health_advice_advisor", other_presenter),
            ("health_advice_focus", other_category),
        ]:
            # Select 'other', then test it's required
            cleaned_data.update({field_name: valid_qs})
            field_name_other = f"{field_name}_other"

            with self.subTest(
                f"Testing '{field_name_other}' with '{field_name}' and '{valid_qs}'",
                field_name_other=field_name_other,
            ):
                form_validator = IntegratedCareReviewFormValidator(cleaned_data=cleaned_data)
                try:
                    form_validator.validate()
                except forms.ValidationError:
                    pass
                self.assertIn(field_name_other, form_validator._errors)
                self.assertIn(
                    "This field is required",
                    str(form_validator._errors.get(field_name_other)),
                )
                self.assertEqual(len(form_validator._errors), 1, form_validator._errors)

            # Complete 'other' field, and move onto next test
            cleaned_data.update({field_name_other: "Some other value"})
