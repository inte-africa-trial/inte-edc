from django import forms

from inte_lists.models import DmTreatments

from ..models import DrugSupplyDm
from .mixins import DrugSupplyNcdFormMixin


class DrugSupplyDmForm(DrugSupplyNcdFormMixin, forms.ModelForm):
    list_model_cls = DmTreatments
    relation_label = "drugsupplydm"

    class Meta:
        model = DrugSupplyDm
        fields = "__all__"
