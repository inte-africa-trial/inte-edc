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
        self.applicable_if_true(diagnoses.htn != YES, field_applicable="htn_test")
        self.required_if(YES, field="htn_test", field_required="htn_test_date")
        self.required_if(YES, field="htn_test", field_required="htn_reason")
        self.applicable_if(
            YES,
            field="htn_test",
            field_applicable="htn_dx",
            msg="This field is not applicable. Patient has been previously diagnosed with hypertension.",
        )

        # diabetes
        self.applicable_if_true(diagnoses.dm != YES, field_applicable="dm_test")
        self.required_if(YES, field="dm_test", field_required="dm_test_date")
        self.required_if(YES, field="dm_test", field_required="dm_reason")
        self.applicable_if(
            YES,
            field="dm_test",
            field_applicable="diabetes_dx",
            msg="This field is not applicable. Patient has been previously diagnosed with diabetes.",
        )

        # hiv
        self.applicable_if_true(diagnoses.hiv != YES, field_applicable="hiv_test")
        self.required_if(YES, field="hiv_test", field_required="hiv_test_date")
        self.required_if(YES, field="hiv_test", field_required="hiv_reason")
        self.applicable_if(
            YES,
            field="hiv_test",
            field_applicable="hiv_dx",
            msg="This field is not applicable. Patient has been previously diagnosed with HIV.",
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
