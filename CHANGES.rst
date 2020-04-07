Changes
=======

0.1.8
-----
- change prompt on ``baslinecarestatus`` to clarify that ``hiv_clinic_other_is_study_clinic``
  refers to ``hiv_clinic_other``.
- bump up edc==0.1.18

0.1.7
-----
- bump up edc==0.1.17

0.1.6
-----
- bug fixes, bump up edc==0.1.14

0.1.5
-----
- bump up edc==0.1.13
- change approach to multi-country, multi-site deployments, see edc CHANGES
- use separate settings for `uat` and `live`
- hard-code ALLOWED_HOSTS for Uganda.

0.1.4
-----
- add util to generate a dummy rando list. In this trial, randomization is by site, not individual.
  However, the edc still needs randomization slots per patient, even if they are meaningless.
- skip randomization list checks -- run these manually on-demand.
- add support for multi-site/country deployment in settings, gunicorn and nginx files
  (inte-sites, inte-edc). Add `make_files.py` and templates in these folders.
- bump up edc==0.1.12

0.1.3
-----
- use model and model form mixins from `edc-crf`
- update settings and env for new attributes from `edc-protocol`
- bump up to DJ>=3.0.3, python 3.8, edc==0.1.9
