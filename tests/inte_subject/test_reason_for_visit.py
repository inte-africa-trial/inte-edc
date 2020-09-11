# import pdb
#
# from django.test import TestCase, tag
# from edc_constants.constants import (
#     HIV,
#     INCOMPLETE,
#     NO,
#     NOT_APPLICABLE,
#     OTHER,
#     REFILL,
#     YES,
# )
# from edc_utils import get_utcnow
# from inte_lists.models import ClinicServices, HealthServices
# from inte_screening.constants import HIV_CLINIC
# from inte_subject.forms import ReasonForVisitForm
#
# from ..inte_test_case_mixin import InteTestCaseMixin
#
#
# class TestReasonForVisit(InteTestCaseMixin, TestCase):
#     def setUp(self):
#         super().setUp()
#         # hiv clinic
#         self.subject_screening_hiv = self.get_subject_screening(
#             report_datetime=get_utcnow(), clinic_type=HIV_CLINIC
#         )
#         self.subject_consent_hiv = self.get_subject_consent(
#             subject_screening=self.subject_screening_hiv, clinic_type=HIV_CLINIC
#         )
#         self.subject_visit_hiv = self.get_subject_visit(
#             subject_screening=self.subject_screening_hiv,
#             subject_consent=self.subject_consent_hiv,
#         )
#         self.data = {
#             "subject_visit": None,
#             "report_datetime": None,
#             "crf_status": INCOMPLETE,
#             "site": None,
#             "clinic_services": ClinicServices.objects.exclude(name__in=[REFILL, OTHER]),
#             "clinic_services_other": None,
#             "refill_hiv": YES,
#             "refill_dm": NOT_APPLICABLE,
#             "refill_htn": NOT_APPLICABLE,
#             "health_services": HealthServices.objects.filter(name=HIV),
#             "health_services_other": None,
#         }
#
#         self.data.update(
#             subject_visit=self.subject_visit_hiv.pk,
#             report_datetime=self.subject_visit_hiv.report_datetime,
#         )
#
#     def test_ok(self):
#         form = ReasonForVisitForm(data=self.data)
#         form.is_valid()
#         self.assertEqual(form._errors, {})
