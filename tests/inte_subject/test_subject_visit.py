from dateutil.relativedelta import relativedelta
from django import forms
from django.test import TestCase, override_settings
from edc_constants.constants import HIV, NOT_APPLICABLE, OTHER, STUDY_DEFINED_TIMEPOINT
from edc_utils import get_utcnow
from edc_visit_schedule.constants import DAY1, MONTH6, MONTH12
from edc_visit_tracking.constants import MISSED_VISIT, SCHEDULED

from inte_lists.list_data import list_data
from inte_lists.models import ClinicServices, HealthServices
from inte_prn.icc_registered import (
    InterventionSiteNotRegistered,
    is_icc_registered_site,
)
from inte_prn.models import IntegratedCareClinicRegistration
from inte_screening.constants import HIV_CLINIC
from inte_sites.is_intervention_site import NotInterventionSite
from inte_subject.choices import INFO_SOURCE
from inte_subject.constants import INTEGRATED
from inte_subject.forms.subject_visit_form import SubjectVisitFormValidator
from tests.inte_test_case_mixin import InteTestCaseMixin


class TestSubjectVisitFormValidator(InteTestCaseMixin, TestCase):

    form_validator_default_form_cls = SubjectVisitFormValidator

    def setUp(self):
        super().setUp()
        self.baseline_datetime = get_utcnow() - relativedelta(months=1)
        self.subject_screening = self.get_subject_screening(
            report_datetime=self.baseline_datetime, clinic_type=HIV_CLINIC
        )
        self.subject_consent = self.get_subject_consent(
            subject_screening=self.subject_screening,
            clinic_type=HIV_CLINIC,
            report_datetime=self.baseline_datetime,
        )
        self.subject_visit = self.get_subject_visit(
            subject_screening=self.subject_screening,
            subject_consent=self.subject_consent,
            visit_code=DAY1,
        )

    def test_form_validator_allows_missed_visit(self):
        cleaned_data = {
            "appointment": self.subject_visit.appointment,
            "report_datetime": self.subject_visit.report_datetime,
            "reason": MISSED_VISIT,
            "clinic_services": ClinicServices.objects.filter(name=NOT_APPLICABLE),
            "health_services": HealthServices.objects.filter(name=NOT_APPLICABLE),
            "info_source": NOT_APPLICABLE,
        }
        form_validator = self.validate_form_validator(cleaned_data)
        self.assertDictEqual({}, form_validator._errors)

    def test_13m_after_baseline_allows_missed_6m_visit_and_start_12m_visit(self):
        baseline_datetime = get_utcnow() - relativedelta(months=13)
        subject_screening = self.get_subject_screening(
            report_datetime=baseline_datetime, clinic_type=HIV_CLINIC
        )
        subject_consent = self.get_subject_consent(
            subject_screening=subject_screening,
            clinic_type=HIV_CLINIC,
            report_datetime=baseline_datetime,
        )

        # Create (and miss) baseline visit, 13 months ago
        baseline_subject_visit = self.get_subject_visit(
            subject_screening=subject_screening,
            subject_consent=subject_consent,
            visit_code=DAY1,
        )
        cleaned_data = {
            "appointment": baseline_subject_visit.appointment,
            "report_datetime": baseline_subject_visit.report_datetime,
            "reason": MISSED_VISIT,
            "clinic_services": ClinicServices.objects.filter(name=NOT_APPLICABLE),
            "health_services": HealthServices.objects.filter(name=NOT_APPLICABLE),
            "info_source": NOT_APPLICABLE,
        }
        form_validator = self.validate_form_validator(cleaned_data)
        self.assertDictEqual({}, form_validator._errors)

        # Create (and miss) 6m visit, now
        month6_subject_visit = self.get_subject_visit(
            subject_screening=subject_screening,
            subject_consent=subject_consent,
            report_datetime=get_utcnow(),
            visit_code=MONTH6,
        )
        cleaned_data = {
            "appointment": month6_subject_visit.appointment,
            "report_datetime": get_utcnow(),
            "reason": MISSED_VISIT,
            "clinic_services": ClinicServices.objects.filter(name=NOT_APPLICABLE),
            "health_services": HealthServices.objects.filter(name=NOT_APPLICABLE),
            "info_source": NOT_APPLICABLE,
        }
        form_validator = self.validate_form_validator(cleaned_data)
        self.assertDictEqual({}, form_validator._errors)

        # Create (and start) 12m visit, now
        month12_subject_visit = self.get_subject_visit(
            subject_screening=subject_screening,
            subject_consent=subject_consent,
            report_datetime=get_utcnow(),
            visit_code=MONTH12,
        )
        cleaned_data = {
            "appointment": month12_subject_visit.appointment,
            "report_datetime": get_utcnow(),
            "reason": SCHEDULED,
            "clinic_services": ClinicServices.objects.filter(name=STUDY_DEFINED_TIMEPOINT),
            "health_services": HealthServices.objects.filter(name=HIV),
            "info_source": "patient",
        }
        form_validator = self.validate_form_validator(cleaned_data)
        self.assertDictEqual({}, form_validator._errors)

    def test_missed_visit_raises_validation_error_if_clinic_services_not_not_applicable(
        self,
    ):
        cleaned_data = {
            "appointment": self.subject_visit.appointment,
            "report_datetime": self.subject_visit.report_datetime,
            "reason": MISSED_VISIT,
            "health_services": HealthServices.objects.filter(name=NOT_APPLICABLE),
            "info_source": NOT_APPLICABLE,
        }
        for value, _ in list_data["inte_lists.clinicservices"]:
            if value != NOT_APPLICABLE:
                with self.subTest(value=value):
                    cleaned_data.update(
                        {
                            "clinic_services": ClinicServices.objects.filter(name=value),
                        }
                    )
                    if value == OTHER:
                        cleaned_data.update(
                            {"clinic_services_other": "some other clinic service"}
                        )
                    else:
                        cleaned_data.pop("clinic_services_other", None)

                    form_validator = self.validate_form_validator(cleaned_data)
                    self.assertIn("clinic_services", form_validator._errors)
                    self.assertIn(
                        "Expected 'Not applicable' response only "
                        "(if this is a missed visit report).",
                        str(form_validator._errors.get("clinic_services")),
                    )
                    self.assertEqual(len(form_validator._errors), 1, form_validator._errors)

    def test_missed_visit_raises_validation_error_if_health_services_not_not_applicable(
        self,
    ):
        cleaned_data = {
            "appointment": self.subject_visit.appointment,
            "report_datetime": self.subject_visit.report_datetime,
            "reason": MISSED_VISIT,
            "clinic_services": ClinicServices.objects.filter(name=NOT_APPLICABLE),
            "info_source": NOT_APPLICABLE,
        }
        for value, _ in list_data["inte_lists.healthservices"]:
            if value != NOT_APPLICABLE:
                with self.subTest(value=value):
                    cleaned_data.update(
                        {
                            "health_services": HealthServices.objects.filter(name=value),
                        }
                    )
                    form_validator = self.validate_form_validator(cleaned_data)
                    self.assertIn("health_services", form_validator._errors)
                    self.assertIn(
                        "Expected 'Not applicable' response only "
                        "(if this is a missed visit report).",
                        str(form_validator._errors.get("health_services")),
                    )
                    self.assertEqual(len(form_validator._errors), 1, form_validator._errors)

    def test_missed_visit_raises_validation_error_if_info_source_not_not_applicable(
        self,
    ):
        cleaned_data = {
            "appointment": self.subject_visit.appointment,
            "report_datetime": self.subject_visit.report_datetime,
            "reason": MISSED_VISIT,
            "clinic_services": ClinicServices.objects.filter(name=NOT_APPLICABLE),
            "health_services": HealthServices.objects.filter(name=NOT_APPLICABLE),
        }

        for value, _ in INFO_SOURCE:
            if value != NOT_APPLICABLE:
                with self.subTest(value=value):
                    cleaned_data.update({"info_source": value})
                    if value == OTHER:
                        cleaned_data.update(
                            {"info_source_other": "some other information source"}
                        )
                    else:
                        cleaned_data.pop("info_source_other", None)

                    form_validator = self.validate_form_validator(cleaned_data)
                    self.assertIn("info_source", form_validator._errors)
                    self.assertIn(
                        "Expected 'Not applicable' response only "
                        "(if this is a missed visit report).",
                        str(form_validator._errors.get("info_source")),
                    )
                    self.assertEqual(len(form_validator._errors), 1, form_validator._errors)


class TestSubjectVisit(InteTestCaseMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.baseline_datetime = get_utcnow() - relativedelta(months=1)
        self.subject_screening = self.get_subject_screening(
            report_datetime=self.baseline_datetime, clinic_type=HIV_CLINIC
        )
        self.subject_consent = self.get_subject_consent(
            subject_screening=self.subject_screening,
            clinic_type=HIV_CLINIC,
            report_datetime=self.baseline_datetime,
        )

    @override_settings(SITE_ID=101)  # control
    def test_control_site(self):
        self.assertRaises(
            NotInterventionSite,
            is_icc_registered_site,
            report_datetime=get_utcnow(),
        )

    @override_settings(SITE_ID=103)  # intervention
    def test_not_registered_intervention_site(self):

        self.assertRaises(
            InterventionSiteNotRegistered,
            is_icc_registered_site,
            report_datetime=get_utcnow(),
        )

    @override_settings(SITE_ID=103)  # intervention
    def test_icc_opened_by_appt_datetime(self):

        appointment = self.get_appointment(
            subject_identifier=self.subject_consent.subject_identifier,
            visit_code=DAY1,
            visit_code_sequence=0,
            reason=SCHEDULED,
        )
        IntegratedCareClinicRegistration.objects.create(
            report_datetime=appointment.created,
            date_opened=appointment.appt_datetime,
        )
        try:
            is_icc_registered_site(report_datetime=appointment.appt_datetime)
        except InterventionSiteNotRegistered:
            self.fail("InterventionSiteNotRegistered unexpectedly raised")

    @override_settings(SITE_ID=103)  # intervention
    def test_icc_not_opened_by_appt_datetime(self):

        appointment = self.get_appointment(
            subject_identifier=self.subject_consent.subject_identifier,
            visit_code=DAY1,
            visit_code_sequence=0,
            reason=SCHEDULED,
        )
        IntegratedCareClinicRegistration.objects.create(
            report_datetime=appointment.created,
            date_opened=appointment.appt_datetime + relativedelta(days=1),
        )
        self.assertRaises(
            InterventionSiteNotRegistered,
            is_icc_registered_site,
            report_datetime=appointment.appt_datetime,
        )

    @override_settings(SITE_ID=103)  # intervention
    def test_not_registered_intervention_subject_visit_form(self):
        appointment = self.get_appointment(
            subject_identifier=self.subject_consent.subject_identifier,
            visit_code=DAY1,
            visit_code_sequence=0,
            reason=SCHEDULED,
        )
        icc_registration = IntegratedCareClinicRegistration.objects.create(
            report_datetime=appointment.created,
            date_opened=appointment.appt_datetime,
        )
        clinic_services = ClinicServices.objects.filter(name=STUDY_DEFINED_TIMEPOINT)
        health_services = HealthServices.objects.filter(name=INTEGRATED)
        cleaned_data = dict(
            appointment=appointment,
            report_datetime=appointment.appt_datetime,
            clinic_services=clinic_services,
            health_services=health_services,
            reason=SCHEDULED,
        )
        form_validator = SubjectVisitFormValidator(cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertNotIn("health_services", form_validator._errors)

        icc_registration.delete()

        form_validator = SubjectVisitFormValidator(cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn("health_services", form_validator._errors)
