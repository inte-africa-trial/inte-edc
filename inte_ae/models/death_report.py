from edc_adverse_event.model_mixins import (
    DeathReportExtraFieldsModelMixin,
    DeathReportModelMixin,
)
from edc_model import models as edc_models


class DeathReport(
    DeathReportExtraFieldsModelMixin, DeathReportModelMixin, edc_models.BaseUuidModel
):

    death_date_field = "death_date"

    class Meta(
        DeathReportExtraFieldsModelMixin.Meta,
        DeathReportModelMixin.Meta,
        edc_models.BaseUuidModel.Meta,
    ):
        pass
