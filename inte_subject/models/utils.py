from django.core.exceptions import ObjectDoesNotExist

from .diabetes_initial_review import DiabetesInitialReview
from .hiv_initial_review import HivInitialReview
from .hypertension_initial_review import HypertensionInitialReview


def is_hypertensive(subject_identifier):
    try:
        HypertensionInitialReview.objects.get(
            subject_visit__subject_identifier=subject_identifier
        )
    except ObjectDoesNotExist:
        return False
    return True


def is_hiv_pos(subject_identifier):
    try:
        HivInitialReview.objects.get(
            subject_visit__subject_identifier=subject_identifier
        )
    except ObjectDoesNotExist:
        return False
    return True


def is_diabetic(subject_identifier):
    try:
        DiabetesInitialReview.objects.get(
            subject_visit__subject_identifier=subject_identifier
        )
    except ObjectDoesNotExist:
        return False
    return True
