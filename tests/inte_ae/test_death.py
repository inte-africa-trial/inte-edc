from dateutil.relativedelta import relativedelta
from django.forms import ValidationError
from django.test import override_settings, TestCase, tag
from edc_constants.constants import INCOMPLETE, YES
from edc_utils import get_utcnow
from inte_prn.models import IntegratedCareClinicRegistration
from inte_screening.constants import HIV_CLINIC
from inte_subject.forms import NextAppointmentForm
from inte_subject.forms.next_appointment_form import NextAppointmentFormValidator
from tests.inte_test_case_mixin import InteTestCaseMixin
from model_bakery import baker


class TestNextAppointment(InteTestCaseMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.subject_screening = self.get_subject_screening(
            report_datetime=get_utcnow(), clinic_type=HIV_CLINIC
        )
        self.subject_consent = self.get_subject_consent(
            subject_screening=self.subject_screening, clinic_type=HIV_CLINIC
        )

    def test_death(self):
        Death
