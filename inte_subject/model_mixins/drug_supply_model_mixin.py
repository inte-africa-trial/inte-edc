from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class DrugSupplyModelMixin(models.Model):

    supply_received_days = models.IntegerField(
        verbose_name="Days supply from clinic pharmacy",
        validators=[MinValueValidator(0), MaxValueValidator(180)],
    )
    supply_purchased_days = models.IntegerField(
        verbose_name="Days supply purchased",
        validators=[MinValueValidator(0), MaxValueValidator(180)],
        help_text=(
            "This can be purchased by patient, through a medicines club "
            "that the patient belong to, through insurance or someone else has paid. "
        ),
    )

    class Meta:
        abstract = True
