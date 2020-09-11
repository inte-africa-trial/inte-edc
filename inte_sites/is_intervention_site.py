from django.contrib.sites.models import Site
from edc_randomization import RandomizationError
from edc_randomization.models import RandomizationList


def is_intervention_site():
    if RandomizationList.objects.all().count() == 0:
        raise RandomizationError("RandomizationList is not loaded.")
    obj = RandomizationList.objects.filter(site_name=Site.objects.get_current().name)[0]
    return obj.assignment == "intervention"
