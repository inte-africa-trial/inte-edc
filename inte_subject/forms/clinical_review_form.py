from django import forms
from edc_constants.constants import NO, NOT_APPLICABLE, YES
from edc_form_validators.form_validator import FormValidator
from inte_screening.constants import DIABETES_CLINIC, HIV_CLINIC, HYPERTENSION_CLINIC

from ..models import (
    ClinicalReview,
    DiabetesInitialReview,
    HivInitialReview,
    HypertensionInitialReview,
)
from ..morbidity import Morbidities
from .mixins import (
    CrfModelFormMixin,
    CrfFormValidatorMixin,
)


class ClinicalReviewFormValidator(CrfFormValidatorMixin, FormValidator):
    def clean(self):
        morbidities = Morbidities(
            subject_identifier=self.subject_identifier,
            report_datetime=self.report_datetime,
        )

        clinic_type = self.subject_screening.clinic_type
        if clinic_type == HYPERTENSION_CLINIC and not morbidities.is_hypertensive:
            raise forms.ValidationError(
                "Wait! Expected an Hypertension diagnosis at baseline. "
                f"Was {HypertensionInitialReview._meta.verbose_name} CRF completed?"
            )
        elif clinic_type == DIABETES_CLINIC and not morbidities.is_diabetic:
            raise forms.ValidationError(
                "Wait! Expected a Diabetes diagnosis at baseline. "
                f"Was {DiabetesInitialReview._meta.verbose_name} CRF completed?"
            )
        elif clinic_type == HIV_CLINIC and not morbidities.is_hiv_pos:
            raise forms.ValidationError(
                "Wait! Expected an HIV diagnosis at baseline. "
                f"Was {HivInitialReview._meta.verbose_name} CRF completed?"
            )

        self.applicable_if_true(
            not morbidities.is_hypertensive, field_applicable="hypertension_tested"
        )
        self.required_if(
            YES, field="hypertension_tested", field_required="hypertension_tested_date"
        )
        self.required_if(
            YES, field="hypertension_tested", field_required="hypertension_reason"
        )
        self.applicable_if(
            YES, field="hypertension_tested", field_applicable="hypertension_dx"
        )

        self.applicable_if_true(
            not morbidities.is_diabetic, field_applicable="diabetes_tested"
        )
        self.required_if(
            YES, field="diabetes_tested", field_required="diabetes_tested_date"
        )
        self.required_if(YES, field="diabetes_tested", field_required="diabetes_reason")
        self.applicable_if(YES, field="diabetes_tested", field_applicable="diabetes_dx")

        self.applicable_if_true(
            not morbidities.is_hiv_pos, field_applicable="hiv_tested"
        )
        self.required_if(YES, field="hiv_tested", field_required="hiv_tested_date")
        self.required_if(YES, field="hiv_tested", field_required="hiv_reason")
        self.applicable_if(YES, field="hiv_tested", field_applicable="hiv_dx")

    def raise_if_dx_and_applicable(self, clinic, cond):
        if self.subject_screening.clinic_type in [clinic] and self.cleaned_data.get(
            f"{cond}_tested"
        ) in [YES, NO]:
            raise forms.ValidationError(
                {
                    f"{cond}_tested": (
                        f"Not applicable. Patient was recruited from the {cond.title} clinic."
                    ),
                }
            )


class ClinicalReviewForm(CrfModelFormMixin, forms.ModelForm):

    form_validator_cls = ClinicalReviewFormValidator

    class Meta:
        model = ClinicalReview
        fields = "__all__"
