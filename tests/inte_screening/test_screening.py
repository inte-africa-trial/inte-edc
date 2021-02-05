from django.test import TestCase, tag
from edc_constants.constants import MALE, NO, NOT_APPLICABLE, RANDOM_SAMPLING, YES
from edc_utils.date import get_utcnow

from inte_screening.constants import NCD_CLINIC
from inte_screening.forms import SubjectScreeningForm
from inte_screening.models import SubjectScreening


class TestForms(TestCase):
    def get_data(self):
        return {
            "screening_consent": YES,
            "selection_method": RANDOM_SAMPLING,
            "report_datetime": get_utcnow(),
            "initials": "EW",
            "gender": MALE,
            "age_in_years": 25,
            "clinic_type": NCD_CLINIC,
            "qualifying_condition": YES,
            "lives_nearby": YES,
            "requires_acute_care": NO,
            "unsuitable_for_study": NO,
            "unsuitable_agreed": NOT_APPLICABLE,
        }

    def test_screening_ok(self):

        form = SubjectScreeningForm(data=self.get_data(), instance=None)
        form.is_valid()
        self.assertEqual(form._errors, {})
        form.save()
        self.assertTrue(SubjectScreening.objects.all()[0].eligible)

    def test_screening_invalid(self):

        data = self.get_data()

        responses = dict(
            age_in_years=17,
        )

        for k, v in responses.items():
            with self.subTest(k=v):
                data.update({k: v})
                form = SubjectScreeningForm(data=data, instance=None)
                form.is_valid()
                self.assertIn("age_in_years", form._errors)

    def test_screening_ineligible(self):

        data = self.get_data()

        responses = dict(
            qualifying_condition=NO,
            lives_nearby=NO,
            requires_acute_care=YES,
        )

        for k, v in responses.items():
            with self.subTest(k=v):
                data.update({k: v})
                form = SubjectScreeningForm(data=data, instance=None)
                form.is_valid()
                self.assertEqual(form._errors, {})
                form.save()

                self.assertFalse(SubjectScreening.objects.all()[0].eligible)

    def test_screening_unsuitable(self):

        data = self.get_data()

        data.update(unsuitable_for_study=YES)
        form = SubjectScreeningForm(data=data, instance=None)
        form.is_valid()
        self.assertIn("reasons_unsuitable", form._errors)

        data.update(reasons_unsuitable="blah blah")
        form = SubjectScreeningForm(data=data, instance=None)
        form.is_valid()
        self.assertIn("unsuitable_agreed", form._errors)

        data.update(unsuitable_agreed=NO)
        form = SubjectScreeningForm(data=data, instance=None)
        form.is_valid()
        self.assertIn("unsuitable_agreed", form._errors)

        data.update(unsuitable_agreed=YES)
        form = SubjectScreeningForm(data=data, instance=None)
        form.is_valid()
        form.save()
        self.assertFalse(SubjectScreening.objects.all()[0].eligible)
