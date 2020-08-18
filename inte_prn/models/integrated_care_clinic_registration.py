from django.db import models
from edc_model.models import HistoricalRecords
from edc_model.models.base_uuid_model import BaseUuidModel
from edc_sites.models import CurrentSiteManager, SiteModelMixin
from edc_utils.date import get_utcnow


class IntegratedCareClinicRegistrationManager(models.Manager):
    def get_by_natural_key(self, site_name):
        return self.get(site__name=site_name)


class IntegratedCareClinicRegistration(SiteModelMixin, BaseUuidModel):

    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time", default=get_utcnow
    )

    date_opened = models.DateField(verbose_name="Date integrated clinic opened")

    comment = models.TextField(
        verbose_name=(
            "Please give a brief summary of the opportunities and challenges in getting this clinic open."
        ),
        null=True,
        blank=False,
        help_text="Optional",
    )

    on_site = CurrentSiteManager()

    objects = IntegratedCareClinicRegistrationManager()

    history = HistoricalRecords()

    def __str__(self):
        return f"{self.site.name} opened on {self.date_opened}"

    def natural_key(self):
        return (self.site.name,)

    class Meta(BaseUuidModel.Meta):
        verbose_name = "Integrated Care Clinic Registration"
        verbose_name_plural = "Integrated Care Clinic Registration"
        constraints = [
            models.UniqueConstraint(fields=["site"], name="unique_icc_registration")
        ]
