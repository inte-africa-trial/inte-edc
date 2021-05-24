from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.views.generic import TemplateView
from edc_dashboard.view_mixins import EdcViewMixin
from edc_navbar import NavbarViewMixin
from edc_utils import get_utcnow

from inte_prn.models import IntegratedCareClinicRegistration
from inte_screening.models.daily_closing_log_revised import get_daily_log_revision_date
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
        context.update(
            icc_registration_outstanding=icc_registration_outstanding,
            daily_closing_log_url=self.get_daily_closing_log_url(),
        )
        return context

    @staticmethod
    def get_daily_closing_log_url():

        if get_utcnow().date() >= get_daily_log_revision_date():
            return reverse(
                "inte_screening_admin:inte_screening_dailyclosinglogrevised_changelist"
            )
        return reverse("inte_screening_admin:inte_screening_dailyclosinglog_changelist")
