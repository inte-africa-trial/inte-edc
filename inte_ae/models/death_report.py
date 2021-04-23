from edc_adverse_event.model_mixins import DeathReportModelMixin
from edc_model import models as edc_models
from respond_models.mixins.ae import RespondDeathReportFieldsModelMixin


class DeathReport(
    RespondDeathReportFieldsModelMixin, DeathReportModelMixin, edc_models.BaseUuidModel
):

    death_date_field = "death_date"

    # @property
    # def death_datetime(self):
    #     return self.death_date

    class Meta(DeathReportModelMixin.Meta, edc_models.BaseUuidModel.Meta):
        pass
