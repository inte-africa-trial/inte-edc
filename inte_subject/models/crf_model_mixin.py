from django.contrib.sites.managers import CurrentSiteManager
from django.db import models
from django.db.models.deletion import PROTECT
from edc_consent.model_mixins import RequiresConsentFieldsModelMixin
from edc_metadata.model_mixins.updates import UpdatesCrfMetadataModelMixin
from edc_model.models.historical_records import HistoricalRecords
from edc_offstudy.model_mixins import OffstudyCrfModelMixin
from edc_reference.model_mixins import ReferenceModelMixin
from edc_sites.models import SiteModelMixin
from edc_visit_schedule.model_mixins import SubjectScheduleCrfModelMixin
from edc_visit_tracking.managers import CrfModelManager
from edc_visit_tracking.model_mixins import (
    CrfModelMixin as BaseCrfModelMixin,
    PreviousVisitModelMixin,
)

from .subject_visit import SubjectVisit


class CrfNoManagerModelMixin(
    BaseCrfModelMixin,
    SubjectScheduleCrfModelMixin,
    RequiresConsentFieldsModelMixin,
    PreviousVisitModelMixin,
    UpdatesCrfMetadataModelMixin,
    OffstudyCrfModelMixin,
    SiteModelMixin,
    ReferenceModelMixin,
):

    """ Base model for all scheduled models
    """

    subject_visit = models.OneToOneField(SubjectVisit, on_delete=PROTECT)

    def natural_key(self):
        return self.subject_visit.natural_key()

    natural_key.dependencies = [
        "inte_subject.subjectvisit",
        "sites.Site",
        "edc_appointment.appointment",
    ]

    class Meta:
        abstract = True
        indexes = [models.Index(fields=["subject_visit", "site", "id"])]


class CrfModelMixin(CrfNoManagerModelMixin):

    on_site = CurrentSiteManager()
    objects = CrfModelManager()
    history = HistoricalRecords(inherit=True)

    class Meta(CrfNoManagerModelMixin.Meta):
        abstract = True
