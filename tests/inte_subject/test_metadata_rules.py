from dateutil.relativedelta import relativedelta
from django.test import TestCase
from edc_appointment.constants import INCOMPLETE_APPT
from edc_constants.constants import NO, NOT_APPLICABLE, POS, YES
from edc_metadata import KEYED, REQUIRED
from edc_metadata.models import CrfMetadata
from edc_utils import get_utcnow
from edc_visit_tracking.constants import UNSCHEDULED
from model_bakery import baker

from inte_screening.constants import HIV_CLINIC
from tests.inte_test_case_mixin import InteTestCaseMixin


class TestMetadataRules(InteTestCaseMixin, TestCase):
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

    @staticmethod
    def get_metadata_models(subject_visit):
        crf_metadatas = CrfMetadata.objects.filter(
            subject_identifier=subject_visit.subject_identifier,
            visit_code=subject_visit.visit_code,
            visit_code_sequence=subject_visit.visit_code_sequence,
        )
        return [
            obj.model
            for obj in crf_metadatas.filter(entry_status__in=[KEYED, REQUIRED]).order_by(
                "model"
            )
        ]

    def test_diagnoses_dates1(self):
        subject_visit_baseline = self.get_subject_visit(
            subject_screening=self.subject_screening,
            subject_consent=self.subject_consent,
            report_datetime=self.baseline_datetime,
        )

        baker.make(
            "inte_subject.clinicalreviewbaseline",
            subject_visit=subject_visit_baseline,
            report_datetime=self.baseline_datetime,
            hiv_test=POS,
            hiv_dx=YES,
            hiv_test_ago="5y",
        )

        baker.make(
            "inte_subject.hivinitialreview",
            subject_visit=subject_visit_baseline,
            report_datetime=self.baseline_datetime,
            dx_ago="5y",
            arv_initiation_ago="4y",
        )

        subject_visit_baseline.appointment.appt_status = INCOMPLETE_APPT
        subject_visit_baseline.appointment.save()
        subject_visit_baseline.appointment.refresh_from_db()
        subject_visit_baseline.refresh_from_db()

        subject_visit = self.get_next_subject_visit(
            subject_visit=subject_visit_baseline,
            reason=UNSCHEDULED,
            report_datetime=self.baseline_datetime + relativedelta(days=14),
        )
        clinical_review = baker.make(
            "inte_subject.clinicalreview",
            subject_visit=subject_visit,
            hiv_test=NOT_APPLICABLE,
            hiv_dx=NOT_APPLICABLE,
            hiv_test_date=None,
            htn_test=NO,
            htn_dx=NOT_APPLICABLE,
            htn_test_date=None,
            dm_test=NO,
            dm_dx=NOT_APPLICABLE,
            dm_test_date=None,
        )
        clinical_review.save()
        models = self.get_metadata_models(subject_visit)
        self.assertIn("inte_subject.hivreview", models)
        self.assertNotIn("inte_subject.hivinitialreview", models)
        self.assertNotIn("inte_subject.htninitialreview", models)
        self.assertNotIn("inte_subject.dminitialreview", models)
        self.assertNotIn("inte_subject.htnreview", models)
        self.assertNotIn("inte_subject.dmreview", models)

    def test_diagnoses_dates2(self):
        subject_visit_baseline = self.get_subject_visit(
            subject_screening=self.subject_screening,
            subject_consent=self.subject_consent,
            report_datetime=self.baseline_datetime,
        )

        baker.make(
            "inte_subject.clinicalreviewbaseline",
            subject_visit=subject_visit_baseline,
            report_datetime=self.baseline_datetime,
            hiv_test=POS,
            hiv_dx=YES,
            hiv_test_ago="5y",
        )

        baker.make(
            "inte_subject.hivinitialreview",
            subject_visit=subject_visit_baseline,
            report_datetime=self.baseline_datetime,
            dx_ago="5y",
            arv_initiation_ago="4y",
        )

        subject_visit_baseline.appointment.appt_status = INCOMPLETE_APPT
        subject_visit_baseline.appointment.save()
        subject_visit_baseline.appointment.refresh_from_db()
        subject_visit_baseline.refresh_from_db()

        subject_visit = self.get_next_subject_visit(
            subject_visit=subject_visit_baseline,
            reason=UNSCHEDULED,
            report_datetime=self.baseline_datetime + relativedelta(days=14),
        )

        clinical_review = baker.make(
            "inte_subject.clinicalreview",
            subject_visit=subject_visit,
            report_datetime=self.baseline_datetime + relativedelta(days=14),
            hiv_test=NOT_APPLICABLE,
            hiv_dx=NOT_APPLICABLE,
            hiv_test_date=None,
            htn_test=NO,
            htn_dx=NOT_APPLICABLE,
            htn_test_date=None,
            dm_test=NO,
            dm_dx=NOT_APPLICABLE,
            dm_test_date=None,
        )

        clinical_review.htn_test = YES
        clinical_review.htn_test_date = subject_visit.report_datetime
        clinical_review.htn_dx = YES
        clinical_review.save()
        clinical_review.refresh_from_db()

        self.assertEqual(NOT_APPLICABLE, clinical_review.hiv_test)

        models = self.get_metadata_models(subject_visit)
        self.assertIn("inte_subject.hivreview", models)
        self.assertIn("inte_subject.htninitialreview", models)
        self.assertNotIn("inte_subject.hivinitialreview", models)
        self.assertNotIn("inte_subject.dminitialreview", models)
        self.assertNotIn("inte_subject.htnreview", models)
        self.assertNotIn("inte_subject.dmreview", models)
