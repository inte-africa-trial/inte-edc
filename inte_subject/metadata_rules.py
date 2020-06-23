from edc_constants.constants import POS, YES
from edc_metadata import REQUIRED, NOT_REQUIRED
from edc_metadata_rules import CrfRule, CrfRuleGroup, register, P


@register()
class CareStatusRuleGroup(CrfRuleGroup):

    hiv = CrfRule(
        predicate=P("hiv_result", "eq", POS),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=["hivinitialreview"],
    )

    diabetic = CrfRule(
        predicate=P("diabetic", "eq", YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=["diabetesinitialreview"],
    )

    hypertensive = CrfRule(
        predicate=P("hypertensive", "eq", YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=["hypertensioninitialreview"],
    )

    class Meta:
        app_label = "inte_subject"
        source_model = "inte_subject.carestatus"
