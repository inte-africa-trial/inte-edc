from django.test import TestCase, tag
from edc_list_data.site_list_data import site_list_data


class TestList(TestCase):
    def test_(self):
        site_list_data.autodiscover()
