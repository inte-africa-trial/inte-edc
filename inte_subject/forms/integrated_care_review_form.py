from django import forms
from edc_constants.constants import OTHER, YES
from edc_form_validators import FormValidator

from ..models import IntegratedCareReview
from .mixins import (
    CrfFormValidatorMixin,
    CrfModelFormMixin,
    raise_if_clinical_review_does_not_exist,
    raise_if_intervention_site_without_icc_registration,
)


class IntegratedCareReviewFormValidator(
    CrfFormValidatorMixin,
    FormValidator,
):
    def clean(self):
        raise_if_clinical_review_does_not_exist(self.cleaned_data.get("subject_visit"))

        raise_if_intervention_site_without_icc_registration()

        health_message_q = "receive_health_talk_messages"
        health_advice_q = "additional_health_advice"
        parent_dependants = [
            (health_message_q, "health_talk_conditions"),
            (health_message_q, "health_talk_focus"),
            (health_message_q, "health_talk_presenters"),
            (health_advice_q, "health_advice_advisor"),
            (health_advice_q, "health_advice_focus"),
        ]

        for (parent_q, dependant_q) in parent_dependants:
            self.m2m_required_if(
                response=YES,
                field=parent_q,
                m2m_field=dependant_q,
            )
            self.m2m_other_specify(
                OTHER,
                m2m_field=dependant_q,
                field_other=f"{dependant_q}_other",
            )

        #################################################
        self.applicable_if(
            YES,
            field="hospital_card",
            field_applicable="hospital_card_type",
        )
        self.applicable_if(
            YES,
            field="missed_appointment",
            field_applicable="missed_appointment_call",
        )
        self.applicable_if(
            YES,
            field="missed_appointment_call",
            field_applicable="missed_appointment_call_who",
        )
        self.validate_other_specify(
            field="missed_appointment_call_who",
            other_specify_field="missed_appointment_call_who_other",
        )

        #################################################
        self.applicable_if(
            YES,
            field="laboratory_tests",
            field_applicable="pay_for_laboratory_tests",
        )
        self.m2m_required_if(
            response=YES,
            field="pay_for_laboratory_tests",
            m2m_field="which_laboratory_tests_charged_for",
        )
        self.m2m_other_specify(
            OTHER,
            m2m_field="which_laboratory_tests_charged_for",
            field_other="which_laboratory_tests_charged_for_other",
        )


class IntegratedCareReviewForm(CrfModelFormMixin, forms.ModelForm):

    form_validator_cls = IntegratedCareReviewFormValidator

    class Meta:
        model = IntegratedCareReview
        fields = "__all__"
