from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

fqdn = "inte.clinicedc.org"

all_inte_sites = {
    "uganda": (
        (100, "kinoni", "Kinoni"),
        (110, "bugamba", "Bugamba"),
        (120, "bwizibwera", "Bwizibwera"),
        (140, "ruhoko", "Ruhoko"),
        (150, "kyazanga", "Kyazanga"),
        (160, "bukulula", "Bukulula"),
        (170, "kojja", "Kojja"),
        (180, "mpigi", "Mpigi"),
        (190, "namayumba", "Namayumba"),
        (200, "buwambo", "Buwambo"),
        (210, "kajjansi", "Kajjansi"),
        (220, "tikalu", "Tikalu"),
        (230, "namulonge", "Namulonge"),
        (240, "kasanje", "Kasanje"),
        (250, "kasangati", "Kasangati"),
    )
}

try:
    country = settings.COUNTRY
except ImproperlyConfigured:
    country = None
    inte_sites = []
else:
    inte_sites = all_inte_sites[country]
