from pprint import pprint

from dateutil.relativedelta import relativedelta
from django.forms import ValidationError
from django.test import TestCase, tag
from edc_action_item.models import ActionItem, ActionType
from edc_constants.constants import YES
from edc_utils import get_utcnow
from model_bakery import baker

from inte_ae.models import DeathReport
from inte_prn.form_validators import EndOfStudyFormValidator
from inte_screening.constants import HIV_CLINIC
from inte_visit_schedule.constants import SCHEDULE_HIV

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

    @tag("d")
    def test_eos_death(self):
        self.prepare()
        now = get_utcnow()
        action_type = ActionType.objects.get(name=DeathReport.action_name)
        action_item = ActionItem.objects.create(
            subject_identifier=self.subject_consent.subject_identifier,
            action_type=action_type,
            reference_model="inte_ae.deathreport",
        )

        baker.make(
            "inte_ae.deathreport",
            subject_identifier=self.subject_consent.subject_identifier,
            action_identifier=action_item.action_identifier,
            death_date=now - relativedelta(days=5),
        )
        cleaned_data = {
            "subject_identifier": self.subject_consent.subject_identifier,
            "report_datetime": now,
            "visit_schedule": "visit_schedule",
            "schedule_name": SCHEDULE_HIV,
            "death_date": now - relativedelta(days=5),
            "comment": "",
        }
        form_validator = EndOfStudyFormValidator(cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            pprint(form_validator._errors)
            self.fail("ValidationError unexpectedly raised.")
