from django import forms
from edc_constants.constants import NO, YES
from edc_form_validators import FormValidator
from respond_forms.form_validator_mixins import DiagnosisFormValidatorMixin
from respond_forms.utils import raise_if_clinical_review_does_not_exist

from ..models import HealthEconomicsRevised
from .mixins import (
    CrfFormValidatorMixin,
    CrfModelFormMixin,
    HealthEconomicsFormValidatorMixin,
    raise_if_intervention_site_without_icc_registration,
)


class HealthEconomicsRevisedFormValidator(
    HealthEconomicsFormValidatorMixin,
    DiagnosisFormValidatorMixin,
    CrfFormValidatorMixin,
    FormValidator,
):
    def clean(self):
        raise_if_clinical_review_does_not_exist(self.cleaned_data.get("subject_visit"))

        raise_if_intervention_site_without_icc_registration()

        self.clean_education()

        self.required_if(NO, field="is_highest_earner", field_required="highest_earner")

        self.clean_recv_drugs_by_duration("month")

        self.clean_non_drug_activities_by_duration("month")

        self.validate_other_specify(
            field="missed_routine_activities",
            other_specify_field="missed_routine_activities_other",
        )

        self.required_if(
            YES,
            field="lost_income",
            field_required="lost_income_amount",
        )

        self.applicable_if(YES, field="childcare", field_applicable="childcare_source")

        self.validate_other_specify(
            field="childcare_source", other_specify_field="childcare_source_other"
        )

        self.validate_other_specify(field="transport", other_specify_field="transport_other")

        self.clean_recv_drugs_by_duration("today")

        self.clean_non_drug_activities_by_duration("today")

        self.required_if(YES, field="health_insurance", field_required="health_insurance_cost")

        self.required_if(YES, field="patient_club", field_required="patient_club_cost")

    def clean_non_drug_activities_by_duration(self, duration):
        self.required_if(
            YES,
            field=f"non_drug_activities_{duration}",
            field_required=f"non_drug_activities_detail_{duration}",
        )

        self.required_if(
            YES,
            field=f"non_drug_activities_{duration}",
            field_required=f"non_drug_activities_cost_{duration}",
        )


class HealthEconomicsRevisedForm(CrfModelFormMixin, forms.ModelForm):

    form_validator_cls = HealthEconomicsRevisedFormValidator

    class Meta:
        model = HealthEconomicsRevised
        fields = "__all__"
