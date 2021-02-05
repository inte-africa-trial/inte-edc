from arrow import Arrow
from django.apps import apps as django_apps
from django.contrib.sites.models import Site
from django.core.exceptions import ObjectDoesNotExist

from inte_sites.is_intervention_site import is_intervention_site_or_raise

from .models import IntegratedCareClinicRegistration


class InterventionSiteNotRegistered(Exception):
    pass


def icc_registered(report_datetime=None):
    report_datetime_utc = Arrow.fromdatetime(report_datetime)
    return IntegratedCareClinicRegistration.objects.filter(
        site=Site.objects.get_current(),
        date_opened__gte=report_datetime_utc.date(),
    ).exists()


def is_icc_registered_site(report_datetime=None, report_date=None, site=None):
    """Returns True if site is an open intervention site or raises.

    Raises if NOT an intervention site or is an NOT intervention
    with an ICC registration form submitted by this report_datetime.
    """

    if report_datetime:
        report_date_utc = Arrow.fromdatetime(report_datetime).date()
    elif report_date:
        report_date_utc = Arrow.fromdate(report_date).date()
    site = site or Site.objects.get_current()
    if is_intervention_site_or_raise(site=site):
        model_cls = django_apps.get_model("inte_prn.integratedcareclinicregistration")
        try:
            model_cls.objects.get(
                site=site,
                date_opened__lte=report_date_utc,
            )
        except ObjectDoesNotExist:
            raise InterventionSiteNotRegistered(
                f"Site's ICC registration not found.  Got `{site.name}`."
            )
    return True
