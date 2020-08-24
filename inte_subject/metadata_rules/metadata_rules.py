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
        predicate=P("diabetes_dx", "eq", YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=["diabetesinitialreview"],
    )

    hypertension = CrfRule(
        predicate=P("hypertension_dx", "eq", YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=["hypertensioninitialreview"],
    )

    class Meta:
        app_label = "inte_subject"
        source_model = "inte_subject.clinicalreviewbaseline"


@register()
class ClinicalReviewRuleGroup(CrfRuleGroup):

    hiv = CrfRule(
        predicate=P("hiv_dx", "eq", YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=["hivinitialreview"],
    )

    diabetes = CrfRule(
        predicate=P("diabetes_dx", "eq", YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=["diabetesinitialreview"],
    )

    hypertension = CrfRule(
        predicate=P("hypertension_dx", "eq", YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=["hypertensioninitialreview"],
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

    refill_diabetes = CrfRule(
        predicate=P("refill_diabetes", "eq", YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=["drugrefilldiabetes"],
    )

    refill_hypertension = CrfRule(
        predicate=P("refill_hypertension", "eq", YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=["drugrefillhypertension"],
    )

    class Meta:
        app_label = "inte_subject"
        source_model = "inte_subject.medications"
