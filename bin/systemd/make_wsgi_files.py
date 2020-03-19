#!/usr/bin/env python3
"""
Generate wsgi.py files for each site

Usage: python make_wsgi_files.py <country>
Example:
    python make_wsgi_files.py uganda
"""

import sys
import os
from inte_sites.sites import all_sites, fqdn
from string import Template


def main():
    template_file = "wsgi.template"
    country = sys.argv[1]
    sites = [site[2].lower() for site in all_sites[country]]
    sites.sort()
    path = os.getcwd()
    with open(template_file) as template_file:
        template_str = template_file.read()
    for site in sites:
        if site:
            with open(os.path.join(path, f"wsgi_{site}.py"), "w+") as f:
                f.write(template_str.format(site=site, country=country))
    sys.exit()


if __name__ == "__main__":
    main()
