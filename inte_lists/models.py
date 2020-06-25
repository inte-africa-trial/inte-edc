from edc_list_data.model_mixins import ListModelMixin


class ArvDrugs(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Arv Drugs"
        verbose_name_plural = "Arv Drugs"


class ArvRegimens(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "ARV Regimens"
        verbose_name_plural = "ARV Regimens"


class ClinicServices(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Clinic Services"
        verbose_name_plural = "Clinic Services"


class Conditions(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Conditions"
        verbose_name_plural = "Conditions"


class DiabetesTreatments(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Diabetes Treatments"
        verbose_name_plural = "Diabetes Treatments"


class HealthServices(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Health Services"
        verbose_name_plural = "Health Services"


class HypertensionTreatments(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Hypertension Treatments"
        verbose_name_plural = "Hypertension Treatments"


class OffstudyReasons(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Offstudy Reasons"
        verbose_name_plural = "Offstudy Reasons"


class RxModifications(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Treatment Modifications"
        verbose_name_plural = "Treatment Modifications"


class RxModificationReasons(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Treatment Modification Reasons"
        verbose_name_plural = "Treatment Modification Reasons"


class VisitReasons(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Visit Reasons"
        verbose_name_plural = "Visit Reasons"
