from django import forms
from edc_constants.constants import DIABETES, HIV, HYPERTENSION, OTHER, REFILL
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator

from ..models import ReasonForVisit
from .crf_form_validator_mixin import CrfFormValidatorMixin


class ReasonForVisitFormValidator(CrfFormValidatorMixin, FormValidator):
    def clean(self):
        self.m2m_other_specify(
            OTHER, m2m_field="clinic_services", field_other="clinic_services_other",
        )

        is_refill = REFILL in self.get_m2m_selected(m2m_field="clinic_services")
        self.applicable_if_true(
            is_refill
            and HYPERTENSION in self.get_m2m_selected(m2m_field="health_services"),
            field_applicable="refill_hypertension",
        )
        self.applicable_if_true(
            is_refill
            and DIABETES in self.get_m2m_selected(m2m_field="health_services"),
            field_applicable="refill_diabetes",
        )
        self.applicable_if_true(
            is_refill and HIV in self.get_m2m_selected(m2m_field="health_services"),
            field_applicable="refill_hiv",
        )


class ReasonForVisitForm(CrfModelFormMixin, forms.ModelForm):

    form_validator_cls = ReasonForVisitFormValidator

    class Meta:
        model = ReasonForVisit
        fields = "__all__"
