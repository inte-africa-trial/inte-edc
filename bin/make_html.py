#!/usr/bin/env python3

"""
Generate country index html file that displays links for each site

* create a tmp folder.
* copy the template file and make file into the tmp folder
* run

Usage: python make_html.py <country> <country_code>
Example: python make_html.py uganda ug
"""

import sys
import os

from inte_sites.sites import all_inte_sites, fqdn


def main():
    sites_anchors = []
    path = os.getcwd()
    country = sys.argv[1]
    country_code = sys.argv[2]
    sites = [site[2].lower() for site in all_inte_sites[country]]
    sites.sort()
    for site in sites:
        if site:
            sites_anchors.append(
                f'<a href="https://{site}.{country_code}.{fqdn}/" class="list-group-item">{country.title()}</a>'
            )
    with open(f"index_country.template") as f:
        index_str = f.read()
    with open(os.path.join(path, f"index_{country_code}.html"), "w+") as f:
        f.write(index_str.format(sites_anchors="\n         ".join(sites_anchors)))
    sys.exit()


if __name__ == "__main__":
    main()
