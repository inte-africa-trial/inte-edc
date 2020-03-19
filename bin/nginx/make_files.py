#!/usr/bin/env python3
"""
Generate nginx conf files for each site

* create a tmp folder.
* copy the template file and make file into the tmp folder
* run

Usage: python make_files.py <country> <country_code>
Example:
    python make_files.py uganda ug
"""

import sys
import os
from inte_sites.sites import all_sites, fqdn
from string import Template


def main():
    template_file = "nginx.template"
    country = sys.argv[1]
    country_code = sys.argv[2]
    sites = [site[2].lower() for site in all_sites[country]]
    sites.sort()
    path = os.getcwd()
    with open(template_file) as template_file:
        template_str = template_file.read()
    for site in sites:
        if site:
            with open(os.path.join(path, f"{site}.{country_code}.conf"), "w+") as f:
                server_name = f"{site}.{country_code}.{fqdn}"
                proxy_pass = f"http://unix:/run/gunicorn-{country_code}-{site}.sock"
                f.write(
                    Template(template_str).substitute(
                        server_name=server_name, proxy_pass=proxy_pass
                    )
                )

    sys.exit()


if __name__ == "__main__":
    main()
