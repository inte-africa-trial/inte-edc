from django.db import models
from edc_constants.choices import YES_NO
from edc_model import models as edc_models

from inte_lists.models import (
    HealthAdvisors,
    HealthInterventionTypes,
    HealthTalkConditions,
)

from ..model_mixins import CrfModelMixin


class IntegratedCareReview(CrfModelMixin, edc_models.BaseUuidModel):
    """FORM 26 - Participant Review of Integrated Care."""

    receive_health_talk_messages = models.CharField(
        verbose_name="Do you receive health messages when attending this clinic?",
        max_length=15,
        choices=YES_NO,
    )

    health_talk_conditions = models.ManyToManyField(
        HealthTalkConditions,
        related_name="+",
        verbose_name="If YES, what disease conditions are discussed during health talks?",
        blank=True,
    )

    health_talk_conditions_other = edc_models.OtherCharField()

    health_talk_focus = models.ManyToManyField(
        HealthInterventionTypes,
        related_name="+",
        verbose_name="If YES, what type of messages are delivered during health talks?",
        blank=True,
    )

    health_talk_focus_other = edc_models.OtherCharField()

    health_talk_presenters = models.ManyToManyField(
        HealthAdvisors,
        related_name="+",
        verbose_name="If YES, who gives the health talks?",
        blank=True,
    )

    health_talk_presenters_other = edc_models.OtherCharField()

    additional_health_advice = models.CharField(
        verbose_name="Did you receive any additional health advice during your visits?",
        max_length=15,
        choices=YES_NO,
    )

    health_advice_advisor = models.ManyToManyField(
        HealthAdvisors,
        related_name="+",
        verbose_name="If YES, who gave this health advice?",
        blank=True,
    )

    health_advice_advisor_other = edc_models.OtherCharField()

    health_advice_focus = models.ManyToManyField(
        HealthInterventionTypes,
        related_name="+",
        verbose_name="If YES, what was the focus of the advice?",
        blank=True,
    )

    health_advice_focus_other = edc_models.OtherCharField()

    class Meta(CrfModelMixin.Meta, edc_models.BaseUuidModel.Meta):
        verbose_name = "Integrated Care Review"
        verbose_name_plural = "Integrated Care Reviews"
