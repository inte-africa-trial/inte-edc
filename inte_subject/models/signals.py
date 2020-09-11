# from django.core.exceptions import ObjectDoesNotExist
# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
# from .general_assessment import GeneralAssessmentInitial
# from .subject_condition_history import SubjectConditionHistory
#
#
# def update_subject_condition_history(instance):
#
#     try:
#         obj = SubjectConditionHistory.objects.get()
#     except ObjectDoesNotExist:
#         obj = SubjectConditionHistory.objects.create()
#
#     obj.diabetes =
#
#
# @receiver(
#     post_save,
#     weak=False,
#     sender=GeneralAssessmentInitial,
#     dispatch_uid="subject_consent_on_post_save",
# )
# def subject_consent_on_post_save(sender, instance, raw, created, **kwargs):
#     """Creates an onschedule instance for this consented subject, if
#     it does not exist.
#     """
#     if not raw:
#         update_subject_condition_history(instance)
