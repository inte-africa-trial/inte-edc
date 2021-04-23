from edc_adverse_event.form_validators import ValidateDeathReportMixin
from edc_consent.constants import CONSENT_WITHDRAWAL
from edc_constants.constants import DEAD, LOST_TO_FOLLOWUP, OTHER
from edc_form_validators import FormValidator
from edc_ltfu.modelform_mixins import LtfuFormValidatorMixin
from edc_offstudy.constants import OTHER_RX_DISCONTINUATION
from edc_transfer.constants import TRANSFERRED
from edc_transfer.form_validators import SubjectTransferFormValidatorMixin


class EndOfStudyFormValidator(
    LtfuFormValidatorMixin,
    SubjectTransferFormValidatorMixin,
    ValidateDeathReportMixin,
    FormValidator,
):

    offschedule_reason_field = "offschedule_reason"
    death_date_field = "death_date"

    loss_to_followup_model = "inte_prn.losstofollowup"
    loss_to_followup_date_field = "ltfu_date"
    loss_to_followup_reason = LOST_TO_FOLLOWUP

    subject_transfer_model = "inte_prn.subjecttransfer"
    subject_transfer_date_field = "transfer_date"
    subject_transfer_reason = TRANSFERRED

    def clean(self):

        self.validate_loss_to_followup()

        self.validate_subject_transferred()

        self.validate_death_report_if_deceased()

        if self.cleaned_data.get("offschedule_reason"):
            if self.cleaned_data.get("offschedule_reason").name != OTHER:
                self.validate_other_specify(
                    field="offschedule_reason",
                    other_specify_field="other_offschedule_reason",
                    other_stored_value=OTHER_RX_DISCONTINUATION,
                )

            if self.cleaned_data.get("offschedule_reason").name != OTHER_RX_DISCONTINUATION:
                self.validate_other_specify(
                    field="offschedule_reason",
                    other_specify_field="other_offschedule_reason",
                    other_stored_value=OTHER,
                )

        self.required_if(DEAD, field="offschedule_reason", field_required="death_date")

        self.required_if(
            CONSENT_WITHDRAWAL,
            field="offschedule_reason",
            field_required="consent_withdrawal_reason",
        )

        self.required_if(
            "included_in_error",
            field="offschedule_reason",
            field_required="included_in_error",
        )

        self.required_if(
            "included_in_error",
            field="offschedule_reason",
            field_required="included_in_error_date",
        )
