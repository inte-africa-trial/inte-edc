import pdb

from django import forms
from edc_constants.constants import OTHER
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator

from ..models import DrugRefillHiv


class DrugRefillHivFormValidator(FormValidator):
    def clean(self):
        self.m2m_other_specify(
            OTHER, m2m_field="modifications", field_other="modifications_other"
        )
        self.m2m_other_specify(
            OTHER,
            m2m_field="modification_reasons",
            field_other="modification_reasons_other",
        )


class DrugRefillHivForm(
    CrfModelFormMixin, forms.ModelForm,
):
    form_validator_cls = DrugRefillHivFormValidator

    class Meta:
        model = DrugRefillHiv
        fields = "__all__"
