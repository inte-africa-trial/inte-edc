from dateutil.relativedelta import relativedelta
from django.test import TestCase, tag
from edc_action_item.models import ActionItem, ActionType
from edc_constants.constants import NO, OTHER, YES
from edc_utils import get_utcnow
from model_bakery import baker

from inte_ae.action_items import DeathReportAction
from inte_ae.forms.death_report_form import DeathReportForm, DeathReportFormValidator
from inte_screening.constants import HIV_CLINIC

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
            subject_screening=self.subject_screening,
            clinic_type=HIV_CLINIC,
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
            "death_location": "home",
            "hospital_death": NO,
            "informant": "spouse",
            "confirmed_by": "tel",
            "comment": "",
            "narrative": "some narrative",
        }

        form_validator = self.validate_form_validator(cleaned_data)
        self.assertDictEqual({}, form_validator._errors)

        form = DeathReportForm(data=cleaned_data)
        form.is_valid()
        self.assertDictEqual({}, form._errors)

    @tag("death")
    def test_death_report_form_2(self):
        self.prepare()
        action_type = ActionType.objects.get(name=DeathReportAction.name)
        action_item = ActionItem.objects.create(
            subject_identifier=self.subject_consent.subject_identifier,
            action_type=action_type,
            reference_model="inte_ae.deathreport",
        )

        cleaned_data = {
            "action_identifier": action_item.action_identifier,
            "tracking_identifier": action_item.action_identifier,
            "action_item": action_item,
            "subject_identifier": self.subject_consent.subject_identifier,
            "report_datetime": get_utcnow(),
            "death_date": get_utcnow() - relativedelta(days=5),
            # "death_datetime":
            # "study_day":
            "death_as_inpatient": NO,
            "death_location": OTHER,
            "death_location_other": "some location",
            # "cause_of_death":
            "hospital_death": NO,
            "hospital_name": None,
            "informant": OTHER,
            "informant_other": "some informant",
            "confirmed_by": OTHER,
            "confirmed_by_other": "some confirmation",
            "narrative": "some narrative",
        }

        form_validator = self.validate_form_validator(cleaned_data)
        self.assertDictEqual({}, form_validator._errors)

        form = DeathReportForm(data=cleaned_data)
        form.is_valid()

        self.assertDictEqual({}, form._errors)

        form.save(commit=True)
