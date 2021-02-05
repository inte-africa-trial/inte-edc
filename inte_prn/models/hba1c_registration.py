"""
102
Bwizibwera

105
Kyazanga

111
Kajjansi

115
kasangati

209
Mnazi

210
Sinza

206
Kisarawe

215
Temeke
"""

from django.db import models
from edc_model.models import BaseUuidModel, HistoricalRecords, date_not_future
from edc_protocol.validators import date_not_before_study_start
from edc_sites.models import CurrentSiteManager, SiteModelMixin
from edc_utils.date import get_utcnow

from inte_sites.is_intervention_site import is_intervention_site


class Hba1cRegistrationManagerError(Exception):
    pass


class Hba1cRegistrationManager(models.Manager):
    def get_by_natural_key(self, site_name):
        return self.get(site__name=site_name)


class Hba1cRegistration(SiteModelMixin, BaseUuidModel):

    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time", default=get_utcnow
    )

    date_opened = models.DateField(
        verbose_name="Date integrated clinic opened",
        validators=[date_not_future, date_not_before_study_start],
    )
    on_site = CurrentSiteManager()

    objects = Hba1cRegistrationManager()

    history = HistoricalRecords()

    def __str__(self):
        return f"{self.site.name} opened on {self.date_opened}"

    def save(self, *args, **kwargs):
        if not is_intervention_site():
            raise Hba1cRegistrationManagerError(
                "Registration failed. This site is not included in this substudy. "
                "Perhaps catch this in the form validation."
            )
        super().save(*args, **kwargs)

    def natural_key(self):
        return (self.site.name,)

    class Meta(BaseUuidModel.Meta):
        verbose_name = "HbA1c  Registration"
        verbose_name_plural = "Integrated Care Clinic Registration"
        constraints = [
            models.UniqueConstraint(fields=["site"], name="unique_icc_registration")
        ]
