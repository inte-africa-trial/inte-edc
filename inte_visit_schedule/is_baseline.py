from edc_visit_schedule.constants import DAY1


def is_baseline(subject_visit):
    return (
        subject_visit.appointment.visit_code == DAY1
        and subject_visit.appointment.visit_code_sequence == 0
    )
