from django import forms
from django.contrib.sites.models import Site
from django.core.exceptions import ObjectDoesNotExist
from edc_constants.constants import FREE_OF_CHARGE, YES, NO
from edc_form_validators.form_validator import FormValidator
from inte_lists.models import DrugPaySources
from inte_prn.models import IntegratedCareClinicRegistration
from inte_sites.is_intervention_site import is_intervention_site

from ..models import HealthEconomicsRevised
from .mixins import CrfFormValidatorMixin, CrfModelFormMixin, model_exists_or_raise


class HealthEconomicsRevisedFormValidator(CrfFormValidatorMixin, FormValidator):
    def clean(self):
        self.require_icc_registration()

        self.clean_education()

        self.required_if(NO, field="is_highest_earner", field_required="highest_earner")

        self.clean_recv_drugs_by_duration("month")

        self.clean_non_drug_activities_by_duration("month")

        self.validate_other_specify(
            field="missed_routine_activities",
            other_specify_field="missed_routine_activities_other",
        )

        self.required_if(
            YES, field="lost_income", field_required="lost_income_amount",
        )

        self.applicable_if(YES, field="childcare", field_applicable="childcare_source")

        self.validate_other_specify(
            field="childcare_source", other_specify_field="childcare_source_other"
        )

        self.validate_other_specify(
            field="transport", other_specify_field="transport_other"
        )

        self.clean_recv_drugs_by_duration("today")

        self.clean_non_drug_activities_by_duration("today")

        self.required_if(
            YES, field="health_insurance", field_required="health_insurance_cost"
        )

        self.required_if(YES, field="patient_club", field_required="patient_club_cost")

    @staticmethod
    def require_icc_registration():
        if is_intervention_site():
            try:
                IntegratedCareClinicRegistration.objects.get(
                    site_id=Site.objects.get_current()
                )
            except ObjectDoesNotExist:
                raise forms.ValidationError(
                    "This is an intervention site. Complete the "
                    f"`{IntegratedCareClinicRegistration._meta.verbose_name}` form first."
                )

    def clean_education(self):
        cond = (
            self.cleaned_data.get("education_in_years") is not None
            and self.cleaned_data.get("education_in_years") > 0
        )

        if cond and self.cleaned_data.get("education_in_years") > self.age_in_years:
            raise forms.ValidationError(
                {
                    "education_in_years": (
                        "Cannot exceed subject's age. "
                        f"Got subject is {self.age_in_years} years old."
                    )
                }
            )

        self.required_if_true(cond, field_required="education_certificate")

        self.applicable_if_true(cond, field_applicable="primary_school")
        self.required_if(
            YES,
            field="primary_school",
            field_required="primary_school_in_years",
            field_required_evaluate_as_int=True,
        )
        self.applicable_if_true(cond, field_applicable="secondary_school")
        self.required_if(
            YES,
            field="secondary_school",
            field_required="secondary_school_in_years",
            field_required_evaluate_as_int=True,
        )
        self.applicable_if_true(cond, field_applicable="higher_education")
        self.required_if(
            YES,
            field="higher_education",
            field_required="higher_education_in_years",
            field_required_evaluate_as_int=True,
        )

    def clean_recv_drugs_by_duration(self, duration):
        conditions = ["dm", "htn", "hiv", "other"]
        for cond in conditions:
            self.applicable_if(
                YES,
                field=f"received_rx_{duration}",
                field_applicable=f"rx_{cond}_{duration}",
            )
            self.m2m_required_if(
                response=YES,
                field=f"rx_{cond}_{duration}",
                m2m_field=f"rx_{cond}_paid_{duration}",
            )
            self.m2m_single_selection_if(
                FREE_OF_CHARGE, m2m_field=f"rx_{cond}_paid_{duration}"
            )
            self.m2m_other_specify(
                *[
                    obj.name
                    for obj in DrugPaySources.objects.all()
                    if obj.name != FREE_OF_CHARGE
                ],
                m2m_field=f"rx_{cond}_paid_{duration}",
                field_other=f"rx_{cond}_cost_{duration}",
            )

        responses = [self.cleaned_data.get(f"rx_{k}_{duration}") for k in conditions]
        if self.cleaned_data.get(f"received_rx_{duration}") == YES and all(
            [r == NO for r in responses]
        ):
            raise forms.ValidationError(
                {
                    f"received_rx_{duration}": (
                        "Invalid. Must have received at least one type "
                        "of drug below if `YES`."
                    )
                }
            )

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
