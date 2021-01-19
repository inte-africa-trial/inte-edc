import pdb

from dateutil.relativedelta import relativedelta
from django.test import TestCase, tag
from edc_constants.constants import YES
from edc_utils import get_utcnow
from inte_ae.forms.death_report_form import DeathReportForm, DeathReportFormValidator
from inte_screening.constants import HIV_CLINIC
from model_bakery import baker
from pprint import pprint

from ..inte_test_case_mixin import InteTestCaseMixin


class TestDeathReport(InteTestCaseMixin, TestCase):

    form_validator_default_form_cls = DeathReportFormValidator

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

    @tag("death")
    def test_death_report_form_validator(self):
        self.prepare()
        cleaned_data = {
            "subject_identifier": self.subject_consent.subject_identifier,
            "report_datetime": get_utcnow(),
            "death_date": get_utcnow() - relativedelta(days=5),
            "comment": "",
        }

        form_validator = self.validate_form_validator(cleaned_data)
        self.assertDictEqual({}, form_validator._errors)

    @tag("death")
    def test_death_report_form(self):
        self.prepare()
        cleaned_data = {
            "subject_identifier": self.subject_consent.subject_identifier,
            "report_datetime": get_utcnow(),
            "death_date": get_utcnow() - relativedelta(days=5),
            "comment": "",
        }

        form_validator = self.validate_form_validator(cleaned_data)
        self.assertDictEqual({}, form_validator._errors)

        form = DeathReportForm(data=cleaned_data)
        form.is_valid()
        pdb.set_trace()
