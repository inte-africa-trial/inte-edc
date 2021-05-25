from django import forms
from django.test import TestCase, override_settings

from inte_subject.forms.mixins import (
    raise_if_intervention_site_without_icc_registration,
)
from tests.inte_test_case_mixin import InteTestCaseMixin


class TestFormMixins(InteTestCaseMixin, TestCase):
    @override_settings(SITE_ID=103)
    def test_raises_form_validation_error_for_intervention_site_without_icc_registration(self):
        self.assertRaises(
            forms.ValidationError, raise_if_intervention_site_without_icc_registration
        )

    def test_does_not_raise_form_validation_error_for_intervention_site_with_icc_registration(
        self,
    ):
        try:
            raise_if_intervention_site_without_icc_registration()
        except forms.ValidationError:
            self.fail("Did not expect a forms.ValidationError!")

    @override_settings(SITE_ID=101)
    def test_does_not_raise_form_validation_error_for_control_site(self):
        try:
            raise_if_intervention_site_without_icc_registration()
        except forms.ValidationError:
            self.fail("Did not expect a forms.ValidationError!")
