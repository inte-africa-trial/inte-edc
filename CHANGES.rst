Changes
=======

0.1.69
------
- bump to edc 0.3.27
- bump to respond-africa 0.1.12 (last version supporting Python 3.8)
- fix
    - missing form mixins import
    - viral load PRN error (on save)
    - unable to set visit report reason to "Missed visit"
- update clinical baseline review to allow patients from clinic without
  a diagnosis of condition treated by that clinic
  (providing they have a related test, a diagnosis result and >=1 conditions overall)
- Testing environment
    - drop Python 3.8 tests against bleeding edge/development codebase (`edcdev`)
    - bump Python version for tox lint tests (run under GH actions) from 3.8 to 3.9

0.1.68
------
- fix drug refill forms autocomplete field not using proxy model
- fix initial review forms not updating estimated dx date
  if dx ago is provided
- add data migration to update existing initial review instances
- fix order of urls paths and routes for custom admin sites
- bump respond-africa to 0.1.11
- add additional hypertension treatments
- bump edc to 0.3.22

0.1.67
------
- bump to edc 0.3.21

0.1.66
------
- bump to edc 0.3.18
- revised daily closing log (gh-4)
- add integrated care review CRF (Form 26), required at 6m and 12m visits
- add support for DJ 3.2

0.1.65
------
- bump to edc 0.3.15

0.1.64
----------
- bump to edc 0.3.14
- Testing environment
    - add Django 3.2
    - drop Django 3.0
    - drop Python 3.7
- Respond
    - add requirement for respond-africa 0.1.8
    - add respond diagnosis labels
    - use death report model mixin from respond
    - use Diagnosis class from respond
- Health Economics Form
    - add shortened 'HE (Rev 2)' proxy model, form and admin class
    - 'HE (Rev 2)' form required at 6m visits on or after 2021-04-26
    - 'HE (Rev 1)' form now only required for 6m visits before 2021-04-26
    - 'HE (Rev 1)' form not required at baseline or 12m

0.1.59
------
- bump to edc 0.1.72

0.1.58
------
- bump to edc 0.1.71

0.1.52
------
- add proxy models for offschedule and ltfu
- fix issues with acion items and missed visit, ltfu, end of study
  flow

0.1.50
------
- bump to edc 0.1.62

0.1.48
------
- update missed visit, ltfu, death report flow
- pin HE CRF to 6 months instead of any time after baseline
- update HTN drug list
- bump to edc 0.1.60

0.1.41
------
- add validation to catch multiple initials reviews submitted (inte-subject)

0.1.40
------
- fix baseline determination for drug refill `rx_modified` form
  validation (inte-subject)
- fix HE form to allow `0` as payment amount (inte-subject)
- add fields to Clinical Review model; health_insurance,
  patient_club (inte-subject)
- add medication adherence CRFs (inte-subject)
- enforce window period. Extend 6m upper to 1 month before 12m

0.1.38
------
- add result forms to PRN list (VL, CD4, glucose)
- enforce order of CRF submission where necessary
- modify review followup forms (hiv, htn, dm); add care delivery
  questions linked to randomization and icc registration, remove
  test date and dx questions, check for art init date if not
  started at diagnosis.
- add missing other specify fields to HE form
- add diagnoses class to validate any Q's/CRFs related to a
  diagnosis or diagnosis date
- expand forms validation and tests
- add management command to refresh INTE metadata

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
