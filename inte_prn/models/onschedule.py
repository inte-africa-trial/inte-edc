from edc_identifier.managers import SubjectIdentifierManager
from edc_model.models import BaseUuidModel, HistoricalRecords
from edc_visit_schedule.model_mixins import CurrentSiteManager, OnScheduleModelMixin


class OnScheduleHiv(OnScheduleModelMixin, BaseUuidModel):
    """A model used by the system. Auto-completed by subject_consent."""

    on_site = CurrentSiteManager()

    objects = SubjectIdentifierManager()

    history = HistoricalRecords()

    class Meta(OnScheduleModelMixin.Meta):
        pass


class OnScheduleNcd(OnScheduleModelMixin, BaseUuidModel):
    """A model used by the system. Auto-completed by subject_consent."""

    on_site = CurrentSiteManager()

    objects = SubjectIdentifierManager()

    history = HistoricalRecords()

    class Meta(OnScheduleModelMixin.Meta):
        pass
