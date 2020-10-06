from django import forms
from django.core.exceptions import ObjectDoesNotExist
from edc_constants.constants import NO, YES
from edc_form_validators.form_validator import FormValidator
from inte_subject.models import ClinicalReviewBaseline

from ..models import ClinicalReview
from ..diagnoses import Diagnoses, InitialReviewRequired
from .mixins import (
    CrfModelFormMixin,
    CrfFormValidatorMixin,
)


class ClinicalReviewFormValidator(CrfFormValidatorMixin, FormValidator):
    def clean(self):
        self.requires_clinical_review_at_baseline()

        diagnoses = Diagnoses(
            subject_identifier=self.subject_identifier,
            report_datetime=self.report_datetime,
        )

        try:
            diagnoses.initial_reviews
        except InitialReviewRequired as e:
            raise forms.ValidationError(e)

        # htn
        self.applicable_if_true(
            diagnoses.htn_dx != YES,
            field_applicable="htn_test",
            applicable_msg=(
                "Patient was not previously diagnosed with hypertension. "
                "Expected YES or NO."
            ),
            not_applicable_msg="Patient was previously diagnosed with hypertension.",
        )
        self.required_if(YES, field="htn_test", field_required="htn_test_date")
        self.required_if(YES, field="htn_test", field_required="htn_reason")
        self.applicable_if(YES, field="htn_test", field_applicable="htn_dx")

        # diabetes
        self.applicable_if_true(
            diagnoses.dm_dx != YES,
            field_applicable="dm_test",
            applicable_msg=(
                "Patient was not previously diagnosed with diabetes. "
                "Expected YES or NO."
            ),
            not_applicable_msg="Patient was previously diagnosed with diabetes.",
        )
        self.required_if(YES, field="dm_test", field_required="dm_test_date")
        self.required_if(YES, field="dm_test", field_required="dm_reason")
        self.applicable_if(YES, field="dm_test", field_applicable="dm_dx")

        # hiv
        self.applicable_if_true(
            diagnoses.hiv_dx != YES,
            field_applicable="hiv_test",
            applicable_msg=(
                "Patient was not previously diagnosed with HIV infection. "
                "Expected YES or NO."
            ),
            not_applicable_msg="Patient was previously diagnosed with HIV infection.",
        )
        self.required_if(YES, field="hiv_test", field_required="hiv_test_date")
        self.required_if(YES, field="hiv_test", field_required="hiv_reason")
        self.applicable_if(YES, field="hiv_test", field_applicable="hiv_dx")

        self.required_if(
            YES,
            field="health_insurance",
            field_required="health_insurance_monthly_pay",
            field_required_evaluate_as_int=True,
        )
        self.required_if(
            YES,
            field="patient_club",
            field_required="patient_club_monthly_pay",
            field_required_evaluate_as_int=True,
        )

    def raise_if_dx_and_applicable(self, clinic, cond):
        if self.subject_screening.clinic_type in [clinic] and self.cleaned_data.get(
            f"{cond}_test"
        ) in [YES, NO]:
            raise forms.ValidationError(
                {
                    f"{cond}_test": (
                        f"Not applicable. Patient was recruited from the {cond.title} clinic."
                    ),
                }
            )

    def requires_clinical_review_at_baseline(self):
        try:
            ClinicalReviewBaseline.objects.get(
                subject_visit__subject_identifier=self.subject_identifier
            )
        except ObjectDoesNotExist:
            raise forms.ValidationError(
                f"Please complete the {ClinicalReviewBaseline._meta.verbose_name} first."
            )


class ClinicalReviewForm(CrfModelFormMixin, forms.ModelForm):

    form_validator_cls = ClinicalReviewFormValidator

    class Meta:
        model = ClinicalReview
        fields = "__all__"
