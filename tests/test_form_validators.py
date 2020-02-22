from dateutil.relativedelta import relativedelta
from django import forms
from django.test import TestCase, tag
from edc_constants.constants import NO, YES, NOT_APPLICABLE
from edc_utils.date import get_utcnow
from inte_form_validators.form_validators import BaselineCareStatusFormValidator
from pytz import timezone


@tag("form_validators")
class TestBaselineCareStatusFormValidator(TestCase):

    def get_now(self):
        return get_utcnow().astimezone(timezone("Africa/Kampala"))

    def test_ok(self):
        user_input = {
            "hiv": YES,
            "attending_hiv_clinic": YES,
            "use_hiv_clinic_nearby": YES,
            "hiv_next_appt_date": self.get_now(),
            "diabetic": NO,
            "hypertensive": NO,
            "use_ncd_clinic_nearby": NOT_APPLICABLE,
            "attending_ncd_clinic": NOT_APPLICABLE,
            "ncd_next_appt_date": None,
        }

        form_validator = BaselineCareStatusFormValidator(cleaned_data=user_input)
        form_validator.validate()
        self.assertEqual(form_validator._errors, {})

    def test_hiv_pos_attending(self):
        user_input = {
            "enroled_from_clinic": "hiv",
            "hiv": YES,
            "attending_hiv_clinic": YES,
            "use_hiv_clinic_nearby": YES,
            "hiv_next_appt_date": self.get_now(),
        }
        form_validator = BaselineCareStatusFormValidator(cleaned_data=user_input)
        form_validator.validate()
        self.assertEqual(form_validator._errors, {})

    def test_hiv_other_clinic(self):
        user_input = {
            "enroled_from_clinic": "hiv",
            "hiv": YES,
            "attending_hiv_clinic": NOT_APPLICABLE,
            "use_hiv_clinic_nearby": None,
            "hiv_clinic_other": None,
            "hiv_willing_to_transfer": NOT_APPLICABLE,
            "hiv_next_appt_date": None,
        }
        # is HIV positive, expect attending_hiv_clinic
        user_input.update(attending_hiv_clinic=NOT_APPLICABLE)
        form_validator = BaselineCareStatusFormValidator(cleaned_data=user_input)
        self.assertRaises(forms.ValidationError, form_validator.validate)
        self.assertIn("attending_hiv_clinic", form_validator._errors)

        # attending clinic, expect to know if  using nearby clinic
        user_input.update(attending_hiv_clinic=YES)
        form_validator = BaselineCareStatusFormValidator(cleaned_data=user_input)
        self.assertRaises(forms.ValidationError, form_validator.validate)
        self.assertIn("use_hiv_clinic_nearby", form_validator._errors)

        # not using nearby clinic, expect name of remote clinic
        user_input.update(use_hiv_clinic_nearby=NO)
        form_validator = BaselineCareStatusFormValidator(cleaned_data=user_input)
        self.assertRaises(forms.ValidationError, form_validator.validate)
        self.assertIn("hiv_clinic_other", form_validator._errors)

        # provided name of remote clinic, expect intention to transfer (YES/NO)
        user_input.update(hiv_clinic_other="blah blah")
        form_validator = BaselineCareStatusFormValidator(cleaned_data=user_input)
        self.assertRaises(forms.ValidationError, form_validator.validate)
        self.assertIn("hiv_willing_to_transfer", form_validator._errors)

        # attending hiv clinic, expect appt date
        user_input.update(hiv_willing_to_transfer=YES)
        user_input.update(attending_hiv_clinic=YES)
        form_validator = BaselineCareStatusFormValidator(cleaned_data=user_input)
        self.assertRaises(forms.ValidationError, form_validator.validate)
        self.assertIn("hiv_next_appt_date", form_validator._errors)

    def test_ncd_attending(self):
        user_input = {
            "enroled_from_clinic": "ncd",
            "diabetes": NO,
            "hypertension": NO,
        }
        form_validator = BaselineCareStatusFormValidator(cleaned_data=user_input)
        self.assertRaises(forms.ValidationError, form_validator.validate)
        self.assertIn("attending_ncd_clinic", form_validator._errors)
