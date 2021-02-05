from django.core.exceptions import ImproperlyConfigured
from edc_action_item.site_action_items import site_action_items
from edc_visit_tracking.action_items import VisitMissedAction

from inte_prn.constants import LOSS_TO_FOLLOWUP_HIV_ACTION, LOSS_TO_FOLLOWUP_NCD_ACTION
from inte_visit_schedule.constants import SCHEDULE_HIV, SCHEDULE_NCD


class SubjectVisitMissedAction(VisitMissedAction):
    reference_model = "inte_subject.subjectvisitmissed"
    admin_site_name = "inte_subject_admin"
    loss_to_followup_action_name = None

    def get_loss_to_followup_action_name(self):
        schedule = self.reference_obj.visit.appointment.schedule
        if schedule.name == SCHEDULE_HIV:
            return LOSS_TO_FOLLOWUP_HIV_ACTION
        if schedule.name == SCHEDULE_NCD:
            return LOSS_TO_FOLLOWUP_NCD_ACTION
        raise ImproperlyConfigured(
            "Unable to determine action name. Schedule name not known. "
            f"Got {schedule.name}."
        )


site_action_items.register(SubjectVisitMissedAction)
