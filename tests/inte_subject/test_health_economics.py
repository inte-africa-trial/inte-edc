from django import forms
from django.test import override_settings, TestCase, tag  # noqa
from edc_appointment.constants import INCOMPLETE_APPT
from edc_constants.constants import (
    COMPLETE,
    FREE_OF_CHARGE,
    NOT_APPLICABLE,
    NO,
    OTHER,
    YES,
)
from edc_metadata import REQUIRED
from edc_metadata.models import CrfMetadata
from inte_lists.models import DrugPaySources
from inte_prn.models import IntegratedCareClinicRegistration
from inte_subject.forms import (
    HealthEconomicsRevisedForm,
    HealthEconomicsRevisedFormValidator,
)
from model_bakery import baker


from ..inte_test_case_mixin import InteTestCaseMixin


class TestHealthEconomics(InteTestCaseMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.subject_screening = self.get_subject_screening()
        self.subject_consent = self.get_subject_consent(self.subject_screening)
        self.subject_visit = self.get_subject_visit(
            subject_screening=self.subject_screening,
            subject_consent=self.subject_consent,
        )
        baker.make(
            "inte_subject.clinicalreviewbaseline", subject_visit=self.subject_visit
        )

    @tag("he")
    @override_settings(SITE_ID=103)
    def test_form_validator_requires_icc_registration_for_intervention(self):
        cleaned_data = {
            "subject_visit": self.subject_visit,
            "crf_status": COMPLETE,
            "report_datetime": self.subject_visit.report_datetime,
        }
        form = HealthEconomicsRevisedForm(data=cleaned_data)
        form.is_valid()
        self.assertIn("__all__", form._errors)
        self.assertIn(
            IntegratedCareClinicRegistration._meta.verbose_name,
            ";".join(form._errors.get("__all__")),
        )

    @tag("he")
    @override_settings(SITE_ID=101)
    def test_form_validator_does_not_require_icc_registration_for_control(self):
        cleaned_data = {
            "subject_visit": self.subject_visit,
            "crf_status": COMPLETE,
            "report_datetime": self.subject_visit.report_datetime,
        }
        form = HealthEconomicsRevisedForm(data=cleaned_data)
        form.is_valid()
        self.assertNotIn(
            IntegratedCareClinicRegistration._meta.verbose_name,
            ";".join(form._errors.get("__all__") or []),
        )

    @tag("he")
    def test_form_validator_education(self):
        cleaned_data = {
            "subject_visit": self.subject_visit,
            "crf_status": COMPLETE,
            "report_datetime": self.subject_visit.report_datetime,
            "education_in_years": None,
            "education_certificate": None,
        }
        form_validator = HealthEconomicsRevisedFormValidator(cleaned_data=cleaned_data)
        form_validator.validate()
        self.assertNotIn("education_certificate", form_validator._errors)

        cleaned_data = {
            "subject_visit": self.subject_visit,
            "report_datetime": self.subject_visit.report_datetime,
            "crf_status": COMPLETE,
            "education_in_years": 0,
            "education_certificate": None,
        }
        form_validator = HealthEconomicsRevisedFormValidator(cleaned_data=cleaned_data)
        form_validator.validate()
        self.assertNotIn("education_certificate", form_validator._errors)

        cleaned_data = {
            "subject_visit": self.subject_visit,
            "report_datetime": self.subject_visit.report_datetime,
            "crf_status": COMPLETE,
            "education_in_years": 0,
            "education_certificate": "blah",
        }
        form_validator = HealthEconomicsRevisedFormValidator(cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn("education_certificate", form_validator._errors)

        cleaned_data = {
            "subject_visit": self.subject_visit,
            "report_datetime": self.subject_visit.report_datetime,
            "crf_status": COMPLETE,
            "education_in_years": 1,
            "education_certificate": None,
        }
        form_validator = HealthEconomicsRevisedFormValidator(cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn("education_certificate", form_validator._errors)

        cleaned_data = {
            "subject_visit": self.subject_visit,
            "report_datetime": self.subject_visit.report_datetime,
            "crf_status": COMPLETE,
            "education_in_years": 1,
            "education_certificate": "blah",
        }
        form_validator = HealthEconomicsRevisedFormValidator(cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertNotIn("education_certificate", form_validator._errors)

        # years of education exceeds age
        cleaned_data = {
            "subject_visit": self.subject_visit,
            "report_datetime": self.subject_visit.report_datetime,
            "crf_status": COMPLETE,
            "education_in_years": 100,
            "education_certificate": None,
        }
        form_validator = HealthEconomicsRevisedFormValidator(cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn("education_in_years", form_validator._errors)

    @tag("he")
    def test_form_validator_income(self):
        cleaned_data = {
            "subject_visit": self.subject_visit,
            "report_datetime": self.subject_visit.report_datetime,
            "crf_status": COMPLETE,
            "education_in_years": 10,
            "education_certificate": "secondary",
            "is_highest_earner": NO,
            "highest_earner": None,
        }
        form_validator = HealthEconomicsRevisedFormValidator(cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn("highest_earner", form_validator._errors)

    @tag("he1")
    @override_settings(SITE_ID=103)
    def test_form_validator_expenditure(self):
        baker.make("inte_prn.integratedcareclinicregistration")
        cleaned_data = {
            "subject_visit": self.subject_visit,
            "report_datetime": self.subject_visit.report_datetime,
            "crf_status": COMPLETE,
            "education_in_years": 10,
            "education_certificate": "secondary",
            "is_highest_earner": YES,
            "food_per_month": None,
            "accomodation_per_month": None,
            "large_expenditure_year": None,
        }
        form_validator = HealthEconomicsRevisedFormValidator(cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertDictEqual({}, form_validator._errors)

    @tag("he")
    def test_form_validator_recv_drugs_month(self):
        cleaned_data = {
            "subject_visit": self.subject_visit,
            "report_datetime": self.subject_visit.report_datetime,
            "crf_status": COMPLETE,
            "education_in_years": 10,
            "education_certificate": "secondary",
            "is_highest_earner": YES,
            "food_per_month": None,
            "accomodation_per_month": None,
            "large_expenditure_year": None,
            "received_rx_month": YES,
            "rx_dm_month": NOT_APPLICABLE,
        }
        form_validator = HealthEconomicsRevisedFormValidator(cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn("rx_dm_month", form_validator._errors)

        cleaned_data.update(
            rx_dm_month=YES, rx_dm_paid_month=[],
        )
        form_validator = HealthEconomicsRevisedFormValidator(cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn("rx_dm_paid_month", form_validator._errors)

        # check if "free of charge" then enforces a single selection
        cleaned_data.update(
            rx_dm_month=YES, rx_dm_paid_month=DrugPaySources.objects.all(),
        )
        form_validator = HealthEconomicsRevisedFormValidator(cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn("rx_dm_paid_month", form_validator._errors)

        # check if not "free of charge" then requires cost
        cleaned_data.update(
            rx_dm_month=YES,
            rx_dm_paid_month=DrugPaySources.objects.exclude(
                name__in=[FREE_OF_CHARGE, OTHER]
            ),
        )
        form_validator = HealthEconomicsRevisedFormValidator(cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn("rx_dm_cost_month", form_validator._errors)

        # check if not "free of charge" then requires cost
        cleaned_data.update(
            rx_dm_month=YES,
            rx_dm_paid_month=DrugPaySources.objects.exclude(
                name__in=[FREE_OF_CHARGE, OTHER]
            ),
            rx_dm_cost_month=1000,
        )
        form_validator = HealthEconomicsRevisedFormValidator(cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertNotIn("rx_dm_paid_month", form_validator._errors)
        self.assertNotIn("rx_dm_cost_month", form_validator._errors)
        self.assertNotIn("rx_dm_paid_month_other", form_validator._errors)

        # check other
        cleaned_data.update(
            rx_dm_month=YES,
            rx_dm_paid_month=DrugPaySources.objects.filter(name=OTHER),
            rx_dm_cost_month=1000,
        )
        form_validator = HealthEconomicsRevisedFormValidator(cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn("rx_dm_paid_month_other", form_validator._errors)

    @tag("he")
    def test_form_validator_recv_drugs_all_no(self):
        cleaned_data = {
            "subject_visit": self.subject_visit,
            "report_datetime": self.subject_visit.report_datetime,
            "crf_status": COMPLETE,
            "education_in_years": 10,
            "education_certificate": "secondary",
            "is_highest_earner": YES,
            "food_per_month": None,
            "accomodation_per_month": None,
            "large_expenditure_year": None,
            "received_rx_month": NO,
            "rx_dm_month": NOT_APPLICABLE,
            "rx_htn_month": NOT_APPLICABLE,
            "rx_hiv_month": NOT_APPLICABLE,
            "rx_other_month": NOT_APPLICABLE,
        }

        cleaned_data.update(
            {
                "received_rx_today": YES,
                "rx_dm_today": NO,
                "rx_htn_today": NO,
                "rx_hiv_today": NO,
                "rx_other_today": NO,
            }
        )
        form_validator = HealthEconomicsRevisedFormValidator(cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn("received_rx_today", form_validator._errors)

        cleaned_data.update(
            {
                "received_rx_today": YES,
                "rx_dm_today": NOT_APPLICABLE,
                "rx_htn_today": NO,
                "rx_hiv_today": NO,
                "rx_other_today": NO,
            }
        )
        form_validator = HealthEconomicsRevisedFormValidator(cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn("rx_dm_today", form_validator._errors)

    @tag("he")
    def test_form_validator_non_drug_activities(self):
        cleaned_data = {
            "subject_visit": self.subject_visit,
            "report_datetime": self.subject_visit.report_datetime,
            "crf_status": COMPLETE,
            "education_in_years": 10,
            "education_certificate": "secondary",
            "is_highest_earner": YES,
            "food_per_month": None,
            "accomodation_per_month": None,
            "large_expenditure_year": None,
            "received_rx_month": NO,
            "rx_dm_month": NOT_APPLICABLE,
            "rx_htn_month": NOT_APPLICABLE,
            "rx_hiv_month": NOT_APPLICABLE,
            "rx_other_month": NOT_APPLICABLE,
            "received_rx_today": NO,
            "rx_dm_today": NOT_APPLICABLE,
            "rx_htn_today": NOT_APPLICABLE,
            "rx_hiv_today": NOT_APPLICABLE,
            "rx_other_today": NOT_APPLICABLE,
        }

        cleaned_data.update(
            {
                "non_drug_activities_month": YES,
                "non_drug_activities_detail_month": None,
                "non_drug_activities_cost_month": None,
            }
        )
        form_validator = HealthEconomicsRevisedFormValidator(cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn("non_drug_activities_detail_month", form_validator._errors)

        cleaned_data.update(
            {
                "non_drug_activities_month": YES,
                "non_drug_activities_detail_month": "blah",
                "non_drug_activities_cost_month": None,
            }
        )
        form_validator = HealthEconomicsRevisedFormValidator(cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn("non_drug_activities_cost_month", form_validator._errors)

        cleaned_data.update(
            {
                "non_drug_activities_month": YES,
                "non_drug_activities_detail_month": "blah",
                "non_drug_activities_cost_month": 10,
            }
        )
        form_validator = HealthEconomicsRevisedFormValidator(cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertDictEqual({}, form_validator._errors)

    @tag("he")
    def test_not_required_at_baseline(self):
        crfs = CrfMetadata.objects.filter(
            subject_identifier=self.subject_visit.subject_identifier,
            visit_code=self.subject_visit.visit_code,
            visit_code_sequence=self.subject_visit.visit_code_sequence,
            entry_status=REQUIRED,
        )
        self.assertNotIn(
            "inte_subject.healtheconomicsrevised", [o.model for o in crfs.all()]
        )
        self.subject_visit.save()
        crfs = CrfMetadata.objects.filter(
            subject_identifier=self.subject_visit.subject_identifier,
            visit_code=self.subject_visit.visit_code,
            visit_code_sequence=self.subject_visit.visit_code_sequence,
            entry_status=REQUIRED,
        )
        self.assertNotIn(
            "inte_subject.healtheconomicsrevised", [o.model for o in crfs.all()]
        )

    @tag("he")
    def test_required_at_next_visit(self):
        self.subject_visit.appointment.appt_status = INCOMPLETE_APPT
        self.subject_visit.appointment.save()
        self.subject_visit.appointment.refresh_from_db()

        subject_visit = self.get_subject_visit(
            subject_screening=self.subject_screening,
            subject_consent=self.subject_consent,
            visit_code=self.subject_visit.appointment.next.visit_code,
        )

        crfs = CrfMetadata.objects.filter(
            subject_identifier=subject_visit.subject_identifier,
            visit_code=subject_visit.visit_code,
            visit_code_sequence=subject_visit.visit_code_sequence,
            entry_status=REQUIRED,
        )
        self.assertIn(
            "inte_subject.healtheconomicsrevised", [o.model for o in crfs.all()]
        )

    @tag("he")
    def test_not_required_at_next_visit_if_completed_previously(self):
        self.subject_visit.appointment.appt_status = INCOMPLETE_APPT
        self.subject_visit.appointment.save()
        self.subject_visit.appointment.refresh_from_db()

        subject_visit = self.get_subject_visit(
            subject_screening=self.subject_screening,
            subject_consent=self.subject_consent,
            visit_code=self.subject_visit.appointment.next.visit_code,
        )

        baker.make("inte_subject.healtheconomicsrevised", subject_visit=subject_visit)

        subject_visit.appointment.appt_status = INCOMPLETE_APPT
        subject_visit.appointment.save()
        subject_visit.appointment.refresh_from_db()

        subject_visit = self.get_subject_visit(
            subject_screening=self.subject_screening,
            subject_consent=self.subject_consent,
            visit_code=subject_visit.appointment.next.visit_code,
        )
        crfs = CrfMetadata.objects.filter(
            subject_identifier=subject_visit.subject_identifier,
            visit_code=subject_visit.visit_code,
            visit_code_sequence=subject_visit.visit_code_sequence,
            entry_status=REQUIRED,
        )
        self.assertNotIn(
            "inte_subject.healtheconomicsrevised", [o.model for o in crfs.all()]
        )
