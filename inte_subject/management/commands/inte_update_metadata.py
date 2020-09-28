from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from edc_appointment.constants import CANCELLED_APPT, NEW_APPT
from edc_appointment.models import Appointment
from edc_visit_schedule import site_visit_schedules
from tqdm import tqdm

from ...models import SubjectVisit, ClinicalReview, ClinicalReviewBaseline, Medications


class UpdateCrfMetadataOnDataChange:
    """Updates metadata by looping through all subject visits and
    ClinicalReviewBaseline, ClinicalReview, Medications models.

    The list of models would need to be updated as predicates change.

    This takes a long time so run in a separate thread.
    """

    def __init__(self):
        visit_schedule = site_visit_schedules.get_visit_schedule("visit_schedule")
        for schedule in tqdm(visit_schedule.schedules.values()):
            for visit_code, visit in schedule.visits.items():
                for appointment in self.appointments_for(visit_code):
                    try:
                        subject_visit = SubjectVisit.objects.get(
                            appointment=appointment
                        )
                    except ObjectDoesNotExist:
                        pass
                    else:
                        subject_visit.save()
                        for model_cls in tqdm(
                            [ClinicalReviewBaseline, ClinicalReview, Medications]
                        ):
                            try:
                                obj = model_cls.objects.get(subject_visit=subject_visit)
                            except ObjectDoesNotExist:
                                pass
                            else:
                                obj.update_reference_on_save()
                                obj.metadata_update()
                                obj.run_metadata_rules_for_crf()

    @staticmethod
    def appointments_for(visit_code):
        return (
            Appointment.objects.filter(visit_code=visit_code)
            .exclude(appt_status__in=[NEW_APPT, CANCELLED_APPT])
            .order_by("subject_identifier", "visit_code", "visit_code_sequence")
        )

    @staticmethod
    def update_subject_visit_for(appointment):
        try:
            subject_visit = SubjectVisit.objects.get(appointment=appointment)
        except ObjectDoesNotExist:
            pass
        else:
            subject_visit.save()


class Command(BaseCommand):

    help = "Update metadata by visit schedule"

    def handle(self, *args, **options):

        UpdateCrfMetadataOnDataChange()
