from .health_economics_revision_one import HealthEconomicsRevisionOne


class HealthEconomicsRevisionTwo(HealthEconomicsRevisionOne):

    """Third iteration of HE form."""

    class Meta:
        proxy = True
        verbose_name = "Health Economics (Revision 02)"
        verbose_name_plural = "Health Economics (Revision 02)"
