from django import forms
from edc_adverse_event.modelform_mixins import DeathReportModelFormMixin
from edc_constants.constants import YES
from edc_form_validators import FormValidator

from ..models import DeathReport


class DeathReportFormValidator(FormValidator):
    def clean(self):
        self.validate_other_specify(
            field="death_location", other_specify_field="death_location_other"
        )
        self.required_if(YES, field="hospital_death", field_required="hospital_name")
        self.validate_other_specify(field="informant", other_specify_field="informant_other")
        self.validate_other_specify(
            field="confirmed_by", other_specify_field="confirmed_by_other"
        )


class DeathReportForm(DeathReportModelFormMixin, forms.ModelForm):

    form_validator_cls = DeathReportFormValidator

    class Meta:
        model = DeathReport
        fields = [
            "subject_identifier",
            "report_datetime",
            "death_date",
            "death_location",
            "death_location_other",
            "hospital_death",
            "hospital_name",
            "informant",
            "informant_other",
            "confirmed_by",
            "confirmed_by_other",
            "narrative",
        ]
