from django.db import models
from django.utils.safestring import mark_safe
from edc_constants.choices import YES_NO
from edc_crf.model_mixins import CrfModelMixin
from edc_model.models import BaseUuidModel

from ..choices import PHYSICAL_ACTIVITY, PHYSICAL_ACTIVITY_HOURS


class PhysicalActivity(CrfModelMixin, BaseUuidModel):
    physical_activity = models.CharField(
        verbose_name=(
            "Please tell us the type and amount of physical activity "
            "involved in your work."
        ),
        max_length=50,
        choices=PHYSICAL_ACTIVITY,
        help_text=(
            "Please tick one box that is closest to your present work "
            "from the following five possibilities"
        ),
    )

    physical_exercise = models.CharField(
        verbose_name=mark_safe(
            "<B>Physical exercise</B> such as swimming, jogging, "
            "football, tennis, gym workout etc."
        ),
        max_length=25,
        choices=PHYSICAL_ACTIVITY_HOURS,
    )

    cycling = models.CharField(
        verbose_name=mark_safe(
            "<B>Cycling</B>, including cycling to work and during leisure time."
        ),
        max_length=25,
        choices=PHYSICAL_ACTIVITY_HOURS,
    )
    walking = models.CharField(
        verbose_name=mark_safe(
            "<B>Walking</B>, including walking to work, shopping, for pleasure etc."
        ),
        max_length=25,
        choices=PHYSICAL_ACTIVITY_HOURS,
    )
    housework = models.CharField(
        verbose_name=mark_safe("<B>Housework/Childcare</B>"),
        max_length=25,
        choices=PHYSICAL_ACTIVITY_HOURS,
    )
    casual_labour = models.CharField(
        verbose_name=mark_safe("<B>Gardening, casual labor/DIY</B>"),
        max_length=25,
        choices=PHYSICAL_ACTIVITY_HOURS,
    )

    physically_active = models.CharField(
        verbose_name="Is the patient physically active?",
        max_length=15,
        choices=YES_NO,
        help_text=(
            "Yes” = ≥ 30 minutes of physical activity 5 days a week (or 2.5 hours per week)"
        ),
    )

    class Meta(CrfModelMixin.Meta):
        verbose_name = "Physical Activity"
        verbose_name_plural = "Physical Activity"
