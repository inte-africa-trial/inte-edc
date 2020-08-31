from django.contrib.sites.models import Site
from edc_utils import get_utcnow
from inte_prn.models import IntegratedCareClinicRegistration
from model_bakery.recipe import Recipe

integratedcareclinicregistration = Recipe(
    IntegratedCareClinicRegistration,
    site=Site.objects.get_current(),
    report_datetime=get_utcnow(),
    date_opened=get_utcnow(),
)
