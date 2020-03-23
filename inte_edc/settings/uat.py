from multisite import SiteID

from .defaults import *  # noqa

print(f"Settings file {__file__}")  # noqa

SITE_ID = SiteID(default=1)
EDC_SITES_UAT_DOMAIN = True
ALLOWED_HOSTS = [
    "bugamba.uat.ug.inte.clinicedc.org",
    "bwizibwera.uat.ug.inte.clinicedc.org",
    "kinoni.uat.ug.inte.clinicedc.org",
    "ruhoko.uat.ug.inte.clinicedc.org",
    "kyazanga.uat.ug.inte.clinicedc.org",
    "bukulula.uat.ug.inte.clinicedc.org",
    "kojja.uat.ug.inte.clinicedc.org",
    "mpigi.uat.ug.inte.clinicedc.org",
    "namayumba.uat.ug.inte.clinicedc.org",
    "buwambo.uat.ug.inte.clinicedc.org",
    "kajjansi.uat.ug.inte.clinicedc.org",
    "tikalu.uat.ug.inte.clinicedc.org",
    "namulonge.uat.ug.inte.clinicedc.org",
    "kasanje.uat.ug.inte.clinicedc.org",
    "kasangati.uat.ug.inte.clinicedc.org",
    "sekiwunga.uat.ug.inte.clinicedc.org",
    "muduma.uat.ug.inte.clinicedc.org",
    "kyamulibwa.uat.ug.inte.clinicedc.org",
    "localhost",
]
