from django import forms

from inte_lists.models import HtnTreatments

from ..models import DrugSupplyHtn
from .mixins import DrugSupplyNcdFormMixin


class DrugSupplyHtnForm(DrugSupplyNcdFormMixin, forms.ModelForm):
    list_model_cls = HtnTreatments
    relation_label = "drugsupplyhtn"

    class Meta:
        model = DrugSupplyHtn
        fields = "__all__"
