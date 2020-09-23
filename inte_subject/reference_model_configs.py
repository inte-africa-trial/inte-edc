from edc_reference import site_reference_configs

site_reference_configs.register_from_visit_schedule(
    visit_models={"edc_appointment.appointment": "inte_subject.subjectvisit"}
)

configs = {
    "inte_subject.clinicalreviewbaseline": [
        "hiv_test",
        "dm_test",
        "htn_test",
        "hiv_dx",
        "dm_dx",
        "htn_dx",
    ],
    "inte_subject.clinicalreview": [
        "hiv_test",
        "dm_test",
        "htn_test",
        "hiv_dx",
        "dm_dx",
        "htn_dx",
        "complications",
    ],
    "inte_subject.medications": ["refill_hiv", "refill_dm", "refill_htn"],
}

for reference_name, fields in configs.items():
    site_reference_configs.add_fields_to_config(name=reference_name, fields=fields)
