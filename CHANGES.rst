Changes
=======

0.1.5
-----
- add util to generate a dummy rando list. In this trial, randomization is by site, not individual.
  However, the edc still needs randomization slots per patient, even if they are meaningless.
- tweek multi-site/country approach
- skip randomization list checks -- run these manually on-demand.
- bump up edc==0.1.12

0.1.4
-----
- add support for multi-site/country deployment in settings, gunicorn and nginx files
  (inte-sites, inte-edc). Add `make_files.py` and templates in these folders.

0.1.3
-----
- use model and model form mixins from `edc-crf`
- update settings and env for new attributes from `edc-protocol`
- bump up to DJ>=3.0.3, python 3.8, edc==0.1.9
