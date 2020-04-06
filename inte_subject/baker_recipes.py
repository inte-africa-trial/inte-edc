from dateutil.relativedelta import relativedelta
from django.contrib.sites.models import Site
from edc_constants.constants import YES, NO, MOBILE_NUMBER
from edc_utils import get_utcnow
from edc_visit_tracking.constants import SCHEDULED
from faker import Faker
from inte_consent.models import SubjectConsent
from inte_consent.models import SubjectReconsent
from model_bakery.recipe import Recipe, seq

from .models import SubjectRequisition
from .models import SubjectVisit


fake = Faker()


subjectvisit = Recipe(SubjectVisit, reason=SCHEDULED)

subjectrequisition = Recipe(SubjectRequisition)

subjectconsent = Recipe(
    SubjectConsent,
    assessment_score=YES,
    confirm_identity=seq("12315678"),
    consent_copy=YES,
    consent_datetime=get_utcnow(),
    consent_reviewed=YES,
    consent_signature=YES,
    dob=get_utcnow() - relativedelta(years=25),
    first_name=fake.first_name,
    gender="M",
    identity=seq("12315678"),
    identity_type=MOBILE_NUMBER,
    initials="XX",
    is_dob_estimated="-",
    is_incarcerated=NO,
    is_literate=YES,
    last_name=fake.last_name,
    screening_identifier=None,
    study_questions=YES,
    site=Site.objects.get_current(),
    subject_identifier=None,
)

subjectreconsent = Recipe(
    SubjectReconsent,
    site=Site.objects.get_current(),
    consent_reviewed=YES,
    assessment_score=YES,
    study_questions=YES,
    consent_copy=YES,
    action_identifier=None,
    tracking_identifier=None,
)
