from django.db import models
from edc_crf.model_mixins import CrfModelMixin
from edc_model.models import BaseUuidModel


class NextAppointment(CrfModelMixin, BaseUuidModel):
    next_appt_date = models.DateField()

    class Meta(CrfModelMixin.Meta):
        verbose_name = "Next Appointment"
        verbose_name_plural = "Next Appointments"
