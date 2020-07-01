from django import forms
from inte_lists.models import DiabetesTreatments

from ..models import DrugSupplyDiabetes
from .mixins import DrugSupplyNcdFormMixin


class DrugSupplyDiabetesForm(DrugSupplyNcdFormMixin, forms.ModelForm):
    class Meta:
        model = DrugSupplyDiabetes
        fields = "__all__"
