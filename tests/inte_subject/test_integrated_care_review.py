from dateutil.relativedelta import relativedelta
from django.test import TestCase, override_settings, tag
from edc_appointment.constants import COMPLETE_APPT, INCOMPLETE_APPT
from edc_appointment.creators import UnscheduledAppointmentCreator
from edc_constants.choices import YES_NO_DONT_KNOW
from edc_constants.constants import COMPLETE, HIV, NO, NOT_APPLICABLE, OTHER, YES
from edc_utils import get_utcnow
from edc_visit_schedule.constants import MONTH6, MONTH12
from edc_visit_tracking.constants import UNSCHEDULED
from model_bakery import baker

from inte_lists.models import (
    DrugDispensaries,
    DrugDispensers,
    HealthAdvisors,
    HealthInterventionTypes,
    HealthTalkConditions,
    LaboratoryTests,
)
from inte_prn.models import IntegratedCareClinicRegistration
from inte_screening.constants import HIV_CLINIC
from inte_subject.choices import HCF_PRESCRIPTION_COLLECTION_CHOICES
from inte_subject.constants import NURSE
from inte_subject.forms.integrated_care_review_form import (
    IntegratedCareReviewForm,
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

    form_validator_default_form_cls = IntegratedCareReviewFormValidator

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

    @override_settings(SITE_ID=103)
    def test_form_validator_requires_icc_registration_for_intervention(self):
        cleaned_data = {
            "subject_visit": self.subject_visit,
            "crf_status": COMPLETE,
            "report_datetime": self.subject_visit.report_datetime,
            "receive_health_talk_messages": NO,
            "additional_health_advice": NO,
        }
        form = IntegratedCareReviewForm(data=cleaned_data)
        form.is_valid()
        self.assertIn("__all__", form._errors)
        self.assertIn(
            IntegratedCareClinicRegistration._meta.verbose_name,
            ";".join(form._errors.get("__all__")),
        )

    @override_settings(SITE_ID=101)
    def test_form_validator_does_not_require_icc_registration_for_control(self):
        cleaned_data = {
            "subject_visit": self.subject_visit,
            "crf_status": COMPLETE,
            "report_datetime": self.subject_visit.report_datetime,
            "receive_health_talk_messages": NO,
            "additional_health_advice": NO,
        }
        form = IntegratedCareReviewForm(data=cleaned_data)
        form.is_valid()
        self.assertNotIn(
            IntegratedCareClinicRegistration._meta.verbose_name,
            ";".join(form._errors.get("__all__") or []),
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
            ("health_talk_presenters", HealthAdvisors.objects.filter(name=NURSE)),
        ]:
            with self.subTest(
                f"Testing '{field_name}' is required",
                field_name=field_name,
                valid_qs=valid_qs,
            ):
                form_validator = self.validate_form_validator(cleaned_data)
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
            "health_talk_presenters": HealthAdvisors.objects.filter(name=NURSE),
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
                form_validator = self.validate_form_validator(cleaned_data)
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
            ("health_advice_advisor", HealthAdvisors.objects.filter(name=NURSE)),
            ("health_advice_focus", HealthInterventionTypes.objects.filter(name="lifestyle")),
        ]:
            with self.subTest(
                f"Testing '{field_name}' is required",
                field_name=field_name,
                valid_qs=valid_qs,
            ):
                form_validator = self.validate_form_validator(cleaned_data)
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
            "health_advice_advisor": HealthAdvisors.objects.filter(name=NURSE),
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
                form_validator = self.validate_form_validator(cleaned_data)
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
            "receive_rx_today": YES,
            "rx_collection_hcf": YES,
            "missed_appt": YES,
            "missed_appt_call": YES,
            "lab_tests": YES,
            "pay_for_lab_tests": YES,
        }
        other_condition = HealthTalkConditions.objects.filter(name=OTHER)
        other_category = HealthInterventionTypes.objects.filter(name=OTHER)
        other_presenter = HealthAdvisors.objects.filter(name=OTHER)
        other_dispensary = DrugDispensaries.objects.filter(name=OTHER)
        other_dispenser = DrugDispensers.objects.filter(name=OTHER)
        other_lab_test = LaboratoryTests.objects.filter(name=OTHER)

        for (field_name, valid_qs) in [
            ("health_talk_conditions", other_condition),
            ("health_talk_focus", other_category),
            ("health_talk_presenters", other_presenter),
            ("health_advice_advisor", other_presenter),
            ("health_advice_focus", other_category),
            ("where_rx_dispensed", other_dispensary),
            ("who_dispenses_rx", other_dispenser),
            ("missed_appt_call_who", OTHER),
            ("which_lab_tests_charged_for", other_lab_test),
        ]:
            # Select 'other', then test it's required
            cleaned_data.update({field_name: valid_qs})
            field_name_other = f"{field_name}_other"

            with self.subTest(
                f"Testing '{field_name_other}' with '{field_name}' and '{valid_qs}'",
                field_name_other=field_name_other,
            ):
                form_validator = self.validate_form_validator(cleaned_data)
                self.assertIn(field_name_other, form_validator._errors)
                self.assertIn(
                    "This field is required",
                    str(form_validator._errors.get(field_name_other)),
                )
                self.assertEqual(len(form_validator._errors), 1, form_validator._errors)

            # Complete 'other' field, and move onto next test
            cleaned_data.update({field_name_other: "Some other value"})

    def test_receive_rx_today_required(self):
        cleaned_data = {
            "subject_visit": self.subject_visit,
            "report_datetime": self.subject_visit.report_datetime,
            "receive_health_talk_messages": NO,
            "additional_health_advice": NO,
        }
        form_validator = self.validate_form_validator(cleaned_data)
        self.assertIn("receive_rx_today", form_validator._errors)
        self.assertIn(
            "This field is required",
            str(form_validator._errors.get("receive_rx_today")),
        )
        self.assertEqual(len(form_validator._errors), 1, form_validator._errors)

        # Complete field, and confirm no longer a listed error
        cleaned_data.update({"receive_rx_today": NO})
        form_validator = self.validate_form_validator(cleaned_data)
        self.assertNotIn("receive_rx_today", form_validator._errors)

    def test_rx_collection_hcf_required_if_receive_rx_today(self):
        cleaned_data = {
            "subject_visit": self.subject_visit,
            "report_datetime": self.subject_visit.report_datetime,
            "receive_health_talk_messages": NO,
            "additional_health_advice": NO,
            "receive_rx_today": YES,
        }
        form_validator = self.validate_form_validator(cleaned_data)
        self.assertIn("rx_collection_hcf", form_validator._errors)
        self.assertIn(
            "This field is required",
            str(form_validator._errors.get("rx_collection_hcf")),
        )

        # Test no errors when q answered
        cleaned_data.update({"rx_collection_hcf": YES})
        form_validator = self.validate_form_validator(cleaned_data)
        self.assertNotIn("rx_collection_hcf", form_validator._errors)

    def test_rx_collection_hcf_not_applicable_if_receive_no_prescription_today(self):
        cleaned_data = {
            "subject_visit": self.subject_visit,
            "report_datetime": self.subject_visit.report_datetime,
            "receive_health_talk_messages": NO,
            "additional_health_advice": NO,
            "receive_rx_today": NO,
            "rx_collection_hcf": NOT_APPLICABLE,
        }
        form_validator = self.validate_form_validator(cleaned_data)
        self.assertNotIn("rx_collection_hcf", form_validator._errors)

        # Test raises error when not required, but IS selected
        for answer, _ in HCF_PRESCRIPTION_COLLECTION_CHOICES:
            if answer != NOT_APPLICABLE:
                cleaned_data.update({"rx_collection_hcf": answer})
                form_validator = self.validate_form_validator(cleaned_data)
                self.assertIn("rx_collection_hcf", form_validator._errors)
                self.assertIn(
                    "This field is not required",
                    str(form_validator._errors.get("rx_collection_hcf")),
                )

    def test_follow_up_questions_required_if_rx_collection_hcf(self):
        cleaned_data = {
            "subject_visit": self.subject_visit,
            "report_datetime": self.subject_visit.report_datetime,
            "receive_health_talk_messages": NO,
            "additional_health_advice": NO,
            "receive_rx_today": YES,
            "rx_collection_hcf": YES,
        }

        for (field_name, valid_qs) in [
            ("where_rx_dispensed", DrugDispensaries.objects.filter(name="pharmacy")),
            ("who_dispenses_rx", DrugDispensers.objects.filter(name="pharmacist")),
        ]:
            with self.subTest(
                f"Testing '{field_name}' is required",
                field_name=field_name,
                valid_qs=valid_qs,
            ):
                form_validator = self.validate_form_validator(cleaned_data)
                self.assertIn(field_name, form_validator._errors)
                self.assertIn(
                    "This field is required",
                    str(form_validator._errors.get(field_name)),
                )
                self.assertEqual(len(form_validator._errors), 1, form_validator._errors)

                # Complete field, and move onto testing next one is required
                cleaned_data.update({field_name: valid_qs})

    def test_follow_up_questions_not_required_if_not_rx_collection_hcf(self):
        cleaned_data = {
            "subject_visit": self.subject_visit,
            "report_datetime": self.subject_visit.report_datetime,
            "receive_health_talk_messages": NO,
            "additional_health_advice": NO,
            "receive_rx_today": YES,
            "rx_collection_hcf": NO,
            "where_rx_dispensed": DrugDispensaries.objects.filter(name="pharmacy"),
            "who_dispenses_rx": DrugDispensers.objects.filter(name="pharmacist"),
        }

        for field_name in [
            "where_rx_dispensed",
            "who_dispenses_rx",
        ]:
            with self.subTest(
                f"Testing '{field_name}' is not required",
                field_name=field_name,
            ):
                form_validator = self.validate_form_validator(cleaned_data)
                self.assertIn(field_name, form_validator._errors)
                self.assertIn(
                    "This field is not required",
                    str(form_validator._errors.get(field_name)),
                )
                self.assertEqual(len(form_validator._errors), 1, form_validator._errors)

                # Remove field entry, and move onto testing next field is not required
                cleaned_data[field_name] = None

    def test_card_type_applicable_if_has_hospital_card(self):
        cleaned_data = {
            "subject_visit": self.subject_visit,
            "report_datetime": self.subject_visit.report_datetime,
            "receive_health_talk_messages": NO,
            "additional_health_advice": NO,
            "receive_rx_today": NO,
            "hospital_card": YES,
            "hospital_card_type": NOT_APPLICABLE,
        }
        form_validator = self.validate_form_validator(cleaned_data)
        self.assertIn("hospital_card_type", form_validator._errors)
        self.assertIn(
            "This field is applicable",
            str(form_validator._errors.get("hospital_card_type")),
        )

        # Test no errors when has card, and card type selected
        cleaned_data.update({"hospital_card": YES, "hospital_card_type": "paper_based"})
        form_validator = self.validate_form_validator(cleaned_data)
        self.assertNotIn("hospital_card_type", form_validator._errors)

    def test_card_type_not_applicable_if_no_hospital_card(self):
        cleaned_data = {
            "subject_visit": self.subject_visit,
            "report_datetime": self.subject_visit.report_datetime,
            "receive_health_talk_messages": NO,
            "additional_health_advice": NO,
            "receive_rx_today": NO,
        }
        for answer, _ in YES_NO_DONT_KNOW:
            if answer != YES:
                # Test doesn't error when card type not required, and NOT selected
                cleaned_data.update(
                    {
                        "hospital_card": answer,
                        "hospital_card_type": NOT_APPLICABLE,
                    }
                )
                form_validator = self.validate_form_validator(cleaned_data)
                self.assertNotIn("hospital_card_type", form_validator._errors)

                # Test raises error when card type not required, but IS selected
                cleaned_data.update({"hospital_card_type": "paper_based"})
                form_validator = self.validate_form_validator(cleaned_data)
                self.assertIn("hospital_card_type", form_validator._errors)
                self.assertIn(
                    "This field is not applicable",
                    str(form_validator._errors.get("hospital_card_type")),
                )

    def test_missed_appt_call_applicable_if_has_missed_appt(self):
        cleaned_data = {
            "subject_visit": self.subject_visit,
            "report_datetime": self.subject_visit.report_datetime,
            "receive_health_talk_messages": NO,
            "additional_health_advice": NO,
            "receive_rx_today": NO,
            "hospital_card": NO,
            "missed_appt": YES,
            "missed_appt_call": NOT_APPLICABLE,
        }
        form_validator = self.validate_form_validator(cleaned_data)
        self.assertIn("missed_appt_call", form_validator._errors)
        self.assertIn(
            "This field is applicable",
            str(form_validator._errors.get("missed_appt_call")),
        )

        # Test no errors when has missed appointment, and answered call q
        cleaned_data.update({"missed_appt": YES, "missed_appt_call": YES})
        form_validator = self.validate_form_validator(cleaned_data)
        self.assertNotIn("missed_appt_call", form_validator._errors)

    def test_missed_appt_call_not_applicable_if_not_missed_appt(self):
        cleaned_data = {
            "subject_visit": self.subject_visit,
            "report_datetime": self.subject_visit.report_datetime,
            "receive_health_talk_messages": NO,
            "additional_health_advice": NO,
            "receive_rx_today": NO,
            "hospital_card": NO,
            "missed_appt": NO,
        }
        form_validator = self.validate_form_validator(cleaned_data)
        self.assertNotIn("missed_appt_call", form_validator._errors)

        # Test raises error if completed when not required
        cleaned_data.update({"missed_appt": NO, "missed_appt_call": NO})
        form_validator = self.validate_form_validator(cleaned_data)
        self.assertIn("missed_appt_call", form_validator._errors)
        self.assertIn(
            "This field is not applicable",
            str(form_validator._errors.get("missed_appt_call")),
        )

    def test_who_called_applicable_if_received_missed_visit_call(self):
        cleaned_data = {
            "subject_visit": self.subject_visit,
            "report_datetime": self.subject_visit.report_datetime,
            "receive_health_talk_messages": NO,
            "additional_health_advice": NO,
            "receive_rx_today": NO,
            "hospital_card": NO,
            "missed_appt": YES,
            "missed_appt_call": YES,
            "missed_appt_call_who": NOT_APPLICABLE,
        }
        form_validator = self.validate_form_validator(cleaned_data)
        self.assertIn("missed_appt_call_who", form_validator._errors)
        self.assertIn(
            "This field is applicable",
            str(form_validator._errors.get("missed_appt_call_who")),
        )

        # Test no errors when has missed appointment call, and answered who q
        cleaned_data.update({"missed_appt_call": YES, "missed_appt_call_who": NURSE})
        form_validator = self.validate_form_validator(cleaned_data)
        self.assertNotIn("missed_appt_call_who", form_validator._errors)

    def test_who_called_not_applicable_if_not_received_missed_visit_call(self):
        cleaned_data = {
            "subject_visit": self.subject_visit,
            "report_datetime": self.subject_visit.report_datetime,
            "receive_health_talk_messages": NO,
            "additional_health_advice": NO,
            "receive_rx_today": NO,
            "hospital_card": NO,
            "missed_appt": YES,
            "missed_appt_call": NO,
        }
        form_validator = self.validate_form_validator(cleaned_data)
        self.assertNotIn("missed_appt_call_who", form_validator._errors)

        # Test raises errors if completed when not required
        cleaned_data.update({"missed_appt_call": NO, "missed_appt_call_who": NURSE})
        form_validator = self.validate_form_validator(cleaned_data)
        self.assertIn("missed_appt_call_who", form_validator._errors)
        self.assertIn(
            "This field is not applicable",
            str(form_validator._errors.get("missed_appt_call_who")),
        )

    def test_pay_for_lab_test_applicable_if_had_lab_tests(self):
        cleaned_data = {
            "subject_visit": self.subject_visit,
            "report_datetime": self.subject_visit.report_datetime,
            "receive_health_talk_messages": NO,
            "additional_health_advice": NO,
            "receive_rx_today": NO,
            "hospital_card": NO,
            "missed_appt": NO,
            "lab_tests": YES,
            "pay_for_lab_tests": NOT_APPLICABLE,
        }
        form_validator = self.validate_form_validator(cleaned_data)
        self.assertIn("pay_for_lab_tests", form_validator._errors)
        self.assertIn(
            "This field is applicable",
            str(form_validator._errors.get("pay_for_lab_tests")),
        )

        # Test no errors when had lab tests and pay for q answered
        cleaned_data.update({"lab_tests": YES, "pay_for_lab_tests": NO})
        form_validator = self.validate_form_validator(cleaned_data)
        self.assertNotIn("pay_for_lab_tests", form_validator._errors)

    def test_pay_for_lab_test_not_applicable_if_not_had_lab_tests(self):
        cleaned_data = {
            "subject_visit": self.subject_visit,
            "report_datetime": self.subject_visit.report_datetime,
            "receive_health_talk_messages": NO,
            "additional_health_advice": NO,
            "receive_rx_today": NO,
            "hospital_card": NO,
            "missed_appt": NO,
            "lab_tests": NO,
            "pay_for_lab_tests": NOT_APPLICABLE,
        }
        form_validator = self.validate_form_validator(cleaned_data)
        self.assertNotIn("pay_for_lab_tests", form_validator._errors)

        # Test raises error if completed when not required
        cleaned_data.update({"lab_tests": NO, "pay_for_lab_tests": NO})
        form_validator = self.validate_form_validator(cleaned_data)
        self.assertIn("pay_for_lab_tests", form_validator._errors)
        self.assertIn(
            "This field is not applicable",
            str(form_validator._errors.get("pay_for_lab_tests")),
        )

    def test_follow_up_questions_required_if_paid_for_tests(self):
        cleaned_data = {
            "subject_visit": self.subject_visit,
            "report_datetime": self.subject_visit.report_datetime,
            "receive_health_talk_messages": NO,
            "additional_health_advice": NO,
            "receive_rx_today": NO,
            "hospital_card": NO,
            "missed_appt": NO,
            "lab_tests": YES,
            "pay_for_lab_tests": YES,
        }
        form_validator = self.validate_form_validator(cleaned_data)
        self.assertIn("which_lab_tests_charged_for", form_validator._errors)
        self.assertIn(
            "This field is required",
            str(form_validator._errors.get("which_lab_tests_charged_for")),
        )
        self.assertEqual(len(form_validator._errors), 1, form_validator._errors)

    def test_follow_up_questions_not_required_if_no_lab_tests_or_not_paid_for_tests(self):
        cleaned_data = {
            "subject_visit": self.subject_visit,
            "report_datetime": self.subject_visit.report_datetime,
            "receive_health_talk_messages": NO,
            "additional_health_advice": NO,
            "receive_rx_today": NO,
            "hospital_card": NO,
            "missed_appt": NO,
            "which_lab_tests_charged_for": LaboratoryTests.objects.filter(
                name="blood_pressure_checks"
            ),
        }

        for cd_update in [
            {
                "lab_tests": YES,
                "pay_for_lab_tests": NO,
            },
            {
                "lab_tests": NO,
                "pay_for_lab_tests": NOT_APPLICABLE,
            },
        ]:
            cleaned_data.update(cd_update)

            with self.subTest(
                f"Testing 'which_lab_tests_charged_for' not required for {cd_update}",
            ):
                form_validator = self.validate_form_validator(cleaned_data)
                self.assertIn("which_lab_tests_charged_for", form_validator._errors)
                self.assertIn(
                    "This field is not required",
                    str(form_validator._errors.get("which_lab_tests_charged_for")),
                )
                self.assertEqual(len(form_validator._errors), 1, form_validator._errors)
