from django import forms
from edc_constants.constants import DIABETES, HIV, HYPERTENSION, OTHER, REFILL
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator

from ..models import ReasonForVisit
from .crf_form_validator_mixin import CrfFormValidatorMixin


class ReasonForVisitFormValidator(CrfFormValidatorMixin, FormValidator):
    def clean(self):
        self.m2m_other_specify(
            OTHER, m2m_field="clinic_services", field_other="clinic_services_other",
        )
        self.m2m_other_specify(
            REFILL, m2m_field="clinic_services", field_other="refill_conditions",
        )

        self.m2m_other_specify(
            REFILL, m2m_field="clinic_services", field_other="refill_conditions",
        )

        is_refill = REFILL in self.get_m2m_selected(m2m_field="health_services")
        self.required_if_true(
            is_refill
            and HYPERTENSION in self.get_m2m_selected(m2m_field="health_services"),
            field_required="refill_hypertension",
        )
        self.required_if_true(
            is_refill
            and DIABETES in self.get_m2m_selected(m2m_field="health_services"),
            field_required="refill_diabetes",
        )
        self.required_if_true(
            is_refill and HIV in self.get_m2m_selected(m2m_field="health_services"),
            field_required="refill_hiv",
        )

        # for condition_name, condition_display_name in self.get_m2m_selected(
        #     m2m_field="refill_conditions"
        # ).items():
        #     if condition_name not in self.get_m2m_selected(m2m_field="health_services"):
        #         self.m2m_selections_not_expected(
        #             condition_name,
        #             m2m_field="refill_conditions",
        #             error_msg=(
        #                 f"Invalid. `{condition_display_name}` not one of the "
        #                 f"health services listed above."
        #             ),
        #         )


class ReasonForVisitForm(CrfModelFormMixin, forms.ModelForm):

    form_validator_cls = ReasonForVisitFormValidator

    class Meta:
        model = ReasonForVisit
        fields = "__all__"
