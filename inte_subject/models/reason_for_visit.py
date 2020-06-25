from django.db import models
from edc_model import models as edc_models
from inte_lists.models import HealthServices, ClinicServices

from ..model_mixins import CrfModelMixin


class ReasonForVisit(CrfModelMixin, edc_models.BaseUuidModel):

    health_services = models.ManyToManyField(
        HealthServices,
        verbose_name="Which health service(s) is the patient here for today?",
    )

    hiv_services = models.ManyToManyField(
        ClinicServices,
        verbose_name="If HIV, why is the patient at the clinic?",
        related_name="hiv_services",
        blank=True,
    )

    hiv_services_other = models.CharField(
        verbose_name="If other, please specify reason",
        max_length=150,
        null=True,
        blank=True,
    )

    hypertension_services = models.ManyToManyField(
        ClinicServices,
        verbose_name="If hypertension, why is the patient at the clinic?",
        related_name="hypertension_services",
        blank=True,
    )
    hypertension_services_other = models.CharField(
        verbose_name="If other, please specify reason",
        max_length=150,
        null=True,
        blank=True,
    )

    diabetes_services = models.ManyToManyField(
        ClinicServices,
        verbose_name="If diabetes, why is the patient at the clinic?",
        related_name="diabetes_services",
        blank=True,
    )

    diabetes_services_other = models.CharField(
        verbose_name="If other, please specify reason",
        max_length=150,
        null=True,
        blank=True,
    )

    class Meta(CrfModelMixin.Meta, edc_models.BaseUuidModel.Meta):
        verbose_name = "Reason for Visit"
        verbose_name_plural = "Reason for Visit"
