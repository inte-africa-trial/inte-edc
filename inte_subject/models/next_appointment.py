from django.db import models
from edc_crf.model_mixins import CrfModelMixin
from edc_model import models as edc_models


class NextAppointment(CrfModelMixin, edc_models.BaseUuidModel):

    hiv_clinic_appt_date = models.DateField(
        verbose_name="HIV clinic: next scheduled routine appointment",
        validators=[edc_models.date_is_future],
        null=True,
        blank=True,
        help_text="if applicable.",
    )

    ncd_clinic_appt_date = models.DateField(
        verbose_name="NCD clinic: next scheduled routine appointment",
        validators=[edc_models.date_is_future],
        null=True,
        blank=True,
        help_text="if applicable.",
    )

    diabetes_clinic_appt_date = models.DateField(
        verbose_name="Diabetes-only clinic: next scheduled routine appointment",
        validators=[edc_models.date_is_future],
        null=True,
        blank=True,
        help_text="if applicable.",
    )

    hypertension_clinic_appt_date = models.DateField(
        verbose_name="Hypertension-only clinic: next scheduled routine appointment",
        validators=[edc_models.date_is_future],
        null=True,
        blank=True,
        help_text="if applicable.",
    )

    class Meta(CrfModelMixin.Meta, edc_models.BaseUuidModel.Meta):
        verbose_name = "Routine Appointment"
        verbose_name_plural = "Routine Appointments"
