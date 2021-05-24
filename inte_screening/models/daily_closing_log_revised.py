from django.conf import settings

from .daily_closing_log import DailyClosingLog


def get_daily_log_revision_date():
    try:
        return settings.INTE_SCREENING_DCL_REVISION_DATE.date()
    except AttributeError:
        return settings.INTE_SCREENING_DCL_REVISION_DATE


class DailyClosingLogRevised(DailyClosingLog):
    """Second iteration of Daily Closing Log form."""

    class Meta:
        proxy = True
        verbose_name = "Daily Closing Log (post-enrollment)"
        verbose_name_plural = "Daily Closing Logs (post-enrollment)"
