from django.db import models
from edc_action_item.models.action_model_mixin import ActionModelMixin
from edc_identifier.model_mixins import (
    NonUniqueSubjectIdentifierFieldMixin,
    TrackingModelMixin,
)
from edc_ltfu.constants import LOSS_TO_FOLLOWUP_ACTION
from edc_ltfu.model_mixins import LossToFollowupModelMixin
from edc_model.models.base_uuid_model import BaseUuidModel
from edc_sites.models import CurrentSiteManager, SiteModelMixin
from edc_visit_schedule.model_mixins import VisitScheduleFieldsModelMixin

from inte_prn.choices import LOSS_CHOICES
from inte_prn.constants import LOSS_TO_FOLLOWUP_HIV_ACTION, LOSS_TO_FOLLOWUP_NCD_ACTION
from inte_visit_schedule.constants import SCHEDULE_HIV, SCHEDULE_NCD


class LossToFollowup(
    NonUniqueSubjectIdentifierFieldMixin,
    LossToFollowupModelMixin,
    VisitScheduleFieldsModelMixin,
    SiteModelMixin,
    ActionModelMixin,
    TrackingModelMixin,
    BaseUuidModel,
):

    action_name = LOSS_TO_FOLLOWUP_ACTION

    tracking_identifier_prefix = "LF"

    loss_category = models.CharField(
        verbose_name="Category of loss to follow up",
        max_length=25,
        choices=LOSS_CHOICES,
    )

    on_site = CurrentSiteManager()

    class Meta(LossToFollowupModelMixin.Meta, BaseUuidModel.Meta):
        indexes = [
            models.Index(fields=["subject_identifier", "action_identifier", "site", "id"])
        ]


class LossToFollowupHiv(LossToFollowup):
    action_name = LOSS_TO_FOLLOWUP_HIV_ACTION
    tracking_identifier_prefix = "LFHIV"

    tracking_identifier_prefix = "LH"

    def save(self, *args, **kwargs):
        self.visit_schedule_name = "visit_schedule"
        self.schedule_name = SCHEDULE_HIV
        super().save(*args, **kwargs)

    class Meta:
        proxy = True
        verbose_name = "Loss to Follow Up (HIV)"
        verbose_name_plural = "Loss to Follow Ups (HIV)"


class LossToFollowupNcd(LossToFollowup):
    action_name = LOSS_TO_FOLLOWUP_NCD_ACTION
    tracking_identifier_prefix = "LN"

    def save(self, *args, **kwargs):
        self.visit_schedule_name = "visit_schedule"
        self.schedule_name = SCHEDULE_NCD
        super().save(*args, **kwargs)

    class Meta:
        proxy = True
        verbose_name = "Loss to Follow Up (NCD)"
        verbose_name_plural = "Loss to Follow Ups (NCD)"
