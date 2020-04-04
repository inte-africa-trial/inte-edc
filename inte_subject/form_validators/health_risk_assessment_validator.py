from edc_constants.constants import SMOKER, YES
from edc_form_validators.form_validator import FormValidator


class HealthRiskAssessmentFormValidator(FormValidator):
    def clean(self):

        self.required_if(
            SMOKER, field="smoker_current", field_required="smoker_quit_ago_str"
        )

        self.applicable_if(
            SMOKER, field="smoker_current", field_applicable="smoker_cigarettes_per_day"
        )

        self.applicable_if(YES, field="alcohol", field_applicable="alcohol_consumption")
