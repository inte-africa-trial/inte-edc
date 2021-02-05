from decimal import Decimal

from django.apps import apps as django_apps
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import pre_delete, pre_save
from edc_utils import DisableSignals
from tqdm import tqdm


def update_appointment_schedule(apps=None):
    apps = apps or django_apps
    registered_subject_model_cls = apps.get_model("edc_registration.registeredsubject")
    appointment_model_cls = apps.get_model("edc_appointment.appointment")
    subject_visit_model_cls = apps.get_model("inte_subject.subjectvisit")
    crfmetadata_model_cls = apps.get_model("edc_metadata.crfmetadata")
    for registered_subject in tqdm(
        registered_subject_model_cls.objects.all().order_by("subject_identifier")
    ):
        for index, appointment in enumerate(
            appointment_model_cls.objects.filter(
                subject_identifier=registered_subject.subject_identifier,
            ).order_by("timepoint")
        ):
            if appointment.timepoint in [
                Decimal("0.0"),
                Decimal("6.0"),
                Decimal("12.0"),
            ]:
                continue
            elif appointment.timepoint < Decimal("6.0"):
                appointment.visit_code = "1000"
                appointment.visit_code_sequence = index
                appointment.timepoint = Decimal("0.0")
                with DisableSignals(disabled_signals=[pre_save]):
                    appointment.save()
                appointment.refresh_from_db()
                try:
                    subject_visit = subject_visit_model_cls.objects.get(
                        appointment=appointment
                    )
                except ObjectDoesNotExist:
                    appointment.delete()
                else:
                    crfmetadata_model_cls.objects.filter(
                        subject_identifier=registered_subject.subject_identifier,
                        visit_code=subject_visit.visit_code,
                        visit_code_sequence=subject_visit.visit_code_sequence,
                    ).update(
                        visit_code=appointment.visit_code,
                        visit_code_sequence=appointment.visit_code_sequence,
                        timepoint=appointment.timepoint,
                    )
                    with DisableSignals(disabled_signals=[pre_save]):
                        subject_visit.visit_code = appointment.visit_code
                        subject_visit.visit_code_sequence = appointment.visit_code_sequence
                        subject_visit.save()
            else:
                with DisableSignals(disabled_signals=[pre_delete]):
                    appointment.delete()

    for appointment in appointment_model_cls.objects.filter(visit_code_sequence__gt=0):
        try:
            subject_visit_model_cls.objects.get(appointment=appointment)
        except ObjectDoesNotExist:
            appointment.delete()
