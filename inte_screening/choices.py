from edc_constants.constants import (
    DIABETES,
    HIV,
    HYPERTENSION,
    OTHER,
    PURPOSIVELY_SELECTED,
    RANDOM_SAMPLING,
)

from inte_subject.constants import INTEGRATED, NCD

from .constants import (
    DIABETES_CLINIC,
    HIV_CLINIC,
    HYPERTENSION_CLINIC,
    NCD_CLINIC,
    SEQUENTIAL,
    SYSTEMATIC,
)

CLINIC_CHOICES = (
    (HIV_CLINIC, "HIV Clinic"),
    (NCD_CLINIC, "NCD Clinic (Joint Diabetes/Hypertension)"),
    (DIABETES_CLINIC, "Diabetes Clinic"),
    (HYPERTENSION_CLINIC, "Hypertension Clinic"),
)

REFUSAL_REASONS = (
    ("unwilling_to_say", "I am unwilling to say"),
    ("dont_have_time", "I don't have time"),
    ("stigma", "I am worried about stigma"),
    ("must_consult_spouse", "I need to consult my spouse"),
    ("dont_want_medication", "I don't want to take any more medication"),
    ("dont_want_to_join", "I don't want to take part"),
    ("need_to_think_about_it", "I haven't had a chance to think about it"),
    ("moving", "I am moving to another area"),
    (OTHER, "Other, please specify"),
)


CLINIC_DAYS = (
    (INTEGRATED, "Integrated care day (HIV, Diabetes, Hypertension)"),
    (NCD, "NCD day (Diabetes + Hypertension)"),
    (HIV, "HIV only day"),
    (DIABETES, "Diabetes only day"),
    (HYPERTENSION, "Hypertension only day"),
)

SELECTION_METHOD = (
    (RANDOM_SAMPLING, "Random sampling"),
    (SYSTEMATIC, "Systematically selected"),
    (SEQUENTIAL, "Sequentially selected"),
    (PURPOSIVELY_SELECTED, "Purposively selected"),
)
