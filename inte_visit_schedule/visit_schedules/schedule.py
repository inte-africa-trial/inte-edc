from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Schedule, Visit as BaseVisit
from edc_visit_schedule.constants import (
    DAY1,
    MONTH6,
    MONTH12,
)

from .crfs import (
    crfs_d1,
    crfs_6m,
    crfs_12m,
    crfs_missed,
    crfs_prn as default_crfs_prn,
    crfs_unscheduled as default_crfs_unscheduled,
)
from .requisitions import (
    requisitions_d1,
    requisitions_6m,
    requisitions_12m,
)

default_requisitions = None

SCHEDULE_HIV = "schedule_hiv"
SCHEDULE_NCD = "schedule_ncd"


class Visit(BaseVisit):
    def __init__(
        self,
        crfs_unscheduled=None,
        requisitions_unscheduled=None,
        crfs_prn=None,
        requisitions_prn=None,
        allow_unscheduled=None,
        **kwargs
    ):
        super().__init__(
            allow_unscheduled=True if allow_unscheduled is None else allow_unscheduled,
            crfs_unscheduled=crfs_unscheduled or default_crfs_unscheduled,
            requisitions_unscheduled=requisitions_unscheduled or default_requisitions,
            crfs_prn=crfs_prn or default_crfs_prn,
            requisitions_prn=requisitions_prn,  # or default_requisitions_prn,
            crfs_missed=crfs_missed,
            **kwargs
        )


# schedule for new participants
schedule_hiv = Schedule(
    name=SCHEDULE_HIV,
    verbose_name="Day 1 to Month 12",
    onschedule_model="inte_prn.onschedulehiv",
    offschedule_model="inte_prn.endofstudy",
    consent_model="inte_consent.subjectconsent",
    appointment_model="edc_appointment.appointment",
)

schedule_ncd = Schedule(
    name=SCHEDULE_NCD,
    verbose_name="Day 1 to Month 12",
    onschedule_model="inte_prn.onschedulencd",
    offschedule_model="inte_prn.endofstudy",
    consent_model="inte_consent.subjectconsent",
    appointment_model="edc_appointment.appointment",
)

visit00 = Visit(
    code=DAY1,
    title="Day 1",
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions_d1,
    crfs=crfs_d1,
    facility_name="5-day-clinic",
)


visit06 = Visit(
    code=MONTH6,
    title="Month 6",
    timepoint=6,
    rbase=relativedelta(months=6),
    rlower=relativedelta(months=1),
    rupper=relativedelta(months=5),
    requisitions=requisitions_6m,
    crfs=crfs_6m,
    facility_name="5-day-clinic",
)

visit12 = Visit(
    code=MONTH12,
    title="Month 12",
    timepoint=12,
    rbase=relativedelta(months=12),
    rlower=relativedelta(months=1),
    rupper=relativedelta(months=3),
    requisitions=requisitions_12m,
    crfs=crfs_12m,
    facility_name="5-day-clinic",
)

schedule_hiv.add_visit(visit=visit00)
schedule_hiv.add_visit(visit=visit06)
schedule_hiv.add_visit(visit=visit12)

schedule_ncd.add_visit(visit=visit00)
schedule_ncd.add_visit(visit=visit06)
schedule_ncd.add_visit(visit=visit12)
