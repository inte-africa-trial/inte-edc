from django.db import models
from django.utils.safestring import mark_safe
from edc_constants.choices import YES_NO_UNKNOWN, YES_NO_NA
from edc_constants.constants import NOT_APPLICABLE
from edc_crf.model_mixins import CrfModelMixin
from edc_model.models.base_uuid_model import BaseUuidModel
from edc_model.validators import date_is_future


class BaselineCareStatus(CrfModelMixin, BaseUuidModel):
    hiv = models.CharField(
        verbose_name=mark_safe("Have you previously tested <u>positive</u> for HIV"),
        max_length=15,
        choices=YES_NO_UNKNOWN,
    )

    receives_care_at_hiv_clinic = models.CharField(
        verbose_name="Are you receiving care at an HIV clinic",
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
    )

    attends_this_hiv_clinic = models.CharField(
        verbose_name="Do you attend the HIV clinic within this facility",
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
    )

    hiv_clinic_other = models.CharField(
        verbose_name=mark_safe(
            "If <u>not</u> attending the HIV clinic in this facility, where do you attend?"
        ),
        max_length=50,
        null=True,
        blank=True,
    )

    hiv_clinic_other_is_study_clinic = models.CharField(
        verbose_name="Is this HIV clinic an INTE study clinic?",
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
    )

    hiv_clinic_willing_to_transfer = models.CharField(
        verbose_name="Would you be willing to transfer to the HIV clinic in this facility?",
        max_length=50,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
    )

    hiv_clinic_next_appt_date = models.DateField(
        verbose_name="When is your next HIV appointment",
        validators=[date_is_future],
        null=True,
        blank=True,
    )

    diabetic = models.CharField(
        verbose_name=mark_safe(
            "Have you previously been diagnosed with <u>diabetes</u>?"
        ),
        max_length=25,
        choices=YES_NO_UNKNOWN,
    )

    hypertensive = models.CharField(
        verbose_name=mark_safe(
            "Have you previously been diagnosed with <u>hypertension</u>?"
        ),
        max_length=25,
        choices=YES_NO_UNKNOWN,
    )

    receives_care_at_ncd_clinic = models.CharField(
        verbose_name="Are you receiving care at an NCD clinic",
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
    )

    attends_this_ncd_clinic = models.CharField(
        verbose_name="Do you attend the NCD clinic within this facility",
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
    )

    ncd_clinic_other = models.CharField(
        verbose_name="If not attending the NCD clinic in this facility, where do you attend?",
        max_length=50,
        null=True,
        blank=True,
    )

    ncd_clinic_willing_to_transfer = models.CharField(
        verbose_name="Would you be willing to transfer to the NCD clinic in this facility?",
        max_length=50,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
    )

    ncd_clinic_other_is_study_clinic = models.CharField(
        verbose_name="Is this NCD clinic an INTE study clinic?",
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
    )

    ncd_clinic_next_appt_date = models.DateField(
        verbose_name="When is your next NCD appointment",
        validators=[date_is_future],
        null=True,
        blank=True,
    )

    class Meta(CrfModelMixin.Meta):
        verbose_name = "Baseline Care Status"
        verbose_name_plural = "Baseline Care Status"
