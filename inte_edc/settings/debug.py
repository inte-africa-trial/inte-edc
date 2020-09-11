import os  # noqa
from multisite import SiteID

from .defaults import *  # noqa

print(f"Settings file {__file__}")  # noqa

SITE_ID = SiteID(default=103)
EDC_SITES_UAT_DOMAIN = False
DEBUG = True
ALLOWED_HOSTS = [
    "bagamoyo.tz.inte.clinicedc.org",  # 201
    "bugamba.ug.inte.clinicedc.org",  # 101
    "kinoni.ug.inte.clinicedc.org",  # 103
    "localhost",
]
# ETC_DIR = os.path.join(BASE_DIR, "tests", "etc")  # noqa
# KEY_PATH = os.path.join(ETC_DIR, "crypto_fields")  # noqa
if os.path.exists(BASE_DIR) and not os.path.exists(KEY_PATH):  # noqa
    os.makedirs(KEY_PATH)
    AUTO_CREATE_KEYS = True
