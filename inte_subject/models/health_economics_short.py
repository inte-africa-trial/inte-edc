from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from edc_constants.choices import YES_NO, YES_NO_NA
from edc_constants.constants import NOT_APPLICABLE
from edc_model import models as edc_models

from inte_lists.models import DrugPaySources

from ..model_mixins import CrfModelMixin


class HealthEconomicsShort(CrfModelMixin, edc_models.BaseUuidModel):

    """Third iteration of HE form."""

    occupation = models.CharField(
        verbose_name="What is your occupation/profession?", max_length=50
    )

    education_in_years = models.IntegerField(
        verbose_name="How many years of education did you complete?",
        validators=[MinValueValidator(0), MaxValueValidator(50)],
    )

    education_certificate = models.CharField(
        verbose_name="What is your highest education certificate?",
        max_length=50,
        null=True,
        blank=True,
    )

    primary_school = models.CharField(
        verbose_name="Did you go to primary/elementary school?",
        max_length=15,
        choices=YES_NO_NA,
    )

    primary_school_in_years = models.IntegerField(
        verbose_name="If YES, for how many years",
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        null=True,
        blank=True,
    )

    secondary_school = models.CharField(
        verbose_name="Did you go to secondary school?", max_length=15, choices=YES_NO_NA
    )

    secondary_school_in_years = models.IntegerField(
        verbose_name="If YES, for how many years",
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        null=True,
        blank=True,
    )

    higher_education = models.CharField(
        verbose_name="Did you go to higher education?", max_length=15, choices=YES_NO_NA
    )

    higher_education_in_years = models.IntegerField(
        verbose_name="If YES, for how many years",
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        null=True,
        blank=True,
    )

    welfare = models.CharField(
        verbose_name="Do you receive any welfare or social service support",
        max_length=15,
        choices=YES_NO,
    )

    #################################################
    # Previous health care expenses: Medications
    received_rx_month = models.CharField(
        verbose_name=(
            "Over the last month, did you get any drugs on "
            "your visit to the health facility?"
        ),
        max_length=15,
        choices=YES_NO,
        help_text="not including today",
    )

    rx_dm_month = models.CharField(
        verbose_name=(
            "Did you receive drugs for raised blood sugar " "(diabetes) over the last month?"
        ),
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
        help_text="not including today",
    )
    rx_dm_paid_month = models.ManyToManyField(
        DrugPaySources,
        related_name="+",
        verbose_name="If YES, how were these paid for?",
        blank=True,
    )

    rx_dm_paid_month_other = edc_models.OtherCharField(
        verbose_name="If `other pay source`, please specify ... (DM)"
    )

    rx_dm_cost_month = models.IntegerField(
        verbose_name="If these drugs were not free, how much did you pay?",
        validators=[MinValueValidator(0)],
        null=True,
        blank=True,
        help_text="In local currency",
    )

    rx_htn_month = models.CharField(
        verbose_name=(
            "Did you receive drugs for raised blood pressure "
            "(hypertension) over the last month?"
        ),
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
        help_text="not including today",
    )

    rx_htn_paid_month = models.ManyToManyField(
        DrugPaySources,
        related_name="+",
        verbose_name="If YES, how were these paid for?",
        blank=True,
    )

    rx_htn_paid_month_other = edc_models.OtherCharField(
        verbose_name="If `other pay source`, please specify ...(HTN)"
    )

    rx_htn_cost_month = models.IntegerField(
        verbose_name="If these drugs were not free, how much did you pay?",
        validators=[MinValueValidator(0)],
        null=True,
        blank=True,
        help_text="In local currency",
    )

    rx_hiv_month = models.CharField(
        verbose_name="Did you receive anti-retroviral drugs for HIV over the last month?",
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
        help_text="not including today",
    )
    rx_hiv_paid_month = models.ManyToManyField(
        DrugPaySources,
        related_name="+",
        verbose_name="If YES, how were these paid for?",
        max_length=25,
        blank=True,
    )

    rx_hiv_paid_month_other = edc_models.OtherCharField(
        verbose_name="If `other pay source`, please specify ... (HIV)"
    )

    rx_hiv_cost_month = models.IntegerField(
        verbose_name="If these drugs were not free, how much did you pay?",
        validators=[MinValueValidator(0)],
        null=True,
        blank=True,
        help_text="In local currency",
    )

    rx_other_month = models.CharField(
        verbose_name="Did you receive any 'other' drugs?",
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
    )

    rx_other_paid_month = models.ManyToManyField(
        DrugPaySources,
        related_name="+",
        verbose_name="If YES, received 'other' drugs, how were these paid for?",
        blank=True,
    )

    rx_other_paid_month_other = edc_models.OtherCharField(
        verbose_name="If `other pay source`, please specify ..."
    )

    rx_other_cost_month = models.IntegerField(
        verbose_name="If not free, how much did you pay for these 'other' drugs?",
        validators=[MinValueValidator(0)],
        null=True,
        blank=True,
        help_text="In local currency",
    )

    #######################################################
    # Current Visit: health care expenses
    received_rx_today = models.CharField(
        verbose_name="Did you get any drugs on your visit to the health facility today?",
        max_length=15,
        choices=YES_NO,
    )

    rx_dm_today = models.CharField(
        verbose_name="Did you receive drugs for raised blood sugar (diabetes) today?",
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
    )
    rx_dm_paid_today = models.ManyToManyField(
        DrugPaySources,
        related_name="+",
        verbose_name=(
            "If YES, received raised blood sugar " "(diabetes) drugs, how were these paid for?"
        ),
        blank=True,
    )

    rx_dm_paid_today_other = edc_models.OtherCharField(
        verbose_name="If `other pay source`, please specify ..."
    )

    rx_dm_cost_today = models.IntegerField(
        verbose_name=(
            "If not free, how much did you pay for raised blood sugar (diabetes) drugs?"
        ),
        validators=[MinValueValidator(0)],
        null=True,
        blank=True,
        help_text="In local currency",
    )

    rx_htn_today = models.CharField(
        verbose_name="Did you receive raised blood pressure (hypertension) drugs today?",
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
    )

    rx_htn_paid_today = models.ManyToManyField(
        DrugPaySources,
        related_name="+",
        verbose_name=(
            "If YES, received high blood pressure "
            "(Hypertension) drugs, how were these paid for?"
        ),
        blank=True,
    )

    rx_htn_paid_today_other = edc_models.OtherCharField(
        verbose_name="If `other pay source`, please specify ..."
    )
    rx_htn_cost_today = models.IntegerField(
        verbose_name=(
            "If not free, how much did you pay for high blood pressure (Hypertension) drugs?"
        ),
        validators=[MinValueValidator(0)],
        null=True,
        blank=True,
        help_text="In local currency",
    )

    rx_hiv_today = models.CharField(
        verbose_name="Did you receive ARVs (HIV) today?",
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
    )

    rx_hiv_paid_today = models.ManyToManyField(
        DrugPaySources,
        related_name="+",
        verbose_name="If YES, received ARV (HIV) drugs, how were these paid for?",
        max_length=25,
        blank=True,
    )

    rx_hiv_paid_today_other = edc_models.OtherCharField(
        verbose_name="If `other pay source`, please specify ..."
    )

    rx_hiv_cost_today = models.IntegerField(
        verbose_name="If not free, how much did you pay for ARV (HIV) drugs?",
        validators=[MinValueValidator(0)],
        null=True,
        blank=True,
        help_text="In local currency",
    )

    rx_other_today = models.CharField(
        verbose_name="Did you receive 'other' drugs today?",
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
    )

    rx_other_paid_today = models.ManyToManyField(
        DrugPaySources,
        related_name="+",
        verbose_name="If YES, received 'other' drugs, how were these paid for?",
        blank=True,
    )

    rx_other_paid_today_other = edc_models.OtherCharField(
        verbose_name="If `other pay source`, please specify ..."
    )

    rx_other_cost_today = models.IntegerField(
        verbose_name="If not free, how much did you pay for these 'other' drugs?",
        validators=[MinValueValidator(0)],
        null=True,
        blank=True,
        help_text="In local currency",
    )

    health_insurance = models.CharField(
        verbose_name="Do you have private healthcare insurance?",
        max_length=15,
        choices=YES_NO,
    )

    health_insurance_cost = models.IntegerField(
        verbose_name=(
            "If Yes, how much do you pay towards your contributions to "
            "healthcare insurance every month?"
        ),
        null=True,
        blank=True,
        help_text="in local currency",
    )

    patient_club = models.CharField(
        verbose_name="Do you contribute to a patient club?",
        max_length=15,
        choices=YES_NO,
    )

    patient_club_cost = models.IntegerField(
        verbose_name=(
            "If Yes, how much do you pay towards your contributions to "
            "the patient club every month?"
        ),
        null=True,
        blank=True,
        help_text="in local currency",
    )

    class Meta(CrfModelMixin.Meta, edc_models.BaseUuidModel.Meta):
        verbose_name = "Health Economics (Short)"
        verbose_name_plural = "Health Economics (Short)"
