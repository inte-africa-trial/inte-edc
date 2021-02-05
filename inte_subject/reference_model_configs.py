from edc_reference import site_reference_configs

site_reference_configs.register_from_visit_schedule(
    visit_models={"edc_appointment.appointment": "inte_subject.subjectvisit"}
)

configs = {
    "inte_subject.clinicalreviewbaseline": [
        "dm_dx",
        "dm_test",
        "hiv_dx",
        "hiv_test",
        "htn_dx",
        "htn_test",
    ],
    "inte_subject.clinicalreview": [
        "complications",
        "dm_dx",
        "dm_test",
        "hiv_dx",
        "hiv_test",
        "htn_dx",
        "htn_test",
    ],
    "inte_subject.medications": ["refill_hiv", "refill_dm", "refill_htn"],
}

for reference_name, fields in configs.items():
    site_reference_configs.add_fields_to_config(name=reference_name, fields=fields)
