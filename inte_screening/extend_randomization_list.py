import csv
from typing import Optional

from inte_sites.is_intervention_site import is_intervention_site
from inte_sites.sites import all_sites

"""
from edc_randomization.randomization_list_importer import RandomizationListImporter

RandomizationListImporter(name='default', add=True, dryrun=False)

"""


def randomization_rows(last_int: int, rows_to_add: int):
    rows = []
    for country, sites in all_sites.items():
        for site in sites:
            arm = "intervention" if is_intervention_site(site) else "control"
            n = int(f"{site.site_id}{last_int}")
            for i in range(1, rows_to_add + 1):
                n += 1
                rows.append([n, arm, site.name, country])
    return rows


def export_to_file(filename: str, last_int: int, rows_to_add: Optional[int] = None):
    rows_to_add = rows_to_add or 50
    with open(filename, "a") as f:
        writer = csv.writer(f)
        for row in randomization_rows(last_int, rows_to_add):
            writer.writerow(row)
