from edc_action_item.site_action_items import site_action_items
from edc_visit_tracking.action_items import VisitMissedAction


class SubjectVisitMissedAction(VisitMissedAction):
    reference_model = "inte_subject.subjectvisitmissed"
    admin_site_name = "inte_subject_admin"


site_action_items.register(SubjectVisitMissedAction)
