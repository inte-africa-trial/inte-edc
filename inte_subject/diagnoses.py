from django.apps import apps as django_apps
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from edc_constants.constants import YES


class InitialReviewRequired(Exception):
    pass


class MultipleInitialReviewsExist(Exception):
    pass


class ClinicalReviewBaselineRequired(Exception):
    pass


class DiagnosesError(Exception):
    pass


class Diagnoses:
    def __init__(
        self,
        subject_identifier=None,
        report_datetime=None,
        subject_visit=None,
        lte=None,
    ):
        if subject_visit:
            if subject_identifier or report_datetime:
                raise DiagnosesError(
                    "Ambiguous parameters provided. Expected either "
                    "`subject_visit` or `subject_identifier, report_datetime`. Not both."
                )
            self.report_datetime = subject_visit.report_datetime
            self.subject_identifier = subject_visit.appointment.subject_identifier
        else:
            self.report_datetime = report_datetime
            self.subject_identifier = subject_identifier
        self.lte = lte
        self.dm_dx = self._get_dx("dm")
        self.hiv_dx = self._get_dx("hiv")
        self.htn_dx = self._get_dx("htn")

    def get_dx_by_model(self, instance):
        if isinstance(instance, self.hiv_initial_review_model_cls):
            dx = self.hiv_dx
        elif isinstance(instance, self.htn_initial_review_model_cls):
            dx = self.htn_dx
        elif isinstance(instance, self.dm_initial_review_model_cls):
            dx = self.dm_dx
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
        """Returns YES if any diagnoses for this condition otherwise None.

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
                "Please complete "
                f"{self.clinical_review_baseline_model_cls._meta.verbose_name}."
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

        If any initial review is expected but does not exist,
        an expection is raised.
        """
        initial_reviews = {}
        options = (
            ("hiv", self.hiv_dx, self.hiv_initial_review_model_cls, "An HIV diagnosis"),
            (
                "htn",
                self.htn_dx,
                self.htn_initial_review_model_cls,
                "An hypertension diagnosis",
            ),
            (
                "dm",
                self.dm_dx,
                self.dm_initial_review_model_cls,
                "A diabetes diagnosis",
            ),
        )
        for name, diagnosis, initial_review_model_cls, description in options:
            if diagnosis:
                try:
                    obj = initial_review_model_cls.objects.get(
                        subject_visit__subject_identifier=self.subject_identifier,
                        **self.report_datetime_opts("subject_visit__", lte=True),
                    )
                except ObjectDoesNotExist:
                    subject_visit = self.initial_diagnosis_visit(name)
                    visit_label = (
                        f"{subject_visit.visit_code}." f"{subject_visit.visit_code_sequence}"
                    )
                    raise InitialReviewRequired(
                        f"{description} was been reported on visit {visit_label}. "
                        f"Complete the `{initial_review_model_cls._meta.verbose_name}` "
                        "CRF first."
                    )
                except MultipleObjectsReturned:
                    qs = initial_review_model_cls.objects.filter(
                        subject_visit__subject_identifier=self.subject_identifier,
                        **self.report_datetime_opts("subject_visit__", lte=True),
                    ).order_by(
                        "subject_visit__visit_code",
                        "subject_visit__visit_code_sequence",
                    )
                    visits_str = ", ".join(
                        [
                            (
                                f"{obj.subject_visit.visit_code}."
                                f"{obj.subject_visit.visit_code_sequence}"
                            )
                            for obj in qs
                        ]
                    )
                    raise MultipleInitialReviewsExist(
                        f"More than one `{initial_review_model_cls._meta.verbose_name}` "
                        f"has been submitted. "
                        f"This needs to be corrected. Try removing all but the first "
                        f"`{initial_review_model_cls._meta.verbose_name}` "
                        "before continuing. "
                        f"`{initial_review_model_cls._meta.verbose_name}` "
                        "CRFs have been submitted "
                        f"for visits {visits_str}"
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

    def initial_diagnosis_visit(self, name):
        try:
            clinical_review_baseline = self.clinical_review_baseline_model_cls.objects.get(
                subject_visit__subject_identifier=self.subject_identifier,
                **self.report_datetime_opts("subject_visit__", lte=True),
                **{f"{name}_dx": YES},
            )
        except ObjectDoesNotExist:
            subject_visit = None
        else:
            subject_visit = clinical_review_baseline.subject_visit
        if not subject_visit:
            try:
                clinical_review = self.clinical_review_model_cls.objects.get(
                    subject_visit__subject_identifier=self.subject_identifier,
                    **self.report_datetime_opts("subject_visit__", lte=True),
                    **{f"{name}_dx": YES},
                )
            except ObjectDoesNotExist:
                subject_visit = None
            else:
                subject_visit = clinical_review.subject_visit
        return subject_visit
