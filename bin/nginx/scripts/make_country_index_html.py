#!/usr/bin/env python3

"""
Generate country index html file that displays links for each site

Usage: python make_country_sites_html.py <country> <country_code>
Example: python make_country_sites_html.py uganda ug
"""

import sys
import os

from inte_sites.sites import all_sites, fqdn


def get_domain(country_code, uat):
    domain = []
    if uat:
        domain.append("uat")
    domain.append(country_code)
    domain.append(fqdn)
    return ".".join(domain)


def main():
    """
    Create index.html files for the UAT and LIVE sites

    home is fqdn, e.g. inte.clinicedc.org

    To get to the list of sites:
    - UAT is uat.<country>.<fqdn>, e.g. uat.ug.inte.clinicedc.org
    - LIVE is <country>.<fqdn>, e.g. ug.inte.clinicedc.org

    A site system instance is:
        UAT: <site>.uat.<country>.inte.clinicedc.org
        LIVE: <site>.<country>.inte.clinicedc.org

    """

    sites_anchors = []
    path = os.getcwd()
    uat = "uat" if sys.argv[3] == "uat" else ""
    country = sys.argv[1]
    title = (
        f"INTE Africa UAT Sites: {country.title()}"
        if uat
        else f"INTE Africa Sites: {country.title()}"
    )
    home = f"{uat}.{fqdn}" if uat else fqdn
    home_anchor = f'<a href="https://{home}/" class="list-group-item">Home</a>'
    sites = [site[2].lower() for site in all_sites[country]]
    sites.sort()
    for site in sites:
        if site:
            sites_anchors.append(
                f'<a href="https://{site}.{get_domain(sys.argv[2], uat)}/" class="list-group-item">{site.title()}</a>'
            )
    with open(f"country_index.html.template") as f:
        index_str = f.read()
    with open(os.path.join(path, f"index.html"), "w+") as f:
        f.write(
            index_str.format(
                title=title,
                panel_color="danger" if uat else "success",
                home_anchor=home_anchor,
                sites_anchors="\n         ".join(sites_anchors),
            )
        )
    sys.exit()


if __name__ == "__main__":
    main()
