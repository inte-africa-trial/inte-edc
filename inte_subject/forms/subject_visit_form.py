import pdb

from django import forms
from edc_constants.constants import OTHER, STUDY_DEFINED_TIMEPOINT
from edc_form_validators import FormValidatorMixin
from edc_sites.forms import SiteModelFormMixin
from edc_visit_tracking.form_validators import VisitFormValidator

from ..models import SubjectVisit


class SubjectVisitFormValidator(VisitFormValidator):
    validate_missed_visit_reason = False

    def clean(self):
        super().clean()
        self.m2m_other_specify(
            OTHER, m2m_field="clinic_services", field_other="clinic_services_other",
        )
        selections = self.get_m2m_selected("clinic_services")
        if (
            self.cleaned_data.get("appointment").visit_code_sequence == 0
            and STUDY_DEFINED_TIMEPOINT not in selections
        ):
            raise forms.ValidationError(
                {"clinic_services": "This is scheduled study visit."}
            )
        elif (
            self.cleaned_data.get("appointment").visit_code_sequence != 0
            and STUDY_DEFINED_TIMEPOINT in selections
        ):
            raise forms.ValidationError(
                {"clinic_services": "This is not a scheduled study visit."}
            )


class SubjectVisitForm(SiteModelFormMixin, FormValidatorMixin, forms.ModelForm):

    form_validator_cls = SubjectVisitFormValidator

    class Meta:
        model = SubjectVisit
        fields = "__all__"
