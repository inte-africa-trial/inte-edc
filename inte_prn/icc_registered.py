from django.contrib.sites.models import Site
from inte_prn.models import IntegratedCareClinicRegistration


def icc_registered():
    return IntegratedCareClinicRegistration.objects.filter(
        site_name=Site.objects.get_current().name
    ).exists()
