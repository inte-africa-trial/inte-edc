from django.db import models
from edc_constants.choices import YES_NO, YES_NO_DONT_KNOW, YES_NO_NA
from edc_constants.constants import NOT_APPLICABLE
from edc_model import models as edc_models

from inte_lists.models import (
    HealthAdvisors,
    HealthInterventionTypes,
    HealthTalkConditions,
    LaboratoryTests,
)
from inte_subject.choices import CARD_TYPE_CHOICES, MISSED_VISIT_CALLER_CHOICES

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

    #################################################
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

    #################################################
    hospital_card = models.CharField(
        verbose_name="Do you have a hospital card used in the clinic?",
        max_length=15,
        choices=YES_NO_DONT_KNOW,
    )

    hospital_card_type = models.CharField(
        verbose_name="If YES, what type of card is this?",
        max_length=15,
        choices=CARD_TYPE_CHOICES,
        default=NOT_APPLICABLE,
    )

    missed_appointment = models.CharField(
        verbose_name="Have you missed an appointment since you started attending this clinic?",
        max_length=15,
        choices=YES_NO,
    )

    missed_appointment_call = models.CharField(
        verbose_name="If YES, did you get a phone call from the clinic about the missed visit?",
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
    )

    missed_appointment_call_who = models.CharField(
        verbose_name="If YES, who called you about the missed visit?",
        max_length=15,
        choices=MISSED_VISIT_CALLER_CHOICES,
        default=NOT_APPLICABLE,
    )

    missed_appointment_call_who_other = edc_models.OtherCharField()

    #################################################
    laboratory_tests = models.CharField(
        verbose_name="Have you done any laboratory tests since you started in this clinic?",
        max_length=15,
        choices=YES_NO,
    )

    pay_for_laboratory_tests = models.CharField(
        verbose_name="If YES, did you pay for any of the tests?",
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
    )

    which_laboratory_tests_charged_for = models.ManyToManyField(
        LaboratoryTests,
        verbose_name="If YES, what tests are you charged for?",
        blank=True,
    )

    which_laboratory_tests_charged_for_other = edc_models.OtherCharField()

    class Meta(CrfModelMixin.Meta, edc_models.BaseUuidModel.Meta):
        verbose_name = "Integrated Care Review"
        verbose_name_plural = "Integrated Care Reviews"
