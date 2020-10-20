from django.db import models
from edc_action_item.models.action_model_mixin import ActionModelMixin
from edc_constants.choices import YES_NO_TBD
from edc_constants.constants import TBD
from edc_identifier.managers import SubjectIdentifierManager
from edc_identifier.model_mixins import (
    TrackingModelMixin,
    NonUniqueSubjectIdentifierFieldMixin,
)
from edc_model.models.base_uuid_model import BaseUuidModel
from edc_prn.constants import UNBLINDING_REVIEW_ACTION
from edc_sites.models import SiteModelMixin, CurrentSiteManager
from edc_utils.date import get_utcnow

from .unblinding_user import UnblindingReviewerUser


class UnblindingReview(
    NonUniqueSubjectIdentifierFieldMixin,
    SiteModelMixin,
    ActionModelMixin,
    TrackingModelMixin,
    BaseUuidModel,
):

    action_name = UNBLINDING_REVIEW_ACTION

    tracking_identifier_prefix = "UR"

    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time", default=get_utcnow
    )

    reviewer = models.ForeignKey(
        UnblindingReviewerUser,
        related_name="+",
        on_delete=models.PROTECT,
        verbose_name="Unblinding request reviewed by",
        help_text="Select a name from the list",
    )

    approved = models.CharField(max_length=15, default=TBD, choices=YES_NO_TBD)

    comment = models.TextField(verbose_name="Comment", null=True)

    on_site = CurrentSiteManager()

    objects = SubjectIdentifierManager()

    def natural_key(self):
        return (self.action_identifier,)

    class Meta(BaseUuidModel.Meta):
        verbose_name = "Unblinding Review"
        verbose_name_plural = "Unblinding Reviews"
        indexes = [
            models.Index(
                fields=["subject_identifier", "action_identifier", "site", "id"]
            )
        ]
