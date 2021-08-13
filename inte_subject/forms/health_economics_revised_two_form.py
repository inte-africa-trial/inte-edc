from django import forms
from edc_constants.constants import YES
from edc_form_validators import FormValidator
from respond_forms.form_validator_mixins import DiagnosisFormValidatorMixin
from respond_forms.utils import raise_if_clinical_review_does_not_exist

from ..models import HealthEconomicsRevisedTwo
from .mixins import (
    CrfFormValidatorMixin,
    CrfModelFormMixin,
    HealthEconomicsFormValidatorMixin,
    raise_if_intervention_site_without_icc_registration,
)


class HealthEconomicsRevisedTwoFormValidator(
    HealthEconomicsFormValidatorMixin,
    DiagnosisFormValidatorMixin,
    CrfFormValidatorMixin,
    FormValidator,
):
    def clean(self):
        raise_if_clinical_review_does_not_exist(self.cleaned_data.get("subject_visit"))

        raise_if_intervention_site_without_icc_registration()

        self.clean_education()

        self.clean_recv_drugs_by_duration("month")

        self.clean_recv_drugs_by_duration("today")

        self.required_if(YES, field="health_insurance", field_required="health_insurance_cost")

        self.required_if(YES, field="patient_club", field_required="patient_club_cost")


class HealthEconomicsRevisedTwoForm(CrfModelFormMixin, forms.ModelForm):

    form_validator_cls = HealthEconomicsRevisedTwoFormValidator

    class Meta:
        model = HealthEconomicsRevisedTwo
        fields = "__all__"
