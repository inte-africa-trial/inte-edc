from edc_model.models.base_uuid_model import BaseUuidModel
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from edc_constants.choices import YES_NO


DISPENSE_CHOICES = (
    ("fully", "Fully"),
    ("partially", "Partially"),
    ("not_dispensed", "None"),
)


class TreatmentDetailModelMixin(BaseUuidModel):

    dose = models.IntegerField()

    units = models.CharField(max_length=15)

    frequency = models.IntegerField(
        verbose_name="Frequency",
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="per day",
    )

    prescribed = models.CharField(max_length=15, choices=YES_NO)

    dispensed = models.CharField(max_length=15, choices=DISPENSE_CHOICES)

    quantity = models.IntegerField()

    class Meta:
        abstract = True
