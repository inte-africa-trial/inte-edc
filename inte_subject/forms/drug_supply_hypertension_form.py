from django import forms

from ..models import DrugSupplyHypertension
from .mixins import DrugSupplyNcdFormMixin


class DrugSupplyHypertensionForm(DrugSupplyNcdFormMixin, forms.ModelForm):
    class Meta:
        model = DrugSupplyHypertension
        fields = "__all__"
