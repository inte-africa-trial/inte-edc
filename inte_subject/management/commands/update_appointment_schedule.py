from django.core.management import BaseCommand

from inte_subject.update_appointment_schedule import update_appointment_schedule


class Command(BaseCommand):

    help = "Update appointments and subejctvisit after changes to pre-6m schedule"

    def handle(self, *args, **options):

        update_appointment_schedule()
