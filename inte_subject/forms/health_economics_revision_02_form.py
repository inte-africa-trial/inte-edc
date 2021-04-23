from django import forms
from edc_constants.constants import YES
from edc_form_validators import FormValidator

from ..models import HealthEconomicsRevision02
from .mixins import (
    CrfFormValidatorMixin,
    CrfModelFormMixin,
    DiagnosisFormValidatorMixin,
    HealthEconomicsFormValidatorMixin,
    raise_if_clinical_review_does_not_exist,
)


class HealthEconomicsRevision02FormValidator(
    HealthEconomicsFormValidatorMixin,
    DiagnosisFormValidatorMixin,
    CrfFormValidatorMixin,
    FormValidator,
):
    def clean(self):
        raise_if_clinical_review_does_not_exist(self.cleaned_data.get("subject_visit"))

        self.require_icc_registration()

        self.clean_education()

        self.clean_recv_drugs_by_duration("month")

        self.clean_recv_drugs_by_duration("today")

        self.required_if(YES, field="health_insurance", field_required="health_insurance_cost")

        self.required_if(YES, field="patient_club", field_required="patient_club_cost")


class HealthEconomicsRevision02Form(CrfModelFormMixin, forms.ModelForm):

    form_validator_cls = HealthEconomicsRevision02FormValidator

    class Meta:
        model = HealthEconomicsRevision02
        fields = "__all__"
