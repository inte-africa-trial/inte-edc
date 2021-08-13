from django.apps import apps as django_apps
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from edc_metadata.metadata_rules import PredicateCollection
from edc_visit_schedule.constants import MONTH6
from edc_visit_schedule.utils import is_baseline


def get_required_health_economics_model_name(visit):
    """Returns the model name based on the 1060.0 visit
    report_datetime, if possibly required, or none, if not required.

    Neither version is required if ever completed.
    """
    model_name = None
    if visit.appointment.visit_code == MONTH6 and visit.appointment.visit_code_sequence == 0:
        if visit.report_datetime < settings.INTE_SUBJECT_HE_REVISION_DATE:
            model_name = "inte_subject.healtheconomicsrevised"
        else:
            model_name = "inte_subject.healtheconomicsrevisedtwo"
        model_cls = django_apps.get_model(model_name)
        try:
            model_cls.objects.get(subject_visit__subject_identifier=visit.subject_identifier)
        except ObjectDoesNotExist:
            pass
        else:
            model_name = None
    return model_name or ""


class Predicates(PredicateCollection):

    app_label = "inte_subject"
    visit_model = "inte_subject.subjectvisit"

    @staticmethod
    def health_economics_rev_one_required(visit, **kwargs):
        model_name = get_required_health_economics_model_name(visit)
        return model_name == "inte_subject.healtheconomicsrevised"

    @staticmethod
    def health_economics_rev_two_required(visit, **kwargs):
        model_name = get_required_health_economics_model_name(visit)
        return model_name == "inte_subject.healtheconomicsrevisedtwo"

    @staticmethod
    def family_history_required(visit, **kwargs):
        """Returns True if this is not the baseline visit
        and the CRF has NOT been previously completed.
        """
        required = False
        if not is_baseline(visit):
            model_cls = django_apps.get_model("inte_subject.familyhistory")
            if not model_cls.objects.filter(
                subject_visit__subject_identifier=visit.subject_identifier,
            ).exists():
                required = True
        return required
