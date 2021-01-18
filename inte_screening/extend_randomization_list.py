def dd(all_sites, func_arm=None):
    for country, sites in all_sites.items():
        for site in sites:
             arm = "intervention" if is_intervention_site(site) else "control"
         n = int(f"{site.site_id}220")

        for i in range(1, 50):
             n += 1
         print(f"{n},{arm},{site.name},{country}")