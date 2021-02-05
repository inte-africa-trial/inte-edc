from django import forms
from edc_form_validators.form_validator import FormValidator

from inte_consent.models import SubjectConsent
from inte_prn.icc_registered import icc_registered
from inte_screening.constants import (
    DIABETES_CLINIC,
    HIV_CLINIC,
    HYPERTENSION_CLINIC,
    NCD_CLINIC,
)

from ..models import (
    DmInitialReview,
    HivInitialReview,
    HtnInitialReview,
    NextAppointment,
)
from .mixins import (
    CrfFormValidatorMixin,
    CrfModelFormMixin,
    raise_if_clinical_review_does_not_exist,
)


class NextAppointmentFormValidator(CrfFormValidatorMixin, FormValidator):
    def clean(self):
        raise_if_clinical_review_does_not_exist(self.cleaned_data.get("subject_visit"))
        self.required_if_true(
            icc_registered(report_datetime=self.cleaned_data.get("report_datetime")),
            field_required="integrated_clinic_appt_date",
        )
        self.date_not_before(
            "report_datetime",
            "integrated_clinic_appt_date",
            convert_to_date=True,
        )
        if not icc_registered(report_datetime=self.cleaned_data.get("report_datetime")):
            # hiv_clinic_appt_date
            condition = (
                self.clinic_type == HIV_CLINIC
                or HivInitialReview.objects.filter(
                    subject_visit__appointment__subject_identifier=self.subject_identifier,
                    subject_visit__report_datetime__lte=self.cleaned_data.get(
                        "report_datetime"
                    ),
                ).exists()
            )
            self.required_if_true(condition, field_required="hiv_clinic_appt_date")
            self.date_not_before(
                "report_datetime",
                "hiv_clinic_appt_date",
                convert_to_date=True,
            )
            ncd_condition = (
                DmInitialReview.objects.filter(
                    subject_visit__appointment__subject_identifier=self.subject_identifier,
                    subject_visit__report_datetime__lte=self.cleaned_data.get(
                        "report_datetime"
                    ),
                ).exists()
                or HtnInitialReview.objects.filter(
                    subject_visit__appointment__subject_identifier=self.subject_identifier,
                    subject_visit__report_datetime__lte=self.cleaned_data.get(
                        "report_datetime"
                    ),
                ).exists()
            )
            self.required_if_true(
                ncd_condition and self.clinic_type == NCD_CLINIC,
                field_required="ncd_clinic_appt_date",
            )
            self.date_not_before(
                "report_datetime",
                "ncd_clinic_appt_date",
                convert_to_date=True,
            )
            self.required_if_true(
                ncd_condition and self.clinic_type == DIABETES_CLINIC,
                field_required="dm_clinic_appt_date",
            )
            self.date_not_before(
                "report_datetime",
                "dm_clinic_appt_date",
                convert_to_date=True,
            )
            self.required_if_true(
                ncd_condition and self.clinic_type == HYPERTENSION_CLINIC,
                field_required="htn_clinic_appt_date",
            )
            self.date_not_before(
                "report_datetime",
                "htn_clinic_appt_date",
                convert_to_date=True,
            )

    @property
    def clinic_type(self):
        return SubjectConsent.objects.get(
            subject_identifier=self.subject_identifier
        ).clinic_type


class NextAppointmentForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = NextAppointmentFormValidator

    class Meta:
        model = NextAppointment
        fields = "__all__"
