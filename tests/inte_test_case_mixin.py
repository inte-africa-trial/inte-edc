import string
from random import choices

from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
from edc_appointment.constants import IN_PROGRESS_APPT
from edc_appointment.models import Appointment
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
from edc_visit_tracking.constants import SCHEDULED
from inte_auth.codenames_by_group import get_codenames_by_group
from inte_screening.constants import HIV_CLINIC
from inte_screening.forms import SubjectScreeningForm
from inte_screening.models import SubjectScreening
from inte_sites.sites import fqdn
from inte_subject.models import SubjectVisit
from model_bakery import baker


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

    def get_subject_consent(self, subject_screening, site_name=None, **kwargs):
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
        )
        options.update(**kwargs)
        return baker.make_recipe("inte_consent.subjectconsent", **options)

    def get_subject_visit(
        self, visit_code=None, subject_screening=None, subject_consent=None
    ):
        visit_code = visit_code or DAY1
        subject_screening = subject_screening or self.get_subject_screening()
        subject_consent = subject_consent or self.get_subject_consent(subject_screening)
        subject_identifier = subject_consent.subject_identifier

        appointment = Appointment.objects.get(
            subject_identifier=subject_identifier, visit_code=visit_code
        )
        appointment.appt_status = IN_PROGRESS_APPT
        appointment.save()
        return SubjectVisit.objects.create(appointment=appointment, reason=SCHEDULED)
