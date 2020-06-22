from django import forms
from django.core.exceptions import ObjectDoesNotExist
from edc_action_item.forms.action_item_form_mixin import ActionItemFormMixin
from edc_constants.constants import YES, NO
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator
from inte_subject.forms.care_status_exists_or_raise import care_status_exists_or_raise

from ..constants import INSULIN, DRUGS
from ..models import DiabetesInitialReview, CareStatus


class DiabetesInitialReviewFormValidator(FormValidator):
    def clean(self):
        self.required_if(
            DRUGS, INSULIN, field="managed_by", field_required="med_start_ago",
        )

        self.required_if(YES, field="glucose_performed", field_required="glucose_date")
        self.required_if(YES, field="glucose_performed", field_required="glucose")
        self.required_if(
            YES, field="glucose_performed", field_required="glucose_quantifier"
        )
        self.required_if(YES, field="glucose_performed", field_required="glucose_units")


class DiabetesInitialReviewForm(
    CrfModelFormMixin, ActionItemFormMixin, forms.ModelForm
):
    form_validator_cls = DiabetesInitialReviewFormValidator

    def clean(self):
        care_status_exists_or_raise(self)
        return super().clean()

    class Meta:
        model = DiabetesInitialReview
        fields = "__all__"
