from .daily_closing_log import DailyClosingLog


class DailyClosingLogRevised(DailyClosingLog):
    """Second iteration of Daily Closing Log form."""

    class Meta:
        proxy = True

