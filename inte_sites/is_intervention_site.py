from django.contrib.sites.models import Site
from edc_randomization import RandomizationError
from edc_randomization.models import RandomizationList


class NotInterventionSite(Exception):
    pass


def is_intervention_site(site=None):
    if RandomizationList.objects.all().count() == 0:
        raise RandomizationError("RandomizationList is not loaded.")
    site = site or Site.objects.get_current()
    obj = RandomizationList.objects.filter(site_name=site.name)[0]
    return obj.assignment == "intervention"


def is_intervention_site_or_raise(site=None):
    site = site or Site.objects.get_current()
    if not is_intervention_site(site=site):
        raise NotInterventionSite(f"Not an intervention site. Got {site}")
    return True
