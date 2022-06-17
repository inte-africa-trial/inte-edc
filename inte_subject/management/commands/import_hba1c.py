import csv

from dateutil.parser import parse
from django.core.exceptions import ObjectDoesNotExist
from django.core.management import BaseCommand
from edc_registration.models import RegisteredSubject

from inte_subject.models import SubjectVisit


def import_hba1c(filename=None):
    """WIP, doesn't import anything yet"""
    filename = filename or "/Users/erikvw/Downloads/HbA1C results-ew.csv"
    with open(filename) as f:
        reader = csv.DictReader(
            f, fieldnames=["subject_identifier", "drawn_date", "result", "quantifier"]
        )
        for index, row in enumerate(reader):
            if index == 0:
                continue
            row.update(drawn_date=parse(row.get("drawn_date")))
            subject_visit = SubjectVisit.objects.filter(
                subject_identifier=row.get("subject_identifier")
            ).last()
            if not subject_visit:
                try:
                    RegisteredSubject.objects.get(
                        subject_identifier=row.get("subject_identifier")
                    )
                except ObjectDoesNotExist:
                    print(row.get("subject_identifier"))
                else:
                    print(f"? {row.get('subject_identifier')}")
            else:
                last_subject_visit = (
                    SubjectVisit.objects.filter(
                        subject_identifier=row.get("subject_identifier")
                    )
                    .order_by("report_datetime")
                    .last()
                )

                subject_visit = SubjectVisit.objects.filter(
                    subject_identifier=row.get("subject_identifier"),
                    report_datetime__date__gte=row.get("drawn_date"),
                ).first()

                if subject_visit:
                    print(
                        row.get("subject_identifier"),
                        row.get("drawn_date"),
                        f"{subject_visit.visit_code}.{subject_visit.visit_code_sequence}",
                        subject_visit.report_datetime,
                        (
                            f"{last_subject_visit.visit_code}."
                            f"{last_subject_visit.visit_code_sequence}"
                        ),
                        last_subject_visit.report_datetime,
                        0
                        if not subject_visit
                        else (
                            last_subject_visit.report_datetime - subject_visit.report_datetime
                        ).days,
                    )
                else:
                    print(
                        row.get("subject_identifier"),
                        row.get("drawn_date").date(),
                        "????????",
                        "????????",
                        (
                            f"{last_subject_visit.visit_code}."
                            f"{last_subject_visit.visit_code_sequence}"
                        ),
                        last_subject_visit.report_datetime.date(),
                    )


class Command(BaseCommand):

    help = "Import HbA1c results from CSV"

    def handle(self, *args, **options):

        import_hba1c()
