from dateutil import rrule
from dateutil.relativedelta import relativedelta
from django.test import TestCase
from edc_appointment.constants import IN_PROGRESS_APPT, INCOMPLETE_APPT, NEW_APPT
from edc_appointment.model_mixins import AppointmentWindowError
from edc_utils import get_utcnow
from edc_visit_schedule.constants import DAY1, MONTH6
from edc_visit_tracking.constants import SCHEDULED, UNSCHEDULED

from inte_screening.constants import HIV_CLINIC
from tests.inte_test_case_mixin import InteTestCaseMixin


def weeks_between(start_date, end_date):
    weeks = rrule.rrule(rrule.WEEKLY, dtstart=start_date, until=end_date)
    return weeks.count()


class TestWindowPeriod(InteTestCaseMixin, TestCase):
    def setUp(self):
        self.baseline_datetime = get_utcnow() - relativedelta(months=6)
        self.subject_screening = self.get_subject_screening(
            report_datetime=self.baseline_datetime,
            clinic_type=HIV_CLINIC,
        )
        self.subject_consent = self.get_subject_consent(
            subject_screening=self.subject_screening,
            consent_datetime=self.baseline_datetime,
            clinic_type=HIV_CLINIC,
        )
        self.appointment_1000 = self.get_appointment(
            subject_identifier=self.subject_consent.subject_identifier,
            visit_code=DAY1,
            visit_code_sequence=0,
            reason=SCHEDULED,
        )

        self.appointment_1060 = self.get_appointment(
            subject_identifier=self.subject_consent.subject_identifier,
            visit_code=MONTH6,
            visit_code_sequence=0,
            reason=SCHEDULED,
        )

    def test_window_period_up_to_6m(self):
        weeks_count = weeks_between(
            self.appointment_1000.appt_datetime,
            self.appointment_1060.appt_datetime,
        )

        subject_visit_baseline = self.get_subject_visit(
            subject_screening=self.subject_screening,
            subject_consent=self.subject_consent,
            report_datetime=self.baseline_datetime,
        )
        subject_visit_baseline.appointment.appt_status = INCOMPLETE_APPT
        subject_visit_baseline.appointment.save()
        subject_visit_baseline.appointment.refresh_from_db()
        subject_visit_baseline.refresh_from_db()

        self.appointment_1060.appt_status = NEW_APPT
        self.appointment_1060.save_base()
        self.appointment_1060.refresh_from_db()
        self.assertFalse(self.appointment_1060.appt_status == IN_PROGRESS_APPT)

        for week in range(1, weeks_count):
            appt_datetime = self.appointment_1000.appt_datetime + relativedelta(weeks=week)
            with self.subTest(week=week, appt_datetime=appt_datetime):
                try:
                    subject_visit = self.get_next_subject_visit(
                        subject_visit=subject_visit_baseline,
                        reason=UNSCHEDULED,
                        appt_datetime=appt_datetime,
                        report_datetime=appt_datetime,
                    )
                except AppointmentWindowError:
                    if appt_datetime < self.appointment_1000.appt_datetime + relativedelta(
                        weeks=22
                    ):
                        self.fail("AppointmentWindowError unexpectedly raised")
                else:
                    if appt_datetime >= self.appointment_1000.appt_datetime + relativedelta(
                        weeks=22
                    ):
                        self.fail("AppointmentWindowError unexpectedly NOT raised")
                subject_visit.appointment.appt_status = INCOMPLETE_APPT
                subject_visit.appointment.save()
                subject_visit.appointment.refresh_from_db()

    def test_window_period_for_6m(self):
        self.appointment_1060.appt_datetime = get_utcnow() - relativedelta(months=1)
        self.appointment_1060.save()
        self.appointment_1060.appt_datetime = get_utcnow() - relativedelta(months=2)
        self.assertRaises(AppointmentWindowError, self.appointment_1060.save)
