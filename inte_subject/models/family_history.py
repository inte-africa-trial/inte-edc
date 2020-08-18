from django.db import models
from django.utils.safestring import mark_safe
from edc_constants.choices import TRUE_FALSE_DONT_KNOW
from edc_model import models as edc_models

from ..choices import HOUSEHOLD_YES_NO_CHOICES
from ..model_mixins import CrfModelMixin


class FamilyHistory(CrfModelMixin, edc_models.BaseUuidModel):
    hypertension_in_household = models.CharField(
        verbose_name=mark_safe(
            "Do you know if anyone else in your household has <ul>high blood pressure</ul?"
        ),
        max_length=25,
        choices=HOUSEHOLD_YES_NO_CHOICES,
    )

    diabetes_in_household = models.CharField(
        verbose_name=mark_safe(
            "Do you know if anyone else in your household has <ul>diabetes</ul?"
        ),
        max_length=25,
        choices=HOUSEHOLD_YES_NO_CHOICES,
    )

    hiv_in_household = models.CharField(
        verbose_name=mark_safe(
            "Do you know if anyone else in your household has <ul>HIV</ul?"
        ),
        max_length=25,
        choices=HOUSEHOLD_YES_NO_CHOICES,
    )

    high_bp_bs_tf = models.CharField(
        verbose_name=mark_safe(
            "High blood pressure and high blood sugar can cause many "
            "illnesses like heart attacks, stroke, kidney failure"
        ),
        max_length=25,
        choices=TRUE_FALSE_DONT_KNOW,
    )

    overweight_tf = models.CharField(
        verbose_name=mark_safe(
            "Being overweight protects from high blood pressure and high blood sugar"
        ),
        max_length=25,
        choices=TRUE_FALSE_DONT_KNOW,
    )

    salty_foods_tf = models.CharField(
        verbose_name=mark_safe("Salty food protects from high blood sugar"),
        max_length=25,
        choices=TRUE_FALSE_DONT_KNOW,
    )

    excercise_tf = models.CharField(
        verbose_name=mark_safe(
            "Regular exercise is important for people with <ul>high blood "
            "pressure</ul> or <ul>high blood sugar</ul> even if they are taking "
            "medicines for these conditions."
        ),
        max_length=25,
        choices=TRUE_FALSE_DONT_KNOW,
    )

    take_medicine_tf = models.CharField(
        verbose_name=mark_safe(
            "Drugs for <ul>blood sugar</ul> and <ul>blood pressure</ul> can make you unwell"
        ),
        max_length=25,
        choices=TRUE_FALSE_DONT_KNOW,
    )

    stop_hypertension_meds_tf = models.CharField(
        verbose_name=mark_safe(
            "It is best to stop taking <ul>blood pressure</ul> pills when "
            "you feel better and start pill taking again when you feel sick"
        ),
        max_length=25,
        choices=TRUE_FALSE_DONT_KNOW,
    )

    traditional_hypertension_tf = models.CharField(
        verbose_name=mark_safe(
            "Herbs and traditional medicine are better for "
            "managing <ul>blood pressure</ul> than pills and medicines"
        ),
        max_length=25,
        choices=TRUE_FALSE_DONT_KNOW,
    )

    stop_diabetes_meds_tf = models.CharField(
        verbose_name=mark_safe(
            "It is best to stop taking <ul>blood sugar</ul> medicines when "
            "you feel better and start pill taking again when you feel sick"
        ),
        max_length=25,
        choices=TRUE_FALSE_DONT_KNOW,
    )

    traditional_diabetes_tf = models.CharField(
        verbose_name=mark_safe(
            "Herbs and traditional medicine are better for managing "
            "<ul>diabetes</ul> than pills and medicines"
        ),
        max_length=25,
        choices=TRUE_FALSE_DONT_KNOW,
    )

    diabetes_cause_tf = models.CharField(
        verbose_name=mark_safe(
            "Having drinks with sugar (e.g. tea/coffee) causes diabetes"
        ),
        max_length=25,
        choices=TRUE_FALSE_DONT_KNOW,
    )

    class Meta(CrfModelMixin.Meta, edc_models.BaseUuidModel.Meta):
        verbose_name = "Family History and Knowledge"
        verbose_name_plural = "Family History and Knowledge"
