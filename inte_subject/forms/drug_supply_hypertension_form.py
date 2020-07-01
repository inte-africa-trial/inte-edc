from django import forms
from inte_lists.models import HypertensionTreatments

from ..models import DrugSupplyHypertension
from .mixins import DrugSupplyNcdFormMixin


class DrugSupplyHypertensionForm(DrugSupplyNcdFormMixin, forms.ModelForm):
    list_model_cls = HypertensionTreatments
    relation_label = "drugsupplyhypertension"

    class Meta:
        model = DrugSupplyHypertension
        fields = "__all__"
