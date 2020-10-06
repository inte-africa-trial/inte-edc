from django import forms
from edc_constants.constants import YES
from edc_form_validators.form_validator import FormValidator
from edc_model.widgets import SliderWidget

from ..models import HtnMedicationAdherence
from .mixins import (
    CrfModelFormMixin,
    CrfFormValidatorMixin,
    MedicationAdherenceFormValidatorMixin,
)


class HtnMedicationAdherenceFormValidator(
    MedicationAdherenceFormValidatorMixin, CrfFormValidatorMixin, FormValidator,
):
    pass


class HtnMedicationAdherenceForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = HtnMedicationAdherenceFormValidator

    visual_score_slider = forms.CharField(
        label="Visual Score", widget=SliderWidget(attrs={"min": 0, "max": 100})
    )

    class Meta:
        model = HtnMedicationAdherence
        fields = "__all__"
