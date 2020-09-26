from django import forms
from edc_form_validators.form_validator import FormValidator

from ..models import HivReview
from .mixins import (
    art_initiation_date,
    raise_if_clinical_review_does_not_exist,
    CrfModelFormMixin,
    CrfFormValidatorMixin,
)


class HivReviewFormValidator(CrfFormValidatorMixin, FormValidator):
    def clean(self):
        raise_if_clinical_review_does_not_exist(self.cleaned_data.get("subject_visit"))
        self.applicable_if_true(
            not art_initiation_date(
                subject_identifier=self.subject_identifier,
                report_datetime=self.report_datetime,
            ),
            field_applicable="arv_initiation_actual_date",
            not_applicable_msg="Subject was previously reported as on ART.",
        )


class HivReviewForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = HivReviewFormValidator

    class Meta:
        model = HivReview
        fields = "__all__"
