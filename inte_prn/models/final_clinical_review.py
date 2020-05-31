from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from edc_constants.choices import YES_NO
from edc_model.validators.date import date_not_future

from edc_reportable import COPIES_PER_MILLILITER
from inte_subject.choices import GLUCOSE_UNITS


class FinalClinicalReview(models.Model):
    date = models.DateField(
        verbose_name="Date:",
        validators=[date_not_future],
        blank=False,
        null=True,
    )

    initials = models.CharField(
        verbose_name="Date",
        blank=False,
        max_length=3,
        null=True
    )

    hiv = models.CharField(
        verbose_name="Does the patient have HIV",
        choices=YES_NO,
        max_length=15,
        blank=True,
        null=True
    )

    diabetes = models.CharField(
        verbose_name="Does the patient have DIABETES",
        choices=YES_NO,
        max_length=15,
        blank=True,
        null=True
    )

    hypertension = models.CharField(
        verbose_name="Does the patient have HYPERTENSION",
        choices=YES_NO,
        max_length=15,
        blank=True,
        null=True
    )

    weight = models.DecimalField(
        verbose_name="What is the patient’s weight today?",
        decimal_places=1,
        max_digits=4,
        null=True,
        blank=True,
    )

    height = models.DecimalField(
        verbose_name="What is their height? ",
        decimal_places=1,
        max_digits=4,
        null=True,
        blank=True
    )

    health_insurance = models.CharField(
        verbose_name="Does the patient have any private or work-place health insurance?",
        choices=YES_NO,
        max_length=15,
        blank=True
    )

    club_support = models.CharField(
        verbose_name="Does the patient belong to a ‘club’ that supports medicines purchase?",
        choices=YES_NO,
        max_length=15,
        blank=True,
        null=True,
    )

    blood_glucose = models.DecimalField(
        verbose_name="Blood glucose test result",
        decimal_places=1,
        max_digits=3,
        blank=True,
        null=True
    )

    fasting = models.CharField(
        verbose_name="Had the participant fasted? ",
        choices=YES_NO,
        max_length=15,
        blank=True,
        null=True
    )

    hbA1c = models.DecimalField(
        verbose_name="HbA1c test result",
        decimal_places=1,
        max_digits=2,
        blank=True,
        null=True,
    )

    fasting_glucose_units = models.CharField(
        verbose_name="Units (fasting glucose)",
        max_length=15,
        choices=GLUCOSE_UNITS,
        blank=True,
        null=True,
    )

    sys_blood_pressure_1 = models.IntegerField(
        verbose_name="Reading 1: Systolic pressure",
        null=True,
        blank=True,
    )

    dia_blood_pressure_1 = models.IntegerField(
        verbose_name="Reading 1: Diastolic pressure",
        null=True,
        blank=True,
    )

    sys_blood_pressure_2 = models.IntegerField(
        verbose_name="Reading 2: Systolic pressure",
        null=True,
        blank=True,
    )

    dia_blood_pressure_2 = models.IntegerField(
        verbose_name="Reading 2: Diastolic pressure",
        null=True,
        blank=True,
    )

    viral_load = models.IntegerField(
        verbose_name="The viral load result from this date",
        validators=[MinValueValidator(0), MaxValueValidator(999999)],
        null=True,
        blank=True,
        help_text=COPIES_PER_MILLILITER,
    )

    viral_load_date = models.DateTimeField(
        verbose_name="Date of the viral load test",
        null=True,
        blank=True,
    )

    stroke = models.CharField(
        verbose_name="Stroke",
        choices=YES_NO,
        max_length=15,
        blank=True,
        null=True,
    )

    heart_attack = models.CharField(
        verbose_name="Heart attack / heart failure",
        choices=YES_NO,
        max_length=15,
        blank=True,
        null=True,
    )

    renal_disease = models.CharField(
        verbose_name="Renal (kidney) disease",
        choices=YES_NO,
        max_length=15,
        blank=True,
    )

    vision_problem = models.CharField(
        verbose_name="Vision problems (e.g. blurred vision)",
        choices=YES_NO,
        max_length=15,
        blank=True,
    )

    numbness = models.CharField(
        verbose_name="Numbness / burning sensation",
        choices=YES_NO,
        max_length=15,
        blank=True,
    )

    foot_ulcers = models.CharField(
        verbose_name="Foot ulcers ",
        choices=YES_NO,
        max_length=15,
        blank=True,
    )

    other_condition = models.CharField(
        verbose_name="Any other major conditions?",
        choices=YES_NO,
        max_length=15,
        blank=True
    )
    condition_specify = models.TextField(
        verbose_name="Specify",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Final Clinical Review"
        verbose_name_plural = "Final Clinical Review"
