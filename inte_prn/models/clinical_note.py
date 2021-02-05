from django.db import models
from django_crypto_fields.fields import EncryptedTextField
from edc_identifier.managers import SubjectIdentifierManager
from edc_identifier.model_mixins import (
    NonUniqueSubjectIdentifierFieldMixin,
    TrackingModelMixin,
)
from edc_model.models.base_uuid_model import BaseUuidModel
from edc_sites.models import CurrentSiteManager, SiteModelMixin
from edc_utils.date import get_utcnow


class ClinicalNote(
    NonUniqueSubjectIdentifierFieldMixin,
    TrackingModelMixin,
    SiteModelMixin,
    BaseUuidModel,
):

    tracking_identifier_prefix = "CN"

    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time", default=get_utcnow
    )

    subjective = models.TextField(
        verbose_name="Subjective / Pertinant history",
    )

    note = EncryptedTextField(verbose_name="Clinical Note")

    on_site = CurrentSiteManager()

    objects = SubjectIdentifierManager()

    def natural_key(self):
        return (self.tracking_identifier,)

    class Meta(BaseUuidModel.Meta):
        verbose_name = "Clinical Note"
        verbose_name_plural = "Clinical Notes"
        indexes = [models.Index(fields=["tracking_identifier", "site", "id"])]
