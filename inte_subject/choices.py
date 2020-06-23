from edc_constants.constants import NEG, NEVER, NOT_APPLICABLE, OTHER, POS
from edc_reportable import (
    MILLIGRAMS_PER_DECILITER,
    MILLIMOLES_PER_LITER,
    MILLIMOLES_PER_LITER_DISPLAY,
)
from edc_visit_tracking.constants import SCHEDULED, UNSCHEDULED, MISSED_VISIT

from .constants import DIET_LIFESTYLE, DRUGS, INSULIN, SITTING, GTE_3HRS, THIS_CLINIC

CARE_ACCESS = (
    (THIS_CLINIC, "Patient comes to this facility for their care"),
    (OTHER, "Patient goes to a different clinic"),
    (NOT_APPLICABLE, "Not applicable"),
)

HYPERTENSION_MANAGEMENT = (
    (DRUGS, "Drugs / Medicine"),
    (DIET_LIFESTYLE, "Diet and lifestyle alone"),
)

DIABETES_MANAGEMENT = (
    (INSULIN, "Insulin injections"),
    (DRUGS, "Oral drugs"),
    (DIET_LIFESTYLE, "Diet and lifestyle alone"),
)

ALCOHOL_CONSUMPTION = (
    ("ocassionally", "Ocassionally"),
    ("1_2_per_week", "1-2 times a week"),
    ("3_4_per_week", "3-4 times a week"),
    ("daily", "Daily"),
    (NOT_APPLICABLE, "Not applicable"),
)

EMPLOYMENT_STATUS = (
    ("professional", "Professional / office work / business"),
    ("manual_work", "Skilled / Unskilled manual work"),
    ("housewife", "Housewife"),
    ("unemployed", "Not working / seeking work"),
    ("retired", "Retired"),
    (OTHER, "Other, please specify"),
)

EDUCATION = (
    ("no_formal_education", "No Formal Education"),
    ("primary", "Up to primary"),
    ("secondary", "Up to secondary / high school"),
    ("tertiary", "university educated"),
)

MARITAL_STATUS = (
    ("married", "Married or living with someone"),
    ("single", "Single"),
    ("divorced", "Divorced"),
    ("widowed", "Widow / Spinster"),
)
# *********************************
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
    (MILLIMOLES_PER_LITER, MILLIMOLES_PER_LITER_DISPLAY),
    (NOT_APPLICABLE, "Not applicable"),
)

PAYEE_CHOICES = (
    ("own_cash", "Own cash"),
    ("insurance", "Insurance"),
    ("relative", "Relative of others paying"),
    ("free", "Free drugs from the pharmacy"),
    (NOT_APPLICABLE, "Not applicable"),
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
