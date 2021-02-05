from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView
from edc_dashboard.view_mixins import EdcViewMixin
from edc_navbar import NavbarViewMixin

from inte_prn.models import IntegratedCareClinicRegistration
from inte_sites.is_intervention_site import is_intervention_site


class HomeView(EdcViewMixin, NavbarViewMixin, TemplateView):
    template_name = f"{settings.APP_NAME}/bootstrap{settings.EDC_BOOTSTRAP}/home.html"
    navbar_name = "inte_edc"
    navbar_selected_item = "home"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        icc_registration_outstanding = False
        if is_intervention_site():
            try:
                IntegratedCareClinicRegistration.objects.get(site__id=settings.SITE_ID)
            except ObjectDoesNotExist:
                icc_registration_outstanding = True
        context.update(icc_registration_outstanding=icc_registration_outstanding)
        return context
