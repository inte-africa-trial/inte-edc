#!/usr/bin/env python3

"""
Generate country index html file that displays links for each site

* create a tmp folder.
* copy the template file and make file into the tmp folder
* run

Usage: python make_sites_html.py <country> <country_code>
Example: python make_sites_html.py uganda ug
"""

import sys
import os

from inte_sites.sites import all_sites, fqdn


def main():
    sites_anchors = []
    path = os.getcwd()
    country = sys.argv[1]
    country_code = sys.argv[2]
    uat_or_live = sys.argv[3]
    uat_or_live = "uat" if uat_or_live == "uat" else ""
    title = "INTE Africa UAT Sites" if uat_or_live else "INTE Africa Sites"
    home = f"{uat_or_live}.{fqdn}" if uat_or_live else fqdn
    home_anchor = f'<a href="https://{home}/" class="list-group-item">Home</a>'
    sites = [site[2].lower() for site in all_sites[country]]
    sites.sort()
    for site in sites:
        if site:
            sites_anchors.append(
                f'<a href="https://{site}.{uat_or_live}.{country_code}.{fqdn}/" class="list-group-item">{site.title()}</a>'
            )
    with open(f"country_index.html.template") as f:
        index_str = f.read()
    with open(os.path.join(path, f"index.html"), "w+") as f:
        f.write(
            index_str.format(
                title=title,
                panel_color="danger" if uat_or_live else "success",
                home_anchor=home_anchor,
                sites_anchors="\n         ".join(sites_anchors),
            )
        )
    sys.exit()


if __name__ == "__main__":
    main()
