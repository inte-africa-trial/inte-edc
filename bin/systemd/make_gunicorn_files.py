#!/usr/bin/env python3

"""
Generate gunicorn service and sockets for each site

* create a tmp folder.
* copy the template file and make file into the tmp folder
* run

Usage: python make_gunicorn_file.py <systemd_type> <country>
Example:
    python make_gunicorn_file.py service uganda
    python make_gunicorn_file.py socket uganda
"""

import sys
import os

from inte_sites.sites import all_sites


def main():
    path = os.getcwd()
    try:
        systemd_type = sys.argv[1]
        country = sys.argv[2]
    except KeyError:
        sys.stdout.write(
            "\n\nGenerate systemd gunicorn `service` and `sockets` for each site\n"
            "Usage: python make_gunicorn_file.py <systemd_type> <country>\n"
            "Example:\n"
            "    python make_gunicorn_file.py service uganda\n"
            "    python make_gunicorn_file.py socket uganda\n\n"
        )
    else:
        sites = [site[2].lower() for site in all_sites[country]]
        sites.sort()
        with open(f"gunicorn.{systemd_type}.template") as template_file:
            template_str = template_file.read()
        for site in sites:
            if site:
                with open(
                    os.path.join(path, f"gunicorn.{site}.{systemd_type}"), "w+"
                ) as f:
                    f.write(template_str.format(site=site, country=country))
    print("Now copy the files to the /etc/systemd/system folder, for example:")
    print(f"sudo mv gunicorn.*.{systemd_type} /etc/systemd/system")
    print("sudo systemctl daemon-reload")
    print("You also need to start each ")
    sys.exit()


if __name__ == "__main__":
    main()
