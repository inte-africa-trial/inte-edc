from .health_economics_revision_01 import HealthEconomicsRevision01


class HealthEconomicsRevision02(HealthEconomicsRevision01):

    """Third iteration of HE form."""

    class Meta:
        proxy = True
        verbose_name = "Health Economics (Revision 02)"
        verbose_name_plural = "Health Economics (Revision 02)"
