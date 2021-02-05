from django.contrib.sites.models import Site
from edc_utils import get_utcnow
from model_bakery.recipe import Recipe

from inte_prn.models import IntegratedCareClinicRegistration

integratedcareclinicregistration = Recipe(
    IntegratedCareClinicRegistration,
    site=Site.objects.get_current(),
    report_datetime=get_utcnow(),
    date_opened=get_utcnow(),
)
