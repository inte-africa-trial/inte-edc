from dateutil.relativedelta import relativedelta
from django.forms import ValidationError
from django.test import TestCase, override_settings
from edc_constants.constants import INCOMPLETE, YES
from edc_utils import get_utcnow
from model_bakery import baker

from inte_prn.models import IntegratedCareClinicRegistration
from inte_screening.constants import HIV_CLINIC
from inte_subject.forms import NextAppointmentForm
from inte_subject.forms.next_appointment_form import NextAppointmentFormValidator
from tests.inte_test_case_mixin import InteTestCaseMixin


class TestNextAppointment(InteTestCaseMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.subject_screening = None
        self.subject_consent = None
        self.subject_visit = None
        self.baseline_datetime = get_utcnow() - relativedelta(months=1)

    def prepare(self):
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
            report_datetime=self.baseline_datetime,
        )
        baker.make(
            "inte_subject.clinicalreviewbaseline",
            subject_visit=self.subject_visit,
            report_datetime=self.baseline_datetime,
            hiv_test=YES,
            hiv_dx=YES,
            hiv_test_ago="5y",
        )
        baker.make(
            "inte_subject.hivinitialreview",
            subject_visit=self.subject_visit,
            report_datetime=self.baseline_datetime,
            dx_date=get_utcnow() - relativedelta(years=5),
            arv_initiation_ago="4y",
        )

    def test_next_appointment_vertical(self):
        self.prepare()
        data = {
            "subject_visit": self.subject_visit,
            "report_datetime": self.subject_visit.report_datetime,
            "crf_status": INCOMPLETE,
        }
        form = NextAppointmentForm(data=data)
        form.is_valid()
        self.assertIn("hiv_clinic_appt_date", form._errors)

    @override_settings(SITE_ID=103)
    def test_next_appointment_integrated_raises(self):
        self.prepare()
        IntegratedCareClinicRegistration.objects.create(
            report_datetime=get_utcnow(),
            date_opened=get_utcnow(),
        )
        cleaned_data = {
            "subject_visit": self.subject_visit,
            "hiv_clinic_appt_date": None,
            "htn_clinic_appt_date": None,
            "dm_clinic_appt_date": None,
            "integrated_clinic_appt_date": None,
            "report_datetime": self.subject_visit.report_datetime,
            "crf_status": INCOMPLETE,
        }
        form_validator = NextAppointmentFormValidator(cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError:
            self.assertIn("integrated_clinic_appt_date", form_validator._errors)
            self.assertNotIn("hiv_clinic_appt_date", form_validator._errors)
            self.assertNotIn("htn_clinic_appt_date", form_validator._errors)
            self.assertNotIn("dm_clinic_appt_date", form_validator._errors)
        else:
            self.fail("ValidationError unexpectedly NOT raised.")

    @override_settings(SITE_ID=103)
    def test_next_appointment_integrated_does_not_raise(self):
        self.prepare()
        IntegratedCareClinicRegistration.objects.create(
            report_datetime=self.baseline_datetime,
            date_opened=self.baseline_datetime,
        )
        cleaned_data = {
            "subject_visit": self.subject_visit,
            "hiv_clinic_appt_date": None,
            "htn_clinic_appt_date": None,
            "dm_clinic_appt_date": None,
            "integrated_clinic_appt_date": get_utcnow(),
            "report_datetime": self.subject_visit.report_datetime,
            "crf_status": INCOMPLETE,
        }
        form_validator = NextAppointmentFormValidator(cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError:
            self.fail("ValidationError unexpectedly raised.")
        else:
            self.assertNotIn("hiv_clinic_appt_date", form_validator._errors)
            self.assertNotIn("htn_clinic_appt_date", form_validator._errors)
            self.assertNotIn("dm_clinic_appt_date", form_validator._errors)
