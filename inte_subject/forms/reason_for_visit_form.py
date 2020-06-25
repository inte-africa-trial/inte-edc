from django import forms
from edc_constants.constants import DIABETES, HYPERTENSION, HIV, OTHER
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator


from ..models import ReasonForVisit
from .crf_form_validator_mixin import CrfFormValidatorMixin


class ReasonForVisitFormValidator(CrfFormValidatorMixin, FormValidator):
    def clean(self):
        self.m2m_other_specify(
            HYPERTENSION,
            m2m_field="health_services",
            field_other="hypertension_services",
        )
        self.m2m_other_specify(
            OTHER,
            m2m_field="hypertension_services",
            field_other="hypertension_services_other",
        )
        self.m2m_other_specify(
            DIABETES, m2m_field="health_services", field_other="diabetes_services"
        )
        self.m2m_other_specify(
            OTHER, m2m_field="diabetes_services", field_other="diabetes_services_other",
        )
        self.m2m_other_specify(
            HIV, m2m_field="health_services", field_other="hiv_services"
        )
        self.m2m_other_specify(
            OTHER, m2m_field="hiv_services", field_other="hiv_services_other",
        )


class ReasonForVisitForm(CrfModelFormMixin, forms.ModelForm):

    form_validator_cls = ReasonForVisitFormValidator

    class Meta:
        model = ReasonForVisit
        fields = "__all__"
