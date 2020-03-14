from django import forms
from edc_crf.modelform_mixins import CrfModelFormMixin

from ..form_validators import NextAppointmentValidator
from ..models import NextAppointment


class NextAppointmentForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = NextAppointmentValidator

    class Meta:
        model = NextAppointment
        fields = "__all__"
