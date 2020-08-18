from django.contrib.sites.models import Site
from edc_randomization.models import RandomizationList


def is_intervention_site():

    obj = RandomizationList.objects.filter(site_name=Site.objects.get_current().name)[0]

    return obj.assignment == "intervention"
