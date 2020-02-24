# from django.core.exceptions import ObjectDoesNotExist
#
# from .models import GeneralAssessmentInitial
#
#
# class Conditions:
#
#     def __init__(self, subject_identifier=None):
#         try:
#             general_assessment_inital = GeneralAssessmentInitial.objects.get(
#                 subject_visit__subject_identifier=subject_identifier)
#         except ObjectDoesNotExist:
#             pass
#
#     def diabetes(self):
#         return None
#     def hypertension(self):
#         return None
#     def hiv_positive(self):
#         return None
