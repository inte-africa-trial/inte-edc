from edc_constants.constants import OTHER

DEATH_LOCATIONS = (
    ("home", "At home"),
    ("hospital_clinic", "Hospital/clinic"),
    (OTHER, "Elsewhere, please specify"),
)


INFORMANT = (
    ("spouse", "Spouse"),
    ("Parent", "Parent"),
    ("child", "Child"),
    ("healthcare_worker", "Healthcare Worker"),
    (OTHER, "Other"),
)

CONTACT = (
    ("tel", "Telephone conversation"),
    ("home", "Home visIt"),
    ("relative_at_clinic", "Relative visited the health facility"),
    ("patient_record", "Patient record / document"),
    (OTHER, "Other"),
)
