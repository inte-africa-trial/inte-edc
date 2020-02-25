from django import forms
from edc_sites.forms import SiteModelFormMixin
from edc_form_validators.form_validator_mixin import FormValidatorMixin

from ..form_validators import NextAppointmentValidator
from ..models import NextAppointment


class NextAppointmentForm(SiteModelFormMixin, FormValidatorMixin, forms.ModelForm):
    form_validator_cls = NextAppointmentValidator

    class Meta:
        model = NextAppointment
        fields = "__all__"
