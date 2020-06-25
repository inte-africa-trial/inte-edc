from django.db import models
from edc_model import models as edc_models
from inte_lists.models import DiabetesTreatments
from inte_subject.models import DrugRefillDiabetes

from ..model_mixins import DrugSupplyModelMixin


class DrugSupplyDiabetes(DrugSupplyModelMixin, edc_models.BaseUuidModel):

    drug_refill = models.ForeignKey(DrugRefillDiabetes, on_delete=models.PROTECT)

    drug = models.ForeignKey(DiabetesTreatments, on_delete=models.PROTECT)

    class Meta(edc_models.BaseUuidModel.Meta):
        verbose_name = "Drug Supply: Diabetes"
        verbose_name_plural = "Drug Supply: Diabetes"
