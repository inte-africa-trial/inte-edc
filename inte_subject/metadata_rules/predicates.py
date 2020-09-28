from django.apps import apps as django_apps
from django.core.exceptions import ObjectDoesNotExist
from edc_metadata_rules import PredicateCollection
from inte_prn.icc_registered import (
    InterventionSiteNotRegistered,
    is_icc_registered_site,
)
from inte_sites.is_intervention_site import NotInterventionSite
from inte_visit_schedule.is_baseline import is_baseline


class Predicates(PredicateCollection):

    app_label = "inte_subject"
    visit_model = "inte_subject.subjectvisit"

    @staticmethod
    def health_economics_required(visit, **kwargs):
        """Returns True if this is not the baseline visit and
        the CRF has NOT been previously completed.
        """
        required = False
        icc_registered = False
        intervention_site = False
        try:
            is_icc_registered_site(
                report_datetime=visit.report_datetime, site=visit.site
            )
        except NotInterventionSite:
            pass
        except InterventionSiteNotRegistered:
            intervention_site = True
        else:
            intervention_site = True
            icc_registered = True

        if not is_baseline(visit) and (
            (intervention_site and icc_registered) or not intervention_site
        ):
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
        if not is_baseline(visit):
            model_cls = django_apps.get_model("inte_subject.familyhistory")
            if not model_cls.objects.filter(
                subject_visit__subject_identifier=visit.subject_identifier,
            ).exists():
                required = True
        return required
