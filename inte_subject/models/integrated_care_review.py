from django.db import models
from edc_constants.choices import YES_NO, YES_NO_DONT_KNOW, YES_NO_NA
from edc_constants.constants import NOT_APPLICABLE
from edc_model import models as edc_models

from inte_lists.models import (
    DrugDispensaries,
    DrugDispensers,
    HealthAdvisors,
    HealthInterventionTypes,
    HealthTalkConditions,
    LaboratoryTests,
)

from ..choices import (
    CARD_TYPE_CHOICES,
    HCF_PRESCRIPTION_COLLECTION_CHOICES,
    MISSED_VISIT_CALLER_CHOICES,
)
from ..model_mixins import CrfModelMixin


class IntegratedCareReview(CrfModelMixin, edc_models.BaseUuidModel):
    """FORM 26 - Participant Review of Integrated Care."""

    receive_health_talk_messages = models.CharField(
        verbose_name="Did you receive a health talk when attending the clinic today?",
        max_length=15,
        choices=YES_NO,
    )

    health_talk_conditions = models.ManyToManyField(
        HealthTalkConditions,
        related_name="+",
        verbose_name="If YES, what disease conditions were discussed?",
        blank=True,
    )

    health_talk_conditions_other = edc_models.OtherCharField()

    health_talk_focus = models.ManyToManyField(
        HealthInterventionTypes,
        related_name="+",
        verbose_name="If YES, what type of messages were covered?",
        blank=True,
    )

    health_talk_focus_other = edc_models.OtherCharField()

    health_talk_presenters = models.ManyToManyField(
        HealthAdvisors,
        related_name="+",
        verbose_name="If YES, who gave the health talk?",
        blank=True,
    )

    health_talk_presenters_other = edc_models.OtherCharField()

    additional_health_advice = models.CharField(
        verbose_name="Did you receive any additional health advice during your visit?",
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

    receive_rx_today = models.CharField(
        verbose_name="Did you receive a drug prescription today?",
        max_length=15,
        choices=YES_NO,
    )

    rx_collection_hcf = models.CharField(
        verbose_name="If YES, are you collecting it from this healthcare facility?",
        max_length=15,
        choices=HCF_PRESCRIPTION_COLLECTION_CHOICES,
        default=NOT_APPLICABLE,
    )

    where_rx_dispensed = models.ManyToManyField(
        DrugDispensaries,
        verbose_name=(
            "If YES, where in this healthcare facility are your drugs dispensed from?"
        ),
        blank=True,
    )

    where_rx_dispensed_other = edc_models.OtherCharField()

    who_dispenses_rx = models.ManyToManyField(
        DrugDispensers,
        verbose_name=(
            "If YES, who in this healthcare facility is responsible for dispensing your drugs?"
        ),
        blank=True,
    )

    who_dispenses_rx_other = edc_models.OtherCharField()

    hospital_card = models.CharField(
        verbose_name="Do you have a hospital record stored in the clinic?",
        max_length=15,
        choices=YES_NO_DONT_KNOW,
    )

    hospital_card_type = models.CharField(
        verbose_name="If YES, what type of hospital record is this?",
        max_length=15,
        choices=CARD_TYPE_CHOICES,
        default=NOT_APPLICABLE,
    )

    missed_appt = models.CharField(
        verbose_name="Have you missed an appointment since attending this clinic?",
        max_length=15,
        choices=YES_NO,
    )

    missed_appt_call = models.CharField(
        verbose_name=(
            "If YES, did you get a phone call from the clinic about the missed appointment?"
        ),
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
    )

    missed_appt_call_who = models.CharField(
        verbose_name="If YES, who called you about the missed appointment?",
        max_length=15,
        choices=MISSED_VISIT_CALLER_CHOICES,
        default=NOT_APPLICABLE,
    )

    missed_appt_call_who_other = edc_models.OtherCharField()

    lab_tests = models.CharField(
        verbose_name="Have you done any laboratory tests since you started in this clinic?",
        max_length=15,
        choices=YES_NO,
    )

    pay_for_lab_tests = models.CharField(
        verbose_name="If YES, did you pay for any of these tests?",
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
    )

    which_lab_tests_charged_for = models.ManyToManyField(
        LaboratoryTests,
        verbose_name="If YES, which tests were you charged for?",
        blank=True,
    )

    which_lab_tests_charged_for_other = edc_models.OtherCharField()

    class Meta(CrfModelMixin.Meta, edc_models.BaseUuidModel.Meta):
        verbose_name = "Integrated Care Review"
        verbose_name_plural = "Integrated Care Reviews"
