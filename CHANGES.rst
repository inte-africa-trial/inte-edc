Changes
=======

0.1.36
------
- refactor field and variable naming using these prefixes: htn-> hypertension, dm->diabetes, hiv->hiv
- change visit schedule to three study timepoints (0,6,12) only
- interim / routine / unwell visits can be entered as 'unscheduled' as per the EDC
- define CRF set for all interim visits
- remove reason_for_visit. merge reason_for_visit fields health_services, clinic_services into subject_visit and 
  refill questions into new 'medications' CRF
- change baseline_care_status and investigations to clinical_review_baseline and clinical_review, respectively
- add family history, require once at any visit after baseline (form 8)
- add new version of health economics, require once at any visit after baseline (TODO: link to ICC reg form)
- rename fields and variables diabetic_xxx, hypertensive_xxx to diabetes_xxx and hypertension_xxx for consistency 
- add ICC registration form
- fix daily log options for method of recruitment to align with screening form
- add extra option to subject_visit.info_sources, patient and care card
- make weight and height optional after baseline on the indicators CRF
- fix issues with metadata_rules, expand
- on former investigations CRF, now clinical review, ask for test dates per condition
- change wording on post-baseline clinical review questions to ask for a new DX as of today
- for testing and dx, ask for either duration 'ago' or exact date 
- greatly improve test coverage

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
