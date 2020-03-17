from django.test import TestCase, tag
from edc_reportable import site_reportables, ParserError
from tempfile import mkdtemp
from unittest import skip


@skip
class TestReportables(TestCase):
    def test(self):
        try:
            from inte_labs import reportables
        except ParserError:
            self.fail("ParserError unexpectedly raised.")
        self.assertIsNotNone(site_reportables.get("inte"))
        filename1, filename2 = site_reportables.to_csv("inte", path=mkdtemp())
        print(filename1)
        print(filename2)
