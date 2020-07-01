from django import forms
from inte_lists.models import DiabetesTreatments

from ..models import DrugSupplyDiabetes
from .mixins import DrugSupplyNcdFormMixin


class DrugSupplyDiabetesForm(DrugSupplyNcdFormMixin, forms.ModelForm):
    list_model_cls = DiabetesTreatments
    relation_label = "drugsupplydiabetes"

    class Meta:
        model = DrugSupplyDiabetes
        fields = "__all__"
