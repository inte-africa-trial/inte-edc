from decimal import Decimal

from edc_metadata_rules import PredicateCollection
from django.apps import apps as django_apps

from django.core.exceptions import ObjectDoesNotExist


class Predicates(PredicateCollection):

    app_label = "inte_subject"
    visit_model = "inte_subject.subjectvisit"

    @staticmethod
    def health_economics_required(visit, **kwargs):
        """Returns True if this is not the baseline visit and
        the CRF has NOT been previously completed.
        """
        required = False
        if visit.appointment.timepoint > Decimal("0.0"):
            model_cls = django_apps.get_model("inte_subject.healtheconomicsrevised")
            try:
                model_cls.objects.get(
                    subject_visit__subject_identifier=visit.subject_identifier
                )
            except ObjectDoesNotExist:
                required = True
        return required

    @staticmethod
    def family_history_required(visit, **kwargs):
        """Returns True if this is not the baseline visit
        and the CRF has NOT been previously completed.
        """
        required = False
        if visit.appointment.timepoint > Decimal("0.0"):
            model_cls = django_apps.get_model("inte_subject.familyhistory")
            if not model_cls.objects.filter(
                subject_visit__subject_identifier=visit.subject_identifier,
            ).exists():
                required = True
        return required
