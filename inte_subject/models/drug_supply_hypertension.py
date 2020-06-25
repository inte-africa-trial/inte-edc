from django.db import models
from edc_model import models as edc_models
from inte_lists.models import HypertensionTreatments
from inte_subject.models import DrugRefillHypertension

from ..model_mixins import DrugSupplyModelMixin


class DrugSupplyHypertension(DrugSupplyModelMixin, edc_models.BaseUuidModel):

    drug_refill = models.ForeignKey(DrugRefillHypertension, on_delete=models.PROTECT)

    drug = models.ForeignKey(HypertensionTreatments, on_delete=models.PROTECT)

    class Meta(edc_models.BaseUuidModel.Meta):
        verbose_name = "Drug Supply: Hypertension"
        verbose_name_plural = "Drug Supply: Hypertension"
