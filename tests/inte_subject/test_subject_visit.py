from dateutil.relativedelta import relativedelta
from django import forms
from django.test import TestCase, override_settings
from edc_constants.constants import STUDY_DEFINED_TIMEPOINT
from edc_utils import get_utcnow
from edc_visit_schedule.constants import DAY1
from edc_visit_tracking.constants import SCHEDULED

from inte_lists.models import ClinicServices, HealthServices
from inte_prn.icc_registered import (
    InterventionSiteNotRegistered,
    is_icc_registered_site,
)
from inte_prn.models import IntegratedCareClinicRegistration
from inte_screening.constants import HIV_CLINIC
from inte_sites.is_intervention_site import NotInterventionSite
from inte_subject.constants import INTEGRATED
from inte_subject.forms.subject_visit_form import SubjectVisitFormValidator
from tests.inte_test_case_mixin import InteTestCaseMixin


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
