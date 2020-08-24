from django import forms
from edc_constants.constants import FORMER_SMOKER, YES
from edc_form_validators.form_validator import FormValidator

from ..models import OtherBaselineData
from .mixins import (
    EstimatedDateFromAgoFormMixin,
    CrfFormValidatorMixin,
    CrfModelFormMixin,
)


class OtherBaselineDataFormValidator(
    CrfFormValidatorMixin, EstimatedDateFromAgoFormMixin, FormValidator
):
    def clean(self):

        self.required_if(
            FORMER_SMOKER, field="smoking_status", field_required="smoker_quit_ago"
        )
        self.estimated_date_from_ago("smoker_quit_ago")

        self.applicable_if(YES, field="alcohol", field_applicable="alcohol_consumption")

        self.validate_other_specify(
            field="employment_status", other_specify_field="employment_status_other"
        )


class OtherBaselineDataForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = OtherBaselineDataFormValidator

    class Meta:
        model = OtherBaselineData
        fields = "__all__"
