from edc_reference import site_reference_configs

site_reference_configs.register_from_visit_schedule(
    visit_models={"edc_appointment.appointment": "inte_subject.subjectvisit"}
)

configs = {
    "inte_subject.clinicalreviewbaseline": [
        "hiv_tested",
        "diabetes_tested",
        "hypertension_tested",
        "hiv_dx",
        "diabetes_dx",
        "hypertension_dx",
    ],
    "inte_subject.clinicalreview": ["hiv_dx", "diabetes_dx", "hypertension_dx"],
    "inte_subject.medications": [
        "refill_hiv",
        "refill_diabetes",
        "refill_hypertension",
    ],
}

for reference_name, fields in configs.items():
    site_reference_configs.add_fields_to_config(name=reference_name, fields=fields)
