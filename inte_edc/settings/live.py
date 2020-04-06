from multisite import SiteID

from .defaults import *  # noqa

print(f"Settings file {__file__}")  # noqa

SITE_ID = SiteID(default=1)
EDC_SITES_UAT_DOMAIN = False
ALLOWED_HOSTS = [
    "bugamba.ug.inte.clinicedc.org",
    "bukulula.ug.inte.clinicedc.org",
    "buwambo.ug.inte.clinicedc.org",
    "bwizibwera.ug.inte.clinicedc.org",
    "kajjansi.ug.inte.clinicedc.org",
    "kasangati.ug.inte.clinicedc.org",
    "kasanje.ug.inte.clinicedc.org",
    "kinoni.ug.inte.clinicedc.org",
    "kojja.ug.inte.clinicedc.org",
    "kyamulibwa.ug.inte.clinicedc.org",
    "kyazanga.ug.inte.clinicedc.org",
    "mpigi.ug.inte.clinicedc.org",
    "muduma.ug.inte.clinicedc.org",
    "namayumba.ug.inte.clinicedc.org",
    "namulonge.ug.inte.clinicedc.org",
    "ruhoko.ug.inte.clinicedc.org",
    "sekiwunga.ug.inte.clinicedc.org",
    "tikalu.ug.inte.clinicedc.org",
    "localhost",
]
