from edc_model import models as edc_models


class EstimatedDateFromAgoFormMixin:
    def estimated_date_from_ago(self, f1):
        estimated_date = None
        if self.cleaned_data.get(f1):
            estimated_date = edc_models.duration_to_date(
                self.cleaned_data.get(f1),
                self.cleaned_data.get("report_datetime").date(),
            )
        return estimated_date
