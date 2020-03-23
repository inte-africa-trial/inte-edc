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
    msg = (
        "\n\nGenerate systemd gunicorn `service` and `socket` for each site\n"
        "Usage: python make_gunicorn_file.py <systemd_type> <country>\n"
        "Example:\n"
        "    python make_gunicorn_file.py service uganda\n"
        "    python make_gunicorn_file.py socket uganda\n\n"
    )
    path = os.getcwd()
    try:
        systemd_type = sys.argv[1]
        country = sys.argv[2]
    except KeyError:
        sys.stdout.write(msg)
    else:
        if systemd_type not in ["service", "socket"]:
            sys.stdout.write(msg)
        if country not in ["uganda", "tanzania"]:
            sys.stdout.write(msg)
        print(f"Creating gunicorn systemd {systemd_type} files.")
        sites = [site[2].lower() for site in all_sites[country]]
        sites.sort()
        with open(f"gunicorn.{systemd_type}.template") as template_file:
            template_str = template_file.read()
        for site in sites:
            if site:
                with open(
                    os.path.join(path, f"gunicorn-{site}.{systemd_type}"), "w+"
                ) as f:
                    f.write(template_str.format(site=site, country=country))

        if systemd_type == "socket":
            print("Creating `gunicorn_enable.sh`.")
            with open(os.path.join(path, f"gunicorn_enable.sh"), "w+") as f:
                f.write("#!/bin/bash\n")
                f.write("# A script to start and enable all gunicorn sockets.\n\n")
                f.write("sudo systemctl daemon-reload && \\\n")
                for site in sites:
                    if site:
                        f.write(f"sudo systemctl start gunicorn-{site}.socket && \\\n")
                        f.write(f"sudo systemctl enable gunicorn-{site}.socket && \\\n")
                f.write(f"echo Done.")
            print("Creating `gunicorn_disable.sh`.")
            with open(os.path.join(path, f"gunicorn_disable.sh"), "w+") as f:
                f.write("#!/bin/bash\n")
                f.write("# A script to stop and disable all gunicorn sockets.\n\n")
                f.write("sudo systemctl daemon-reload && \\\n")
                for site in sites:
                    if site:
                        f.write(f"sudo systemctl stop gunicorn-{site}.socket && \\\n")
                        f.write(
                            f"sudo systemctl disable gunicorn-{site}.socket && \\\n"
                        )
                f.write(f"echo Done.")
            print("Creating `gunicorn_start.sh`.")
            with open(os.path.join(path, f"gunicorn_start.sh"), "w+") as f:
                f.write("#!/bin/bash\n")
                f.write("# A script to restart all gunicorn sockets.\n\n")
                f.write("sudo systemctl daemon-reload && \\\n")
                for site in sites:
                    if site:
                        f.write(
                            f"sudo systemctl restart gunicorn-{site}.socket && \\\n"
                        )
                f.write(f"echo Done.\n")
    print("Now copy the files to the /etc/systemd/system folder, for example:")
    print(f"sudo mv gunicorn-*.{systemd_type} /etc/systemd/system")
    print(
        "You also need to start and enable each service by running `gunicorn_enable.sh`."
    )
    sys.exit()


if __name__ == "__main__":
    main()
