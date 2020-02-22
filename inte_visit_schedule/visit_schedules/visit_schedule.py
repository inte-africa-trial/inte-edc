from edc_visit_schedule import VisitSchedule, site_visit_schedules

from .schedule import schedule_hiv, schedule_ncd

VISIT_SCHEDULE = "visit_schedule"

visit_schedule = VisitSchedule(
    name=VISIT_SCHEDULE,
    verbose_name="INTE",
    offstudy_model="edc_offstudy.subjectoffstudy",
    death_report_model="inte_ae.deathreport",
    locator_model="edc_locator.subjectlocator",
    previous_visit_schedule=None,
)

visit_schedule.add_schedule(schedule_hiv)
visit_schedule.add_schedule(schedule_ncd)

site_visit_schedules.register(visit_schedule)
