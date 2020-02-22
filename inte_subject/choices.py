from edc_constants.constants import (
    SMOKER,
    FORMER_SMOKER,
    NONSMOKER,
    NOT_APPLICABLE,
    OTHER,
)
from edc_reportable import (
    MILLIGRAMS_PER_DECILITER,
    MILLIMOLES_PER_LITER,
)
from edc_visit_tracking.constants import SCHEDULED, UNSCHEDULED, MISSED_VISIT

from .constants import SITTING, GTE_3HRS


ACTIVITY_CHOICES = (
    ("working", "Working"),
    ("studying", "Studying"),
    ("caring_for_children", "Caring for children"),
    (OTHER, "Other, please specify"),
)

CHILDCARE_CHOICES = (
    (NOT_APPLICABLE, "Not applicable"),
    ("working", "Working"),
    ("studying", "Studying"),
    ("caring_for_children", "Caring for children"),
    ("house_maintenance", "House maintenance"),
    ("nothing", "Nothing"),
    (OTHER, "Other, specify"),
)

VISIT_UNSCHEDULED_REASON = (
    ("patient_unwell_outpatient", "Patient unwell (outpatient)"),
    ("patient_hospitalised", "Patient hospitalised"),
    ("routine_non_study", "Routine appointment (non-study)"),
    ("recurrence_symptoms", "Recurrence of symptoms"),
    (OTHER, "Other"),
    (NOT_APPLICABLE, "Not applicable"),
)

VISIT_REASON = (
    (SCHEDULED, "Scheduled visit"),
    (UNSCHEDULED, "Unscheduled visit"),
    (MISSED_VISIT, "Missed visit"),
)

ALCOHOL_CONSUMPTION = (
    ("1_day_per_wk", "About once a week"),
    ("2-3_day_per_wk", "2-3 days every week"),
    ("most_days_per_month", "Most days in a month"),
    (NOT_APPLICABLE, "Not applicable"),
)

INFO_SOURCE = (
    ("hospital_notes", "Hospital notes"),
    ("outpatient_cards", "Outpatient cards"),
    ("patient", "Patient"),
    ("collateral_history", "Collateral History from relative/guardian"),
    (OTHER, "Other"),
)

PHYSICAL_ACTIVITY = (
    ("retired", "Retired"),
    (SITTING, "Mostly sitting"),
    ("standing_or_walking", "Mostly standing or walking"),
    ("physical_effort", "Definite physical effort"),
    ("vigorous_physical_activity", "Vigorous physical activity"),
)

PHYSICAL_ACTIVITY_HOURS = (
    ("none", "None"),
    ("lt_1hr", "Some but less than one hour"),
    ("1-3hr", "1 hour but less than 3 hours"),
    (GTE_3HRS, "3 hours or more"),
)


GLUCOSE_UNITS = (
    (MILLIGRAMS_PER_DECILITER, MILLIGRAMS_PER_DECILITER),
    (MILLIMOLES_PER_LITER, MILLIMOLES_PER_LITER),
)

PAYEE_CHOICES = (
    ("own_cash", "Own cash"),
    ("insurance", "Insurance"),
    ("relative", "Relative of others paying"),
    ("free", "Free drugs from the pharmacy"),
    (NOT_APPLICABLE, "Not applicable"),
)

SMOKER_STATUS = (
    (SMOKER, "Currently smoke"),
    (FORMER_SMOKER, "Used to smoke but stopped"),
    (NONSMOKER, "Never smoked"),
)

TRANSPORT_CHOICES = (
    ("bus", "Bus"),
    ("train", "Train"),
    ("ambulance", "Ambulance"),
    ("private_taxi", "Private taxi"),
    ("own_bicycle", "Own bicycle"),
    ("hired_motorbike", "Hired motorbike"),
    ("own_car", "Own car"),
    ("own_motorbike", "Own motorbike"),
    ("hired_bicycle", "Hired bicycle"),
    ("foot", "Foot"),
    (OTHER, "Other, specify"),
)
