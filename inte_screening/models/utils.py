from django.conf import settings


def get_daily_log_revision_date():
    try:
        return settings.INTE_SCREENING_DCL_REVISION_DATETIME.date()
    except AttributeError:
        return settings.INTE_SCREENING_DCL_REVISION_DATETIME
