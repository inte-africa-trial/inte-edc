#!/usr/bin/env python3

"""
Generate settings files for each site per country.

Create a subfolder for the country, then run

Usage: python make_file.py <country>
Example:
    python make_file.py uganda
"""

import sys
import os

from edc_sites import get_sites_by_country


def main():
    country = sys.argv[1]
    sites = [
        site[2].lower()
        for site in get_sites_by_country(
            country=country, sites_module_name="inte_sites.sites"
        )
    ]
    sites.sort()
    for site in sites:
        if site:
            with open(os.path.join(os.getcwd(), country, f"{site}.py"), "w+") as f:
                f.write("from ..defaults import *  # noqa\n")
    sys.exit()


if __name__ == "__main__":
    main()
