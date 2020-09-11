from django.test import TestCase, tag

from ..visit_schedules.schedule import schedule_hiv, schedule_ncd
from ..visit_schedules.visit_schedule import visit_schedule


class TestVisitSchedule(TestCase):
    def test_visit_schedule_models(self):
        self.assertEqual(visit_schedule.death_report_model, "inte_ae.deathreport")
        self.assertEqual(visit_schedule.offstudy_model, "edc_offstudy.subjectoffstudy")
        self.assertEqual(visit_schedule.locator_model, "edc_locator.subjectlocator")

    def test_schedule_hiv_models(self):
        self.assertEqual(schedule_hiv.onschedule_model, "inte_prn.onschedulehiv")
        self.assertEqual(schedule_hiv.offschedule_model, "inte_prn.endofstudy")
        self.assertEqual(schedule_hiv.consent_model, "inte_consent.subjectconsent")
        self.assertEqual(schedule_hiv.appointment_model, "edc_appointment.appointment")

    def test_schedule_ncd_models(self):
        self.assertEqual(schedule_ncd.onschedule_model, "inte_prn.onschedulencd")
        self.assertEqual(schedule_ncd.offschedule_model, "inte_prn.endofstudy")
        self.assertEqual(schedule_ncd.consent_model, "inte_consent.subjectconsent")
        self.assertEqual(schedule_ncd.appointment_model, "edc_appointment.appointment")

    def test_visit_codes_hiv(self):
        self.assertEqual(
            ["1000", "1030", "1060", "1090", "1120"],
            [visit for visit in schedule_ncd.visits],
        )

    def test_visit_codes_ncd(self):
        self.assertEqual(
            [
                "1000",
                "1010",
                "1030",
                "1040",
                "1050",
                "1060",
                "1070",
                "1080",
                "1090",
                "1100",
                "1110",
                "1120",
            ],
            [visit for visit in schedule_ncd.visits],
        )

    def test_crfs(self):
        prn = [
            "inte_subject.bloodresultsfbc",
            "inte_subject.bloodresultsglu",
            "inte_subject.bloodresultshba1c",
            "inte_subject.bloodresultslft",
            "inte_subject.bloodresultsrft",
            "inte_subject.urinedipsticktest",
        ]
        expected = {
            "1000": [
                "inte_subject.physicalexam",
                "inte_subject.patienthistory",
                "inte_subject.bloodresultsfbc",
                "inte_subject.bloodresultslft",
                "inte_subject.bloodresultsrft",
                "inte_subject.urinedipsticktest",
            ],
            "1005": [
                "inte_subject.followupvitals",
                "inte_subject.followup",
                "inte_subject.clinicalreviewbaseline",
                "inte_subject.medicationadherence",
            ],
            "1010": [
                "inte_subject.followupvitals",
                "inte_subject.followup",
                "inte_subject.medicationadherence",
            ],
            "1030": [
                "inte_subject.bloodresultslft",
                "inte_subject.bloodresultsrft",
                "inte_subject.followupvitals",
                "inte_subject.followup",
                "inte_subject.medicationadherence",
            ],
            "1060": [
                "inte_subject.bloodresultshba1c",
                "inte_subject.bloodresultslft",
                "inte_subject.bloodresultsrft",
                "inte_subject.followupvitals",
                "inte_subject.followup",
                "inte_subject.medicationadherence",
            ],
            "1090": [
                "inte_subject.bloodresultslft",
                "inte_subject.bloodresultsrft",
                "inte_subject.followupvitals",
                "inte_subject.followup",
                "inte_subject.medicationadherence",
            ],
            "1120": [
                "inte_subject.bloodresultsfbc",
                "inte_subject.bloodresultsglu",
                "inte_subject.bloodresultshba1c",
                "inte_subject.bloodresultslft",
                "inte_subject.bloodresultsrft",
                "inte_subject.followupvitals",
                "inte_subject.followup",
                "inte_subject.medicationadherence",
                "inte_subject.urinedipsticktest",
            ],
        }
        for visit_code, visit in schedule_hiv.visits.items():
            actual = [crf.model for crf in visit.crfs]
            actual.sort()
            expected.get(visit_code).sort()
            self.assertEqual(
                expected.get(visit_code), actual, msg=f"see CRFs for visit {visit_code}"
            )

            actual = [crf.model for crf in visit.crfs_prn]
            actual.sort()
            self.assertEqual(prn, actual, msg=f"see PRN CRFs for visit {visit_code}")
