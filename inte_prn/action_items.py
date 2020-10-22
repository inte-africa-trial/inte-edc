from edc_action_item.site_action_items import site_action_items
from edc_adverse_event.constants import DEATH_REPORT_ACTION
from edc_ltfu.action_items import LossToFollowupAction as BaseLossToFollowupAction
from edc_offstudy.action_items import EndOfStudyAction as BaseEndOfStudyAction
from edc_prn.action_items import (
    ProtocolDeviationViolationAction as BaseProtocolDeviationViolationAction,
    UnblindingRequestAction as BaseUnblindingRequestAction,
    UnblindingReviewAction as BaseUnblindingReviewAction,
)
from edc_prn.constants import UNBLINDING_REVIEW_ACTION

from .constants import (
    END_OF_STUDY_HIV_ACTION,
    END_OF_STUDY_NCD_ACTION,
    LOSS_TO_FOLLOWUP_HIV_ACTION,
    LOSS_TO_FOLLOWUP_NCD_ACTION,
)


class EndOfStudyHivAction(BaseEndOfStudyAction):
    reference_model = "inte_prn.offschedulehiv"
    admin_site_name = "inte_prn_admin"
    name = END_OF_STUDY_HIV_ACTION
    display_name = "Submit End of Study (HIV)"
    notification_display_name = "End of Study (HIV)"
    singleton = True
    parent_action_names = [
        UNBLINDING_REVIEW_ACTION,
        DEATH_REPORT_ACTION,
        LOSS_TO_FOLLOWUP_HIV_ACTION,
    ]


class EndOfStudyNcdAction(BaseEndOfStudyAction):
    reference_model = "inte_prn.offschedulencd"
    admin_site_name = "inte_prn_admin"
    name = END_OF_STUDY_NCD_ACTION
    display_name = "Submit End of Study (NCD)"
    notification_display_name = "End of Study (NCD)"
    singleton = True
    parent_action_names = [
        UNBLINDING_REVIEW_ACTION,
        DEATH_REPORT_ACTION,
        LOSS_TO_FOLLOWUP_NCD_ACTION,
    ]


class LossToFollowupHivAction(BaseLossToFollowupAction):
    reference_model = "inte_prn.losstofollowuphiv"
    admin_site_name = "inte_prn_admin"
    name = LOSS_TO_FOLLOWUP_HIV_ACTION
    singleton = True

    def get_next_actions(self):
        next_actions = [END_OF_STUDY_HIV_ACTION]
        return next_actions


class LossToFollowupNcdAction(BaseLossToFollowupAction):
    reference_model = "inte_prn.losstofollowupncd"
    admin_site_name = "inte_prn_admin"
    name = LOSS_TO_FOLLOWUP_NCD_ACTION
    singleton = True

    def get_next_actions(self):
        next_actions = [END_OF_STUDY_NCD_ACTION]
        return next_actions


class ProtocolDeviationViolationAction(BaseProtocolDeviationViolationAction):
    reference_model = "inte_prn.protocoldeviationviolation"
    admin_site_name = "inte_prn_admin"


class UnblindingRequestAction(BaseUnblindingRequestAction):
    reference_model = "inte_prn.unblindingrequest"
    admin_site_name = "inte_prn_admin"


class UnblindingReviewAction(BaseUnblindingReviewAction):
    reference_model = "inte_prn.unblindingreview"
    admin_site_name = "inte_prn_admin"


site_action_items.register(EndOfStudyHivAction)
site_action_items.register(EndOfStudyNcdAction)
site_action_items.register(LossToFollowupHivAction)
site_action_items.register(LossToFollowupNcdAction)
site_action_items.register(ProtocolDeviationViolationAction)
site_action_items.register(UnblindingRequestAction)
site_action_items.register(UnblindingReviewAction)
