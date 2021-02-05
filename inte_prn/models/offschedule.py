from edc_action_item.models.action_model_mixin import ActionItemModelManager
from edc_visit_schedule import site_visit_schedules

from inte_visit_schedule.constants import SCHEDULE_HIV, SCHEDULE_NCD

from ..constants import END_OF_STUDY_HIV_ACTION, END_OF_STUDY_NCD_ACTION
from .end_of_study import EndOfStudy


class OffScheduleHivManager(ActionItemModelManager):
    def get_queryset(self):
        qs = self._queryset_class(model=self.model, using=self._db, hints=self._hints)
        return qs.filter(schedule_name=SCHEDULE_HIV)


class OffScheduleNcdManager(ActionItemModelManager):
    def get_queryset(self):
        qs = self._queryset_class(model=self.model, using=self._db, hints=self._hints)
        return qs.filter(schedule_name=SCHEDULE_NCD)


class OffScheduleHiv(EndOfStudy):
    action_name = END_OF_STUDY_HIV_ACTION

    tracking_identifier_prefix = "OH"

    objects = OffScheduleHivManager()

    def save(self, *args, **kwargs):
        self.visit_schedule_name = "visit_schedule"
        self.schedule_name = SCHEDULE_HIV
        super().save(*args, **kwargs)

    @property
    def visit_schedule(self):
        """Returns a visit schedule object."""
        return site_visit_schedules.get_by_onschedule_model(
            onschedule_model=self._meta.label_lower
        )[0]

    @property
    def schedule(self):
        """Returns a schedule object."""
        return site_visit_schedules.get_by_onschedule_model(
            onschedule_model=self._meta.label_lower
        )[1]

    class Meta:
        proxy = True
        verbose_name = "End of Study (HIV)"
        verbose_name_plural = "End of Study (HIV)"


class OffScheduleNcd(EndOfStudy):
    action_name = END_OF_STUDY_NCD_ACTION

    tracking_identifier_prefix = "ON"

    objects = OffScheduleNcdManager()

    def save(self, *args, **kwargs):
        self.visit_schedule_name = "visit_schedule"
        self.schedule_name = SCHEDULE_NCD
        super().save(*args, **kwargs)

    @property
    def visit_schedule(self):
        """Returns a visit schedule object."""
        return site_visit_schedules.get_by_onschedule_model(
            onschedule_model=self._meta.label_lower
        )[0]

    @property
    def schedule(self):
        """Returns a schedule object."""
        return site_visit_schedules.get_by_onschedule_model(
            onschedule_model=self._meta.label_lower
        )[1]

    class Meta:
        proxy = True
        verbose_name = "End of Study (NCD)"
        verbose_name_plural = "End of Study (NCD)"
