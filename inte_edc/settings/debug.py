from multisite import SiteID

from .defaults import *  # noqa

print(f"Settings file {__file__}")  # noqa

SITE_ID = SiteID(default=101)
EDC_SITES_UAT_DOMAIN = False
DEBUG = True
ALLOWED_HOSTS = [
    "bugamba.ug.inte.clinicedc.org",
    "localhost",
]
# ETC_DIR = os.path.join(BASE_DIR, "tests", "etc")
# KEY_PATH = os.path.join(ETC_DIR, "crypto_fields")
# if os.path.exists(BASE_DIR) and not os.path.exists(KEY_PATH):
#     os.makedirs(KEY_PATH)
#     AUTO_CREATE_KEYS = True
