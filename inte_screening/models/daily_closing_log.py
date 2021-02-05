from django.conf import settings
from django.contrib.sites.models import Site
from django.core.validators import MinValueValidator
from django.db import models
from edc_model.models import BaseUuidModel
from edc_model.models.historical_records import HistoricalRecords
from edc_sites.models import CurrentSiteManager, SiteModelMixin
from edc_utils import convert_php_dateformat, get_utcnow

from ..choices import CLINIC_DAYS, SELECTION_METHOD


class DailyClosingLogManager(models.Manager):
    def get_by_natural_key(self, log_identifier):
        return self.get(log_identifier=log_identifier)


class DailyClosingLog(SiteModelMixin, BaseUuidModel):

    site = models.ForeignKey(
        Site,
        on_delete=models.PROTECT,
        null=True,
        related_name="+",
        blank=False,
    )

    log_date = models.DateField(verbose_name="Clinic date", default=get_utcnow)

    clinic_services = models.CharField(
        verbose_name="Which services are being offered at the clinic today?",
        max_length=25,
        choices=CLINIC_DAYS,
    )

    attended = models.IntegerField(
        verbose_name="Total number of patients who attended the clinic today",
        validators=[MinValueValidator(0)],
    )

    selection_method = models.CharField(
        verbose_name="How were patients selected to be approached?",
        max_length=25,
        choices=SELECTION_METHOD,
    )

    approached = models.IntegerField(
        verbose_name="Of those who attended, how many were approached by the study team",
        validators=[MinValueValidator(0)],
    )

    agreed_to_screen = models.IntegerField(
        verbose_name="Of those approached, how many agreed to be screened",
        validators=[MinValueValidator(0)],
    )

    comment = models.TextField(
        verbose_name="Additional Comments",
        null=True,
        blank=True,
    )

    on_site = CurrentSiteManager()

    objects = DailyClosingLogManager()

    history = HistoricalRecords()

    def __str__(self):
        return self.log_date.strftime(convert_php_dateformat(settings.DATE_FORMAT))

    def natural_key(self):
        return (self.log_date, self.site)

    class Meta:
        verbose_name = "Daily Closing Log"
        verbose_name_plural = "Daily Closing Logs"
        constraints = [
            models.UniqueConstraint(fields=["log_date", "site"], name="unique_date_for_site"),
        ]
