from django import forms
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator

from ..models import NextAppointment
from .crf_form_validator_mixin import CrfFormValidatorMixin


class NextAppointmentValidator(CrfFormValidatorMixin, FormValidator):
    pass


class NextAppointmentForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = NextAppointmentValidator

    class Meta:
        model = NextAppointment
        fields = "__all__"
