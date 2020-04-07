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
    "bagamoyo.tz.inte.clinicedc.org",
    "buguruni.tz.inte.clinicedc.org",
    "rugambwa.tz.inte.clinicedc.org",
    "consolata.tz.inte.clinicedc.org",
    "kinondoni.tz.inte.clinicedc.org",
    "kisarawe.tz.inte.clinicedc.org",
    "magomeni.tz.inte.clinicedc.org",
    "mbagala.tz.inte.clinicedc.org",
    "mnazi.tz.inte.clinicedc.org",
    "sinza.tz.inte.clinicedc.org",
    "vincent.tz.inte.clinicedc.org",
    "tambuka.tz.inte.clinicedc.org",
    "tandale.tz.inte.clinicedc.org",
    "tegeta.tz.inte.clinicedc.org",
    "temeke.tz.inte.clinicedc.org",
    "yombo.tz.inte.clinicedc.org",
    "localhost",
]
