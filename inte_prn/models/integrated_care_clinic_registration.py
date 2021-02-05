from django.db import models
from edc_model.models import BaseUuidModel, HistoricalRecords, date_not_future
from edc_protocol.validators import date_not_before_study_start
from edc_sites.models import CurrentSiteManager, SiteModelMixin
from edc_utils.date import get_utcnow

from inte_sites.is_intervention_site import is_intervention_site


class IntegratedCareClinicRegistrationError(Exception):
    pass


class IntegratedCareClinicRegistrationManager(models.Manager):
    def get_by_natural_key(self, site_name):
        return self.get(site__name=site_name)


class IntegratedCareClinicRegistration(SiteModelMixin, BaseUuidModel):

    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time", default=get_utcnow
    )

    date_opened = models.DateField(
        verbose_name="Date integrated clinic opened",
        validators=[date_not_future, date_not_before_study_start],
    )

    comment = models.TextField(
        verbose_name=(
            "Please give a brief summary of the opportunities "
            "and challenges in getting this clinic open."
        ),
        null=True,
        blank=True,
        help_text="Optional",
    )

    on_site = CurrentSiteManager()

    objects = IntegratedCareClinicRegistrationManager()

    history = HistoricalRecords()

    def __str__(self):
        return f"{self.site.name} opened on {self.date_opened}"

    def save(self, *args, **kwargs):
        if not is_intervention_site():
            raise IntegratedCareClinicRegistrationError(
                "Registration failed. This is not an intervention site. "
                "Perhaps catch this in the form validation."
            )
        super().save(*args, **kwargs)

    def natural_key(self):
        return (self.site.name,)

    class Meta(BaseUuidModel.Meta):
        verbose_name = "Integrated Care Clinic Registration"
        verbose_name_plural = "Integrated Care Clinic Registration"
        constraints = [
            models.UniqueConstraint(fields=["site"], name="unique_icc_registration")
        ]
