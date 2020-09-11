from django import forms
from edc_constants.constants import YES
from edc_form_validators.form_validator import FormValidator

from ..constants import INSULIN, DRUGS
from ..models import DmInitialReview
from .mixins import (
    EstimatedDateFromAgoFormMixin,
    GlucoseFormValidatorMixin,
    CrfModelFormMixin,
    CrfFormValidatorMixin,
)


class DmInitialReviewFormValidator(
    GlucoseFormValidatorMixin,
    EstimatedDateFromAgoFormMixin,
    CrfFormValidatorMixin,
    FormValidator,
):
    def clean(self):
        self.required_if(
            DRUGS, INSULIN, field="managed_by", field_required="med_start_ago",
        )

        if self.cleaned_data.get("dx_ago") and self.cleaned_data.get("med_start_ago"):
            if (
                self.estimated_date_from_ago("dx_ago")
                - self.estimated_date_from_ago("med_start_ago")
            ).days > 1:
                raise forms.ValidationError(
                    {"med_start_ago": "Invalid. Cannot be before diagnosis."}
                )
        self.required_if(YES, field="glucose_performed", field_required="glucose_date")
        self.validate_glucose_test()


class DmInitialReviewForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = DmInitialReviewFormValidator

    class Meta:
        model = DmInitialReview
        fields = "__all__"
