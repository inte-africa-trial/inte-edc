from django import forms
from django.contrib.sites.models import Site
from django.core.exceptions import ObjectDoesNotExist
from edc_constants.constants import FREE_OF_CHARGE, OTHER, YES
from edc_form_validators.form_validator import FormValidator

from inte_lists.models import DrugPaySources
from inte_prn.models import IntegratedCareClinicRegistration
from inte_sites.is_intervention_site import is_intervention_site

from ..models import HealthEconomicsShort
from .mixins import (
    CrfFormValidatorMixin,
    CrfModelFormMixin,
    DiagnosisFormValidatorMixin,
    raise_if_clinical_review_does_not_exist,
)


class HealthEconomicsShortFormValidator(
    DiagnosisFormValidatorMixin, CrfFormValidatorMixin, FormValidator
):
    def clean(self):
        raise_if_clinical_review_does_not_exist(self.cleaned_data.get("subject_visit"))

        self.require_icc_registration()

        self.clean_education()

        self.clean_recv_drugs_by_duration("month")

        self.clean_recv_drugs_by_duration("today")

        self.required_if(YES, field="health_insurance", field_required="health_insurance_cost")

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
        conditions = [
            ("dm", "diabetes"),
            ("htn", "hypertension"),
            ("hiv", "HIV"),
            ("other", None),
        ]
        diagnoses = self.get_diagnoses()
        for cond, label in conditions:

            if cond == "other":
                self.applicable_if(
                    YES,
                    field=f"received_rx_{duration}",
                    field_applicable=f"rx_{cond}_{duration}",
                )
            else:
                if self.cleaned_data.get(f"received_rx_{duration}") == YES:
                    self.applicable_if_diagnosed(
                        diagnoses=diagnoses,
                        field_dx=f"{cond}_dx",
                        field_applicable=f"rx_{cond}_{duration}",
                        label=label,
                    )
                else:
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
                OTHER,
                m2m_field=f"rx_{cond}_paid_{duration}",
                field_other=f"rx_{cond}_paid_{duration}_other",
            )
            self.m2m_other_specify(
                *[
                    obj.name
                    for obj in DrugPaySources.objects.all()
                    if obj.name != FREE_OF_CHARGE
                ],
                m2m_field=f"rx_{cond}_paid_{duration}",
                field_other=f"rx_{cond}_cost_{duration}",
                field_other_evaluate_as_int=True,
            )


class HealthEconomicsShortForm(CrfModelFormMixin, forms.ModelForm):

    form_validator_cls = HealthEconomicsShortFormValidator

    class Meta:
        model = HealthEconomicsShort
        fields = "__all__"
