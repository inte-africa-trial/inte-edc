from django.db import models
from django.db.models import PROTECT
from edc_adverse_event.model_mixins import DeathReportModelMixin
from edc_adverse_event.models import CauseOfDeath
from edc_constants.choices import YES_NO
from edc_model import models as edc_models
from edc_model_fields.fields import OtherCharField

from inte_ae.choices import CONTACT, DEATH_LOCATIONS, INFORMANT


class DeathReport(DeathReportModelMixin, edc_models.BaseUuidModel):

    death_date_field = "death_date"

    death_location = models.CharField(
        verbose_name="Where did the participant die?",
        max_length=50,
        choices=DEATH_LOCATIONS,
    )

    death_location_other = OtherCharField()

    hospital_death = models.CharField(
        verbose_name=(
            "Did the participant die in hospital, or die just after " "visiting a hospital?"
        ),
        max_length=50,
        choices=YES_NO,
    )

    hospital_name = models.CharField(
        verbose_name="Which hospital was this", max_length=50, null=True, blank=True
    )

    informant = models.CharField(
        verbose_name="Who has confirmed that the participant has died?",
        max_length=50,
        choices=INFORMANT,
    )

    informant_other = OtherCharField()

    confirmed_by = models.CharField(
        verbose_name="How was this confirmed?",
        max_length=50,
        choices=CONTACT,
    )

    confirmed_by_other = OtherCharField()

    narrative = models.TextField(
        verbose_name="Comment",
        null=True,
        blank=False,
        help_text="Provide any additional details, if relevant",
    )

    # override to set editable=False
    study_day = models.IntegerField(
        verbose_name="Study day",
        null=True,
        editable=False,
        help_text="This field is not used",
    )

    # override to set editable=False
    cause_of_death = models.ForeignKey(
        CauseOfDeath,
        on_delete=PROTECT,
        verbose_name="Main cause of death",
        help_text=(
            "Main cause of death in the opinion of the " "local study doctor and local PI"
        ),
        null=True,
        editable=False,
    )

    @property
    def death_datetime(self):
        return self.death_date

    class Meta(DeathReportModelMixin.Meta, edc_models.BaseUuidModel.Meta):
        pass
