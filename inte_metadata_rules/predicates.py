from edc_metadata_rules import PredicateCollection
from django.apps import apps as django_apps

from django.core.exceptions import ObjectDoesNotExist


class Predicates(PredicateCollection):

    app_label = "inte_subject"
    visit_model = "inte_subject.subjectvisit"

    @staticmethod
    def health_economics_required(visit, **kwargs):
        required = False
        if visit.appointment.timepoint >= 0.0:
            model_cls = django_apps.get_model("inte_subject.healtheconomics")
            try:
                model_cls.objects.get(
                    subject_visit__subject_identifier=visit.subject_identifier
                )
            except ObjectDoesNotExist:
                required = True
        return required
