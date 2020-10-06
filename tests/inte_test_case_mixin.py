import string
from random import choices

from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
from edc_appointment.constants import (
    IN_PROGRESS_APPT,
    INCOMPLETE_APPT,
)
from edc_appointment.creators import UnscheduledAppointmentCreator
from edc_appointment.models import Appointment
from edc_auth.fix_export_permissions import ExportPermissionsFixer
from edc_auth.group_permissions_updater import GroupPermissionsUpdater
from edc_constants.constants import YES, NOT_APPLICABLE, RANDOM_SAMPLING, MALE, NO
from edc_facility.import_holidays import import_holidays
from edc_facility.models import Holiday
from edc_list_data.site_list_data import site_list_data
from edc_randomization.randomization_list_importer import RandomizationListImporter
from edc_sites import add_or_update_django_sites, get_sites_by_country
from edc_sites.tests.site_test_case_mixin import SiteTestCaseMixin
from edc_utils.date import get_utcnow
from edc_visit_schedule.constants import DAY1
from edc_visit_tracking.constants import SCHEDULED, UNSCHEDULED
from inte_auth.codenames_by_group import get_codenames_by_group
from inte_consent.models import SubjectConsent
from inte_screening.constants import HIV_CLINIC
from inte_screening.forms import SubjectScreeningForm
from inte_screening.models import SubjectScreening
from inte_sites.sites import fqdn
from inte_subject.models import SubjectVisit
from model_bakery import baker

from django.core.exceptions import ObjectDoesNotExist


class InteTestCaseMixin(SiteTestCaseMixin):
    fqdn = fqdn

    default_sites = get_sites_by_country("uganda")

    site_names = [s.name for s in default_sites]

    import_randomization_list = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        import_holidays(test=True)
        add_or_update_django_sites(sites=get_sites_by_country("uganda"))
        site_list_data.autodiscover()
        fixer = ExportPermissionsFixer(warn_only=True)
        fixer.fix()
        GroupPermissionsUpdater(
            codenames_by_group=get_codenames_by_group(), verbose=True
        )
        if cls.import_randomization_list:
            RandomizationListImporter(verbose=False, name="default")

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        Holiday.objects.all().delete()

    def login(self, user=None, superuser=None, groups=None):
        user = self.user if user is None else user
        superuser = True if superuser is None else superuser
        if not superuser:
            user.is_superuser = False
            user.is_active = True
            user.save()
            for group_name in groups:
                group = Group.objects.get(name=group_name)
                user.groups.add(group)
        return self.client.force_login(user or self.user)

    def get_subject_screening(
        self, report_datetime=None, eligibility_datetime=None, **kwargs
    ):
        data = {
            "screening_consent": YES,
            "age_in_years": 25,
            "clinic_type": HIV_CLINIC,
            "gender": MALE,
            "hospital_identifier": "13343322",
            "initials": "".join(choices(string.ascii_uppercase, k=2)),
            "lives_nearby": YES,
            "qualifying_condition": YES,
            "report_datetime": report_datetime or get_utcnow(),
            "requires_acute_care": NO,
            "selection_method": RANDOM_SAMPLING,
            "unsuitable_agreed": NOT_APPLICABLE,
            "unsuitable_for_study": NO,
        }
        data.update(**kwargs)
        form = SubjectScreeningForm(data=data, instance=None)
        form.save()

        subject_screening = SubjectScreening.objects.get(
            screening_identifier=form.instance.screening_identifier
        )

        self.assertTrue(subject_screening.eligible)

        if eligibility_datetime:
            subject_screening.eligibility_datetime = eligibility_datetime
            subject_screening.save()

        return subject_screening

    def get_subject_consent(
        self, subject_screening, consent_datetime=None, site_name=None, **kwargs
    ):
        site_name = site_name or "kinoni"
        options = dict(
            user_created="erikvw",
            user_modified="erikvw",
            screening_identifier=subject_screening.screening_identifier,
            initials=subject_screening.initials,
            dob=get_utcnow().date()
            - relativedelta(years=subject_screening.age_in_years),
            site=Site.objects.get(name=site_name),
            clinic_type=HIV_CLINIC,
            consent_datetime=consent_datetime or get_utcnow(),
        )
        options.update(**kwargs)
        return baker.make_recipe("inte_consent.subjectconsent", **options)

    def get_appointment(
        self,
        subject_identifier=None,
        visit_code=None,
        visit_code_sequence=None,
        reason=None,
        appt_datetime=None,
    ):
        appointment = Appointment.objects.get(
            subject_identifier=subject_identifier,
            visit_code=visit_code,
            visit_code_sequence=visit_code_sequence,
        )
        if appt_datetime:
            appointment.appt_datetime = appt_datetime
            appointment.save()
            appointment.refresh_from_db()
        if reason == UNSCHEDULED:
            appointment = self.create_unscheduled_appointment(appointment)
        appointment.appt_status = IN_PROGRESS_APPT
        appointment.save()
        appointment.refresh_from_db()
        return appointment

    @staticmethod
    def create_unscheduled_appointment(appointment):
        appointment.appt_status = INCOMPLETE_APPT
        appointment.save()
        appointment.refresh_from_db()
        appt_creator = UnscheduledAppointmentCreator(
            subject_identifier=appointment.subject_identifier,
            visit_schedule_name=appointment.visit_schedule_name,
            schedule_name=appointment.schedule_name,
            visit_code=appointment.visit_code,
            facility=appointment.facility,
        )
        return appt_creator.appointment

    def get_subject_visit(
        self,
        visit_code=None,
        visit_code_sequence=None,
        subject_screening=None,
        subject_consent=None,
        reason=None,
        appointment=None,
        appt_datetime=None,
    ):
        reason = reason or SCHEDULED
        if not appointment:
            subject_screening = subject_screening or self.get_subject_screening()
            subject_consent = subject_consent or self.get_subject_consent(
                subject_screening
            )
            appointment = self.get_appointment(
                subject_identifier=subject_consent.subject_identifier,
                visit_code=visit_code or DAY1,
                visit_code_sequence=(
                    visit_code_sequence if visit_code_sequence is not None else 0
                ),
                reason=reason,
                appt_datetime=appt_datetime,
            )
        return SubjectVisit.objects.create(appointment=appointment, reason=reason)

    def get_next_subject_visit(
        self, subject_visit=None, reason=None, appt_datetime=None,
    ):
        visit_code = (
            subject_visit.appointment.visit_code
            if reason == UNSCHEDULED
            else subject_visit.appointment.next.visit_code
        )
        # visit_code_sequence will increment in get_subject_visit
        visit_code_sequence = (
            subject_visit.appointment.visit_code_sequence
            if reason == UNSCHEDULED
            else 0
        )
        return self.get_subject_visit(
            visit_code=visit_code,
            visit_code_sequence=visit_code_sequence,
            reason=reason,
            appt_datetime=appt_datetime,
            subject_screening=SubjectScreening.objects.get(
                subject_identifier=subject_visit.subject_identifier
            ),
            subject_consent=SubjectConsent.objects.get(
                subject_identifier=subject_visit.subject_identifier
            ),
        )
