from django import forms
from edc_form_validators.form_validator import FormValidator

from .crf_form_validator_mixin import CrfFormValidatorMixin


class HealthEconomicsValidator(CrfFormValidatorMixin, FormValidator):
    pass
