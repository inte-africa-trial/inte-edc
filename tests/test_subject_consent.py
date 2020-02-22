from django.test import TestCase, tag

from .inte_test_case_mixin import InteTestCaseMixin


class TestSubjectConsent(InteTestCaseMixin, TestCase):
    def test_(self):
        subject_screening = self.get_subject_screening()
        subject_consent = self.get_subject_consent(subject_screening)
        self.assertIsNotNone(subject_consent.subject_identifier)
