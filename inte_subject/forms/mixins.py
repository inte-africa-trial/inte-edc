from django import forms
from edc_constants.constants import OTHER, YES
from edc_model import models as edc_models
from edc_visit_schedule.constants import DAY1


class EstimatedDateFromAgoFormMixin:
    def estimated_date_from_ago(self, f1):
        estimated_date = None
        if self.cleaned_data.get(f1):
            estimated_date = edc_models.duration_to_date(
                self.cleaned_data.get(f1),
                self.cleaned_data.get("report_datetime").date(),
            )
        return estimated_date


class DrugRefillFormValidatorMixin:
    def clean(self):
        if (
            self.cleaned_data.get("subject_visit").appointment.visit_code == DAY1
            and self.cleaned_data.get("rx_modified") == YES
        ):
            raise forms.ValidationError({"rx_modified": "Expected `No` at baseline."})

        self.m2m_other_specify(
            OTHER, m2m_field="modifications", field_other="modifications_other"
        )
        self.m2m_other_specify(
            OTHER,
            m2m_field="modification_reasons",
            field_other="modification_reasons_other",
        )


class DrugSupplyNcdFormMixin:
    def clean(self):
        cleaned_data = super().clean()
        if self.cleaned_data.get("drug") and self.cleaned_data.get("drug").name not in [
            obj.name for obj in self.cleaned_data.get("drug_refill").rx.all()
        ]:
            rx = " + ".join(
                [obj.name for obj in self.cleaned_data.get("drug_refill").rx.all()]
            )
            raise forms.ValidationError(
                f"Invalid. `{self.cleaned_data.get('drug').display_name}` "
                f"not in current treatment of `{rx}`"
            )
        return cleaned_data


class GlucoseFormValidatorMixin:
    def validate_glucose_test(self):
        if self.cleaned_data.get("glucose_date") and self.cleaned_data.get("dx_ago"):
            if (
                self.estimated_date_from_ago("dx_ago")
                - self.cleaned_data.get("glucose_date")
            ).days > 1:
                raise forms.ValidationError(
                    {"glucose_date": "Invalid. Cannot be before diagnosis."}
                )
        self.required_if(YES, field="glucose_performed", field_required="glucose")
        self.required_if(
            YES, field="glucose_performed", field_required="glucose_quantifier"
        )
        self.required_if(YES, field="glucose_performed", field_required="glucose_units")


class ReviewFormValidatorMixin:
    def validate_test_and_care_dates(self):
        if self.cleaned_data.get("test_date") and self.cleaned_data.get(
            "care_start_date"
        ):
            if (
                self.cleaned_data.get("test_date")
                - self.cleaned_data.get("care_start_date")
            ).days > 1:
                raise forms.ValidationError(
                    {"care_start_date": "Invalid. Cannot be before test date."}
                )


class BPFormValidatorMixin:
    def validate_bp_reading(self, sys_field, dia_field):
        if self.cleaned_data.get(sys_field) and self.cleaned_data.get(dia_field):
            if self.cleaned_data.get(sys_field) < self.cleaned_data.get(dia_field):
                raise forms.ValidationError(
                    {dia_field: "Systolic must be greater than diastolic."}
                )
