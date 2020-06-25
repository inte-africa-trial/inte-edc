from django import forms
from edc_model import models as edc_models


class EstimatedDateFromAgoFormMixin:
    def estimated_date_from_ago(self, f1):
        estimated_date = None
        if self.cleaned_data.get(f1):
            estimated_date = edc_models.duration_to_date(
                self.cleaned_data.get(f1),
                self.cleaned_data.get("report_datetime").date(),
            )
        return estimated_date


class DrugSupplyNcdFormMixin:
    def clean(self):
        cleaned_data = super().clean()
        if self.cleaned_data.get("drug") and self.cleaned_data.get("drug").name not in [
            obj.name for obj in self.cleaned_data.get("drug_refill").rx.all()
        ]:
            rx = " + ".join(
                [obj.name for obj in self.cleaned_data.get("drug_refill").rx.all()]
            )
            raise forms.ValidationError(
                f"Invalid. `{self.cleaned_data.get('drug').display_name}` "
                f"not in current treatment of `{rx}`"
            )
        return cleaned_data
