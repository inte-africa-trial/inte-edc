from django.apps import apps as django_apps
from django.core.exceptions import ObjectDoesNotExist
from edc_constants.constants import YES


class InitialReviewRequired(Exception):
    pass


class ClinicalReviewBaselineRequired(Exception):
    pass


class DiagnosesError(Exception):
    pass


class Diagnoses:
    def __init__(
        self, subject_identifier=None, report_datetime=None, lte=None,
    ):
        self.lte = lte
        self.report_datetime = report_datetime
        self.subject_identifier = subject_identifier
        self.dm = self._get_dx("dm")
        self.hiv = self._get_dx("hiv")
        self.htn = self._get_dx("htn")
        self.diagnoses = dict(hiv=self.hiv, htn=self.htn, dm=self.dm)

    def get_dx_by_model(self, instance):
        if isinstance(instance, self.hiv_initial_review_model_cls):
            dx = self.hiv
        elif isinstance(instance, self.htn_initial_review_model_cls):
            dx = self.htn
        elif isinstance(instance, self.dm_initial_review_model_cls):
            dx = self.dm
        else:
            models = [
                self.hiv_initial_review_model_cls,
                self.htn_initial_review_model_cls,
                self.dm_initial_review_model_cls,
            ]
            raise DiagnosesError(f"Invalid. Expected an instance of one of {models}")
        return dx

    @property
    def dm_dx_date(self):
        if self.initial_reviews.get("dm"):
            return self.initial_reviews.get("dm").get_best_dx_date()
        return None

    @property
    def hiv_dx_date(self):
        if self.initial_reviews.get("hiv"):
            return self.initial_reviews.get("hiv").get_best_dx_date()
        return None

    @property
    def htn_dx_date(self):
        if self.initial_reviews.get("htn"):
            return self.initial_reviews.get("htn").get_best_dx_date()
        return None

    def _get_dx(self, name):
        """Returns YES if any diagnoses for this condition or `name`.

        name is `dm`, `hiv` or `htn`.
        """
        diagnoses = [
            getattr(self.clinical_review_baseline, f"{name}_dx") == YES,
            *[(getattr(obj, f"{name}_dx") == YES) for obj in self.clinical_reviews],
        ]
        if any(diagnoses):
            return YES
        return None

    @property
    def clinical_review_baseline(self):
        try:
            obj = self.clinical_review_baseline_model_cls.objects.get(
                subject_visit__subject_identifier=self.subject_identifier,
            )
        except ObjectDoesNotExist:
            raise ClinicalReviewBaselineRequired(
                f"Please complete {self.clinical_review_baseline_model_cls._meta.verbose_name}."
            )
        return obj

    def report_datetime_opts(self, prefix=None, lte=None):
        opts = {}
        prefix = prefix or ""
        if self.report_datetime:
            if lte or self.lte:
                opts.update({f"{prefix}report_datetime__lte": self.report_datetime})
            else:
                opts.update({f"{prefix}report_datetime__lt": self.report_datetime})
        return opts

    @property
    def clinical_reviews(self):
        return self.clinical_review_model_cls.objects.filter(
            subject_visit__subject_identifier=self.subject_identifier,
            **self.report_datetime_opts("subject_visit__"),
        )

    @property
    def previous_subject_visit(self):
        if self.report_datetime:
            return (
                self.subject_visit_model_cls.objects.filter(
                    subject_identifier=self.subject_identifier,
                    **self.report_datetime_opts(),
                )
                .order_by("report_datetime")
                .first()
            )
        return None

    @property
    def baseline_subject_visit(self):
        return (
            self.subject_visit_model_cls.objects.filter(
                subject_identifier=self.subject_identifier,
            )
            .order_by("report_datetime")
            .first()
        )

    @property
    def initial_reviews(self):
        """Returns a dict of initial review model instances
        for each diagnosis.

        If any initial review is expected butt does not exist,
        an expection is raised.
        """
        initial_reviews = {}
        options = (
            ("hiv", self.hiv, self.hiv_initial_review_model_cls, "An HIV diagnosis"),
            (
                "htn",
                self.htn,
                self.htn_initial_review_model_cls,
                "An hypertension diagnosis",
            ),
            ("dm", self.dm, self.dm_initial_review_model_cls, "A diabetes diagnosis"),
        )
        for name, diagnosis, initial_review_model_cls, description in options:
            if diagnosis:
                try:
                    obj = initial_review_model_cls.objects.get(
                        subject_visit__subject_identifier=self.subject_identifier,
                        **self.report_datetime_opts("subject_visit__", lte=True),
                    )
                except ObjectDoesNotExist:
                    subject_visit = (
                        self.previous_subject_visit or self.baseline_subject_visit
                    )
                    visit_label = f"{subject_visit.visit_code}.{subject_visit.visit_code_sequence}"
                    raise InitialReviewRequired(
                        f"{description} was been reported on visit {visit_label}. "
                        f"A `{initial_review_model_cls._meta.verbose_name}` "
                        "CRF is required for that visit."
                    )
                else:
                    initial_reviews.update({name: obj})
        return initial_reviews

    @property
    def dm_initial_review_model_cls(self):
        return django_apps.get_model("inte_subject.dminitialreview")

    @property
    def hiv_initial_review_model_cls(self):
        return django_apps.get_model("inte_subject.hivinitialreview")

    @property
    def htn_initial_review_model_cls(self):
        return django_apps.get_model("inte_subject.htninitialreview")

    @property
    def clinical_review_model_cls(self):
        return django_apps.get_model("inte_subject.clinicalreview")

    @property
    def clinical_review_baseline_model_cls(self):
        return django_apps.get_model("inte_subject.clinicalreviewbaseline")

    @property
    def subject_visit_model_cls(self):
        return django_apps.get_model("inte_subject.subjectvisit")
