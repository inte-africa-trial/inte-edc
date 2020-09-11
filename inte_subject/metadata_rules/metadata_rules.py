from edc_constants.constants import YES
from edc_metadata import REQUIRED, NOT_REQUIRED
from edc_metadata_rules import CrfRule, CrfRuleGroup, register, P

from .predicates import Predicates

pc = Predicates()


@register()
class ClinicalReviewBaselineRuleGroup(CrfRuleGroup):

    hiv = CrfRule(
        predicate=P("hiv_dx", "eq", YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=["hivinitialreview"],
    )

    diabetes = CrfRule(
        predicate=P("dm_dx", "eq", YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=["dminitialreview"],
    )

    hypertension = CrfRule(
        predicate=P("htn_dx", "eq", YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=["htninitialreview"],
    )

    class Meta:
        app_label = "inte_subject"
        source_model = "inte_subject.clinicalreviewbaseline"


@register()
class ClinicalReviewRuleGroup(CrfRuleGroup):

    hiv_dx = CrfRule(
        predicate=P("hiv_dx", "eq", YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=["hivinitialreview"],
    )

    dm_dx = CrfRule(
        predicate=P("dm_dx", "eq", YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=["dminitialreview"],
    )

    htn_dx = CrfRule(
        predicate=P("htn_dx", "eq", YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=["htninitialreview"],
    )

    hiv_test = CrfRule(
        predicate=pc.hiv_review_required,
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=["hivreview"],
    )

    dm_test = CrfRule(
        predicate=pc.dm_review_required,
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=["dmreview"],
    )

    htn_test = CrfRule(
        predicate=pc.htn_review_required,
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=["htnreview"],
    )

    class Meta:
        app_label = "inte_subject"
        source_model = "inte_subject.clinicalreview"


@register()
class HealthEconomicsRuleGroup(CrfRuleGroup):

    econ = CrfRule(
        predicate=pc.health_economics_required,
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=["healtheconomicsrevised"],
    )

    class Meta:
        app_label = "inte_subject"
        source_model = "inte_subject.subjectvisit"


@register()
class FamilyHistoryRuleGroup(CrfRuleGroup):

    econ = CrfRule(
        predicate=pc.family_history_required,
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=["familyhistory"],
    )

    class Meta:
        app_label = "inte_subject"
        source_model = "inte_subject.subjectvisit"


@register()
class MedicationsRuleGroup(CrfRuleGroup):

    refill_hiv = CrfRule(
        predicate=P("refill_hiv", "eq", YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=["drugrefillhiv"],
    )

    refill_dm = CrfRule(
        predicate=P("refill_dm", "eq", YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=["drugrefilldm"],
    )

    refill_htn = CrfRule(
        predicate=P("refill_htn", "eq", YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=["drugrefillhtn"],
    )

    class Meta:
        app_label = "inte_subject"
        source_model = "inte_subject.medications"
