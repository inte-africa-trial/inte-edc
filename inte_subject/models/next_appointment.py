from django.db import models
from edc_model.models import BaseUuidModel

from ..model_mixins import CrfModelMixin


class NextAppointment(CrfModelMixin, BaseUuidModel):
    next_appt_date = models.DateField()

    class Meta(CrfModelMixin.Meta):
        verbose_name = "Next Appointment"
        verbose_name_plural = "Next Appointments"
