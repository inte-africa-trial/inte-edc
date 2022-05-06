# Forms Reference
## Table of contents


<a href="#user-content-1000">**1000.**</a>
1. <a href="#user-content-clinical-review-baseline">Clinical Review: Baseline</a>
2. <a href="#user-content-indicators">Indicators</a>
3. <a href="#user-content-hiv-initial-review">Hiv Initial Review</a>
4. <a href="#user-content-diabetes-initial-review">Diabetes Initial Review</a>
5. <a href="#user-content-hypertension-initial-review">Hypertension Initial Review</a>
6. <a href="#user-content-medications">Medications</a>
7. <a href="#user-content-drug-refill-hypertension">Drug Refill: Hypertension</a>
8. <a href="#user-content-drug-refill-diabetes">Drug Refill: Diabetes</a>
9. <a href="#user-content-drug-refill-hiv">Drug Refill: Hiv</a>
10. <a href="#user-content-other-baseline-data">Other Baseline Data</a>
11. <a href="#user-content-complications-baseline">Complications: Baseline</a>
12. <a href="#user-content-routine-appointment">Routine Appointment</a>

<a href="#user-content-1060">**1060.**</a>
1. <a href="#user-content-clinical-review">Clinical Review</a>
2. <a href="#user-content-hiv-initial-review-1">Hiv Initial Review</a>
3. <a href="#user-content-diabetes-initial-review-1">Diabetes Initial Review</a>
4. <a href="#user-content-indicators-1">Indicators</a>
5. <a href="#user-content-hypertension-initial-review-1">Hypertension Initial Review</a>
6. <a href="#user-content-hiv-review">Hiv Review</a>
7. <a href="#user-content-diabetes-review">Diabetes Review</a>
8. <a href="#user-content-hypertension-review">Hypertension Review</a>
9. <a href="#user-content-medications-1">Medications</a>
10. <a href="#user-content-drug-refill-hypertension-1">Drug Refill: Hypertension</a>
11. <a href="#user-content-drug-refill-diabetes-1">Drug Refill: Diabetes</a>
12. <a href="#user-content-drug-refill-hiv-1">Drug Refill: Hiv</a>
13. <a href="#user-content-hiv-medication-adherence">Hiv Medication Adherence</a>
14. <a href="#user-content-diabetes-medication-adherence">Diabetes Medication Adherence</a>
15. <a href="#user-content-hypertension-medication-adherence">Hypertension Medication Adherence</a>
16. <a href="#user-content-complications-followup">Complications: Followup</a>
17. <a href="#user-content-health-economics-rev-1">Health Economics (Rev 1)</a>
18. <a href="#user-content-health-economics-rev-2">Health Economics (Rev 2)</a>
19. <a href="#user-content-family-history-and-knowledge">Family History And Knowledge</a>
20. <a href="#user-content-integrated-care-review">Integrated Care Review</a>
21. <a href="#user-content-routine-appointment-1">Routine Appointment</a>

<a href="#user-content-1120">**1120.**</a>
1. <a href="#user-content-clinical-review-1">Clinical Review</a>
2. <a href="#user-content-hiv-initial-review-2">Hiv Initial Review</a>
3. <a href="#user-content-diabetes-initial-review-2">Diabetes Initial Review</a>
4. <a href="#user-content-indicators-2">Indicators</a>
5. <a href="#user-content-hypertension-initial-review-2">Hypertension Initial Review</a>
6. <a href="#user-content-hiv-review-1">Hiv Review</a>
7. <a href="#user-content-diabetes-review-1">Diabetes Review</a>
8. <a href="#user-content-hypertension-review-1">Hypertension Review</a>
9. <a href="#user-content-medications-2">Medications</a>
10. <a href="#user-content-drug-refill-hypertension-2">Drug Refill: Hypertension</a>
11. <a href="#user-content-drug-refill-diabetes-2">Drug Refill: Diabetes</a>
12. <a href="#user-content-drug-refill-hiv-2">Drug Refill: Hiv</a>
13. <a href="#user-content-hiv-medication-adherence-1">Hiv Medication Adherence</a>
14. <a href="#user-content-diabetes-medication-adherence-1">Diabetes Medication Adherence</a>
15. <a href="#user-content-hypertension-medication-adherence-1">Hypertension Medication Adherence</a>
16. <a href="#user-content-complications-followup-1">Complications: Followup</a>
17. <a href="#user-content-family-history-and-knowledge-1">Family History And Knowledge</a>
18. <a href="#user-content-integrated-care-review-1">Integrated Care Review</a>


### 1000



*Rendered on 2022-05-06 16:14*

#### Clinical Review: Baseline
*[missing model class docstring]*


*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_clinicalreviewbaseline
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_clinicalreviewbaseline
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: HIV**

**3.0.** Has the patient ever tested for HIV infection?
- db_table: inte_subject_clinicalreviewbaseline
- column: hiv_test
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**4.0.** How long ago was the patient's most recent HIV test?

&nbsp;&nbsp;&nbsp;&nbsp; *If positive, most recent HIV(+) test Format is `YYyMMm` or `DDd`. For example 3y10m, 12y7m ... or 7d, 0d ...*
- db_table: inte_subject_clinicalreviewbaseline
- column: hiv_test_ago
- type: CharField
- length: 8
- responses: *free text*
---

**5.0.** Date of patient's most recent HIV test?
- db_table: inte_subject_clinicalreviewbaseline
- column: hiv_test_date
- type: DateField
- format: YYYY-MM-DD
---

**6.0.** Has the patient ever tested <U>positive</U> for HIV infection?

&nbsp;&nbsp;&nbsp;&nbsp; *If yes, complete form `HIV Initial Review`*
- db_table: inte_subject_clinicalreviewbaseline
- column: hiv_dx
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**Section: Diabetes**

**7.0.** Has the patient ever tested for Diabetes?
- db_table: inte_subject_clinicalreviewbaseline
- column: dm_test
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**8.0.** If Yes, how long ago was the patient tested for Diabetes?

&nbsp;&nbsp;&nbsp;&nbsp; * Format is `YYyMMm` or `DDd`. For example 3y10m, 12y7m ... or 7d, 0d ...*
- db_table: inte_subject_clinicalreviewbaseline
- column: dm_test_ago
- type: CharField
- length: 8
- responses: *free text*
---

**9.0.** Date of patient's most recent Diabetes test?
- db_table: inte_subject_clinicalreviewbaseline
- column: dm_test_date
- type: DateField
- format: YYYY-MM-DD
---

**10.0.** Have you ever been diagnosed with Diabetes

&nbsp;&nbsp;&nbsp;&nbsp; *If yes, complete form `Diabetes Initial Review`*
- db_table: inte_subject_clinicalreviewbaseline
- column: dm_dx
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**Section: Hypertension**

**11.0.** Has the patient ever tested for Hypertension?
- db_table: inte_subject_clinicalreviewbaseline
- column: htn_test
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**12.0.** If Yes, how long ago was the patient tested for Hypertension?

&nbsp;&nbsp;&nbsp;&nbsp; * Format is `YYyMMm` or `DDd`. For example 3y10m, 12y7m ... or 7d, 0d ...*
- db_table: inte_subject_clinicalreviewbaseline
- column: htn_test_ago
- type: CharField
- length: 8
- responses: *free text*
---

**13.0.** Date of patient's most recent Hypertension test?
- db_table: inte_subject_clinicalreviewbaseline
- column: htn_test_date
- type: DateField
- format: YYYY-MM-DD
---

**14.0.** Has the patient ever been diagnosed with Hypertension

&nbsp;&nbsp;&nbsp;&nbsp; *If yes, complete form `Hypertension Initial Review`*
- db_table: inte_subject_clinicalreviewbaseline
- column: htn_dx
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**Section: Other**

**15.0.** Does the patient have any private or work-place health insurance?
- db_table: inte_subject_clinicalreviewbaseline
- column: health_insurance
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**16.0.** Does the patient belong to a ‘club’ that supports medicines purchase?
- db_table: inte_subject_clinicalreviewbaseline
- column: patient_club
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**Section: CRF status**

**17.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_clinicalreviewbaseline
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**18.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_clinicalreviewbaseline
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Indicators
*[missing model class docstring]*


*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_indicators
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_indicators
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: Weight and Height**

**3.0.** Weight:

&nbsp;&nbsp;&nbsp;&nbsp; *in kg*
- db_table: inte_subject_indicators
- column: weight
- type: DecimalField
---

**4.0.** Height:

&nbsp;&nbsp;&nbsp;&nbsp; *in centimeters*
- db_table: inte_subject_indicators
- column: height
- type: DecimalField
---

**Section: Blood Pressure: Reading 1**

**5.0.** Was a blood pressure reading taken
- db_table: inte_subject_indicators
- column: r1_taken
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**6.0.** reason not taken
- db_table: inte_subject_indicators
- column: r1_reason_not_taken
- type: TextField
- length: 250
---

**7.0.** Blood pressure: systolic

&nbsp;&nbsp;&nbsp;&nbsp; *in mm. format SYS, e.g. 120*
- db_table: inte_subject_indicators
- column: sys_blood_pressure_r1
- type: IntegerField
---

**8.0.** Blood pressure: diastolic

&nbsp;&nbsp;&nbsp;&nbsp; *in Hg. format DIA, e.g. 80*
- db_table: inte_subject_indicators
- column: dia_blood_pressure_r1
- type: IntegerField
---

**Section: Blood Pressure: Reading 2**

**9.0.** Was a <u>second</u> blood pressure reading taken
- db_table: inte_subject_indicators
- column: r2_taken
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `not_required`: *Not required* 
---

**10.0.** r2 reason not taken
- db_table: inte_subject_indicators
- column: r2_reason_not_taken
- type: TextField
- length: 250
---

**11.0.** Blood pressure: systolic

&nbsp;&nbsp;&nbsp;&nbsp; *in mm. format SYS, e.g. 120*
- db_table: inte_subject_indicators
- column: sys_blood_pressure_r2
- type: IntegerField
---

**12.0.** Blood pressure: diastolic

&nbsp;&nbsp;&nbsp;&nbsp; *in Hg. format DIA, e.g. 80*
- db_table: inte_subject_indicators
- column: dia_blood_pressure_r2
- type: IntegerField
---

**Section: CRF status**

**13.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_indicators
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**14.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_indicators
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Hiv Initial Review
*[missing model class docstring]*


*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_hivinitialreview
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_hivinitialreview
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: Diagnosis and Care**

**3.0.** How long ago was the patient diagnosed?

&nbsp;&nbsp;&nbsp;&nbsp; *If possible, provide the exact date below instead of estimating here. Format is `YYyMMm` or `DDd`. For example 3y10m, 12y7m ... or 7d, 0d ...*
- db_table: inte_subject_hivinitialreview
- column: dx_ago
- type: CharField
- length: 8
- responses: *free text*
---

**4.0.** Date patient diagnosed

&nbsp;&nbsp;&nbsp;&nbsp; *If possible, provide the exact date here instead of estimating above.*
- db_table: inte_subject_hivinitialreview
- column: dx_date
- type: DateField
- format: YYYY-MM-DD
---

**5.0.** Is the patient receiving care for HIV?
- db_table: inte_subject_hivinitialreview
- column: receives_care
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**6.0.** Where does the patient receive care for HIV
- db_table: inte_subject_hivinitialreview
- column: clinic
- type: CharField
- length: 15
- responses:
  - `this_clinic`: *Patient comes to this facility for their care* 
  - `OTHER`: *Patient goes to a different clinic* 
  - `N/A`: *Not applicable* 
---

**6.1.** If <u>not</u> attending here, where does the patient attend?
- db_table: inte_subject_hivinitialreview
- column: clinic_other
- type: CharField
- length: 50
- responses: *free text*
---

**Section: Monitoring and Treatment**

**7.0.** Has the patient started antiretroviral therapy (ART)?
- db_table: inte_subject_hivinitialreview
- column: arv_initiated
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**8.0.** How long ago did the patient start ART?

&nbsp;&nbsp;&nbsp;&nbsp; *If possible, provide the exact date below instead of estimating here. Format is `YYyMMm` or `DDd`. For example 3y10m, 12y7m ... or 7d, 0d ...*
- db_table: inte_subject_hivinitialreview
- column: arv_initiation_ago
- type: CharField
- length: 8
- responses: *free text*
---

**9.0.** Date started antiretroviral therapy (ART)

&nbsp;&nbsp;&nbsp;&nbsp; *If possible, provide the exact date here instead of estimating above.*
- db_table: inte_subject_hivinitialreview
- column: arv_initiation_actual_date
- type: DateField
- format: YYYY-MM-DD
---

**10.0.** Is the patient's most recent viral load result available?
- db_table: inte_subject_hivinitialreview
- column: has_vl
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `PENDING`: *Pending* 
  - `N/A`: *Not applicable* 
---

**11.0.** Most recent viral load

&nbsp;&nbsp;&nbsp;&nbsp; *copies/mL*
- db_table: inte_subject_hivinitialreview
- column: vl
- type: IntegerField
---

**12.0.** vl quantifier
- db_table: inte_subject_hivinitialreview
- column: vl_quantifier
- type: CharField
- length: 10
- responses:
  - `=`: *=* 
  - `>`: *>* 
  - `<`: *<* 
---

**13.0.** Date of most recent viral load
- db_table: inte_subject_hivinitialreview
- column: vl_date
- type: DateField
- format: YYYY-MM-DD
---

**14.0.** Is the patient's most recent CD4 result available?
- db_table: inte_subject_hivinitialreview
- column: has_cd4
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**15.0.** Most recent CD4

&nbsp;&nbsp;&nbsp;&nbsp; *cells/mm<sup>3</sup>*
- db_table: inte_subject_hivinitialreview
- column: cd4
- type: IntegerField
---

**16.0.** Date of most recent CD4
- db_table: inte_subject_hivinitialreview
- column: cd4_date
- type: DateField
- format: YYYY-MM-DD
---

**Section: CRF status**

**17.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_hivinitialreview
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**18.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_hivinitialreview
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Diabetes Initial Review
*[missing model class docstring]*


*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_dminitialreview
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_dminitialreview
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: Diagnosis and Treatment**

**3.0.** How long ago was the patient diagnosed?

&nbsp;&nbsp;&nbsp;&nbsp; *If possible, provide the exact date below instead of estimating here. Format is `YYyMMm` or `DDd`. For example 3y10m, 12y7m ... or 7d, 0d ...*
- db_table: inte_subject_dminitialreview
- column: dx_ago
- type: CharField
- length: 8
- responses: *free text*
---

**4.0.** Date patient diagnosed

&nbsp;&nbsp;&nbsp;&nbsp; *If possible, provide the exact date here instead of estimating above.*
- db_table: inte_subject_dminitialreview
- column: dx_date
- type: DateField
- format: YYYY-MM-DD
---

**5.0.** How is the patient's diabetes managed?
- db_table: inte_subject_dminitialreview
- column: managed_by
- type: CharField
- length: 25
- responses:
  - `insulin`: *Insulin injections* 
  - `drugs`: *Oral drugs* 
  - `diet_lifestyle`: *Diet and lifestyle alone* 
---

**6.0.** If the patient is taking medicines for diabetes, how long have they been taking these?

&nbsp;&nbsp;&nbsp;&nbsp; * Format is `YYyMMm` or `DDd`. For example 3y10m, 12y7m ... or 7d, 0d ...*
- db_table: inte_subject_dminitialreview
- column: med_start_ago
- type: CharField
- length: 8
- responses: *free text*
---

**Section: Blood Sugar Measurement**

**7.0.** Has the patient had their glucose measured in the last few months?
- db_table: inte_subject_dminitialreview
- column: glucose_performed
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**8.0.** Had the participant fasted?
- db_table: inte_subject_dminitialreview
- column: glucose_fasted
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**9.0.** glucose date
- db_table: inte_subject_dminitialreview
- column: glucose_date
- type: DateField
- format: YYYY-MM-DD
---

**10.0.** Glucose result
- db_table: inte_subject_dminitialreview
- column: glucose
- type: DecimalField
---

**11.0.** glucose quantifier
- db_table: inte_subject_dminitialreview
- column: glucose_quantifier
- type: CharField
- length: 10
- responses:
  - `N/A`: ** 
  - `=`: *=* 
  - `>`: *>* 
  - `>=`: *>=* 
  - `<`: *<* 
  - `<=`: *<=* 
---

**12.0.** Units (glucose)
- db_table: inte_subject_dminitialreview
- column: glucose_units
- type: CharField
- length: 15
- responses:
  - `mg/dL`: *mg/dL* 
  - `mmol/L`: *mmol/L (millimoles/L)* 
  - `N/A`: *Not applicable* 
---

**Section: CRF status**

**13.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_dminitialreview
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**14.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_dminitialreview
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Hypertension Initial Review
*[missing model class docstring]*


*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_htninitialreview
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_htninitialreview
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: Diagnosis and Treatment**

**3.0.** How long ago was the patient diagnosed?

&nbsp;&nbsp;&nbsp;&nbsp; *If possible, provide the exact date below instead of estimating here. Format is `YYyMMm` or `DDd`. For example 3y10m, 12y7m ... or 7d, 0d ...*
- db_table: inte_subject_htninitialreview
- column: dx_ago
- type: CharField
- length: 8
- responses: *free text*
---

**4.0.** Date patient diagnosed

&nbsp;&nbsp;&nbsp;&nbsp; *If possible, provide the exact date here instead of estimating above.*
- db_table: inte_subject_htninitialreview
- column: dx_date
- type: DateField
- format: YYYY-MM-DD
---

**5.0.** How is the patient's hypertension managed?
- db_table: inte_subject_htninitialreview
- column: managed_by
- type: CharField
- length: 15
- responses:
  - `drugs`: *Drugs / Medicine* 
  - `diet_lifestyle`: *Diet and lifestyle alone* 
---

**6.0.** If the patient is taking medicines for hypertension, how long have they been taking these?

&nbsp;&nbsp;&nbsp;&nbsp; * Format is `YYyMMm` or `DDd`. For example 3y10m, 12y7m ... or 7d, 0d ...*
- db_table: inte_subject_htninitialreview
- column: med_start_ago
- type: CharField
- length: 8
- responses: *free text*
---

**Section: CRF status**

**7.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_htninitialreview
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**8.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_htninitialreview
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Medications
*[missing model class docstring]*


*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_medications
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_medications
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: Prescriptions**

**3.0.** Is the patient filling / refilling Hypertension medications?

&nbsp;&nbsp;&nbsp;&nbsp; *Select `not applicable` if subject has not been diagnosed and prescribed medication for Hypertension.*
- db_table: inte_subject_medications
- column: refill_htn
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**4.0.** Is the patient filling / refilling Diabetes medications?

&nbsp;&nbsp;&nbsp;&nbsp; *Select `not applicable` if subject has not been diagnosed and prescribed medication for Diabetes.*
- db_table: inte_subject_medications
- column: refill_dm
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**5.0.** Is the patient filling / refilling HIV medications?

&nbsp;&nbsp;&nbsp;&nbsp; *Select `not applicable` if subject has not been diagnosed and prescribed medication for HIV infection.*
- db_table: inte_subject_medications
- column: refill_hiv
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**Section: CRF status**

**6.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_medications
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**7.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_medications
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Drug Refill: Hypertension
*[missing model class docstring]*


*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.

*Additional instructions*: <span style="color:orange">Note: Medications CRF must be completed first.</span>


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_drugrefillhtn
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_drugrefillhtn
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: Hypertension Drug Refill Today**

**3.0.** Which medicine did the patient receive today?
- db_table: inte_subject_drugrefillhtn
- column: rx
- type: ManyToManyField
- responses: *Select all that apply*
  - `aldactone`: *Aldactone (Spironolactone)* 
  - `amlodipine`: *Amlodipine* 
  - `atenolol`: *Atenolol* 
  - `atorvastatin`: *Atorvastatin* 
  - `bendroflumethiazide`: *Bendroflumethiazide* 
  - `bisoprolol`: *Bisoprolol* 
  - `candesartan`: *Candesartan* 
  - `captopril`: *Captopril* 
  - `carvedilol`: *Carvedilol* 
  - `clopidogrel`: *Clopidogrel* 
  - `enalapril`: *Enalapril* 
  - `frusemide`: *Frusemide* 
  - `hydralazine`: *Hydralazine* 
  - `hydrochlorothiazide`: *Hydrochlorothiazide* 
  - `irbesartan`: *Irbesartan* 
  - `irbesartan_hydrochlorothiazide`: *Irbesartan Hydrochlorothiazide* 
  - `junior_aspirin`: *Junior Aspirin* 
  - `lisinopril`: *Lisinopril* 
  - `losartan_h`: *losartan Hydrochlorothiazide (Losartan H/Repace H)* 
  - `losartan`: *losartan* 
  - `methyldopa`: *Methyldopa* 
  - `metoprolol`: *Metoprolol* 
  - `nifedipine`: *Nifedipine* 
  - `olmesartan`: *Olmesartan* 
  - `propanolol`: *Propanolol* 
  - `ramipril`: *Ramipril* 
  - `rosuvastatin`: *Rosuvastatin* 
  - `s-amlodipine`: *S-Amlodipine* 
  - `simvastatin`: *Simvastatin* 
  - `telmisartan`: *Telmisartan* 
  - `valsartan`: *Valsartan* 
  - `vitamin_b_folic_acid`: *Vitamin Bs + Folic Acid* 
  - `OTHER`: *Other treatment (specify below)* 
---

**3.1.** If other, please specify ...
- db_table: inte_subject_drugrefillhtn
- column: rx_other
- type: CharField
- length: 150
- responses: *free text*
---

**4.0.** Was the patient’s prescription changed at this visit compared with their prescription at the previous visit?
- db_table: inte_subject_drugrefillhtn
- column: rx_modified
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**5.0.** Which changes occurred?
- db_table: inte_subject_drugrefillhtn
- column: modifications
- type: ManyToManyField
- responses: *Select all that apply*
  - `dose_changes`: *Dose changes* 
  - `drugs_substitution`: *Drugs substitution* 
  - `drug_additions`: *Additional drugs added to existing regimen* 
  - `some_stopped`: *Some drugs stopped* 
  - `OTHER`: *Other, specify* 
---

**5.1.** If other, please specify ...
- db_table: inte_subject_drugrefillhtn
- column: modifications_other
- type: CharField
- length: 150
- responses: *free text*
---

**6.0.** Why did the patient’s previous prescription change?
- db_table: inte_subject_drugrefillhtn
- column: modifications_reason
- type: ManyToManyField
- responses: *Select all that apply*
  - `availability`: *Limited availability of drugs* 
  - `side_effects`: *Had side-effects* 
  - `feel_better`: *Felt well and stopped/reduced drug prescription* 
  - `OTHER`: *Other, specify* 
---

**6.1.** If other, please specify ...
- db_table: inte_subject_drugrefillhtn
- column: modifications_reason_other
- type: CharField
- length: 150
- responses: *free text*
---

**7.0.** In how many days has the patient been asked to return to clinic for a drug refill?
- db_table: inte_subject_drugrefillhtn
- column: return_in_days
- type: IntegerField
---

**Section: CRF status**

**8.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_drugrefillhtn
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**9.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_drugrefillhtn
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Drug Refill: Diabetes
*[missing model class docstring]*


*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.

*Additional instructions*: <span style="color:orange">Note: Medications CRF must be completed first.</span>


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_drugrefilldm
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_drugrefilldm
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: Diabetes Drug Refill Today**

**3.0.** Which medicine did the patient receive today?
- db_table: inte_subject_drugrefilldm
- column: rx
- type: ManyToManyField
- responses: *Select all that apply*
  - `glibenclamide_metformin`: *Glibenclamide + Metformin combo* 
  - `glibenclamide_s`: *Glibenclamide (S)* 
  - `gliclazide_s`: *Gliclazide (S)* 
  - `glimepiride_1mg_metformin`: *Glimepiride (1mg) + Metformin combo* 
  - `glimepiride_2mg_metformin`: *Glimepiride (2mg) + Metformin combo* 
  - `glimepiride_s`: *Glimepiride (S)* 
  - `glipizide_s`: *Glipizide (S)* 
  - `insulin`: *Insulin* 
  - `metformin_b`: *Metformin (B)* 
  - `pioglitazone`: *Pioglitazone* 
  - `pregabalin`: *Pregabalin (diabetic neuropathy)* 
  - `vitamin_b_folic_acid`: *Vitamin Bs + Folic Acid (Neuroton- diabetic neuropathy)* 
  - `OTHER`: *Other, specify* 
---

**3.1.** If other, please specify ...
- db_table: inte_subject_drugrefilldm
- column: rx_other
- type: CharField
- length: 150
- responses: *free text*
---

**4.0.** Was the patient’s prescription changed at this visit compared with their prescription at the previous visit?
- db_table: inte_subject_drugrefilldm
- column: rx_modified
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**5.0.** Which changes occurred?
- db_table: inte_subject_drugrefilldm
- column: modifications
- type: ManyToManyField
- responses: *Select all that apply*
  - `dose_changes`: *Dose changes* 
  - `drugs_substitution`: *Drugs substitution* 
  - `drug_additions`: *Additional drugs added to existing regimen* 
  - `some_stopped`: *Some drugs stopped* 
  - `OTHER`: *Other, specify* 
---

**5.1.** If other, please specify ...
- db_table: inte_subject_drugrefilldm
- column: modifications_other
- type: CharField
- length: 150
- responses: *free text*
---

**6.0.** Why did the patient’s previous prescription change?
- db_table: inte_subject_drugrefilldm
- column: modifications_reason
- type: ManyToManyField
- responses: *Select all that apply*
  - `availability`: *Limited availability of drugs* 
  - `side_effects`: *Had side-effects* 
  - `feel_better`: *Felt well and stopped/reduced drug prescription* 
  - `OTHER`: *Other, specify* 
---

**6.1.** If other, please specify ...
- db_table: inte_subject_drugrefilldm
- column: modifications_reason_other
- type: CharField
- length: 150
- responses: *free text*
---

**7.0.** In how many days has the patient been asked to return to clinic for a drug refill?
- db_table: inte_subject_drugrefilldm
- column: return_in_days
- type: IntegerField
---

**Section: CRF status**

**8.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_drugrefilldm
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**9.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_drugrefilldm
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Drug Refill: Hiv
*[missing model class docstring]*


*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.

*Additional instructions*: <span style="color:orange">Note: Medications CRF must be completed first.</span>


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_drugrefillhiv
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_drugrefillhiv
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: ART Drug Refill Today**

**3.0.** Which medicine did the patient receive today?
- db_table: inte_subject_drugrefillhiv
- column: rx
- type: ForeignKey
---

**3.1.** If other, please specify ...
- db_table: inte_subject_drugrefillhiv
- column: rx_other
- type: CharField
- length: 150
- responses: *free text*
---

**4.0.** Was the patient’s prescription changed at this visit compared with their prescription at the previous visit?
- db_table: inte_subject_drugrefillhiv
- column: rx_modified
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**5.0.** Which changes occurred?
- db_table: inte_subject_drugrefillhiv
- column: modifications
- type: ManyToManyField
- responses: *Select all that apply*
  - `dose_changes`: *Dose changes* 
  - `drugs_substitution`: *Drugs substitution* 
  - `drug_additions`: *Additional drugs added to existing regimen* 
  - `some_stopped`: *Some drugs stopped* 
  - `OTHER`: *Other, specify* 
---

**5.1.** If other, please specify ...
- db_table: inte_subject_drugrefillhiv
- column: modifications_other
- type: CharField
- length: 150
- responses: *free text*
---

**6.0.** Why did the patient’s previous prescription change?
- db_table: inte_subject_drugrefillhiv
- column: modifications_reason
- type: ManyToManyField
- responses: *Select all that apply*
  - `availability`: *Limited availability of drugs* 
  - `side_effects`: *Had side-effects* 
  - `feel_better`: *Felt well and stopped/reduced drug prescription* 
  - `OTHER`: *Other, specify* 
---

**6.1.** If other, please specify ...
- db_table: inte_subject_drugrefillhiv
- column: modifications_reason_other
- type: CharField
- length: 150
- responses: *free text*
---

**Section: Supply**

**7.0.** In how many days has the patient been asked to return to clinic for a drug refill?
- db_table: inte_subject_drugrefillhiv
- column: return_in_days
- type: IntegerField
---

**8.0.** How many days supplied by the clinic

&nbsp;&nbsp;&nbsp;&nbsp; *days*
- db_table: inte_subject_drugrefillhiv
- column: clinic_days
- type: IntegerField
---

**9.0.** How many days supplied by a club

&nbsp;&nbsp;&nbsp;&nbsp; *days*
- db_table: inte_subject_drugrefillhiv
- column: club_days
- type: IntegerField
---

**10.0.** How many days supplied by to be purchased

&nbsp;&nbsp;&nbsp;&nbsp; *This can be purchased by patient, through a medicines club that the patient belong to, through insurance or someone else has paid. *
- db_table: inte_subject_drugrefillhiv
- column: purchased_days
- type: IntegerField
---

**Section: CRF status**

**11.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_drugrefillhiv
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**12.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_drugrefillhiv
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Other Baseline Data
*[missing model class docstring]*


*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_otherbaselinedata
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_otherbaselinedata
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: Smoking**

**3.0.** Which of these options describes you
- db_table: inte_subject_otherbaselinedata
- column: smoking_status
- type: CharField
- length: 15
- responses:
  - `smoker`: *Currently smoke* 
  - `former_smoker`: *Used to smoke but stopped* 
  - `nonsmoker`: *Never smoked* 
---

**4.0.** If you used to smoke but stopped, how long ago did you stop

&nbsp;&nbsp;&nbsp;&nbsp; * Format is `YYyMMm` or `DDd`. For example 3y10m, 12y7m ... or 7d, 0d ...*
- db_table: inte_subject_otherbaselinedata
- column: smoker_quit_ago
- type: CharField
- length: 8
- responses: *free text*
---

**Section: Alcohol**

**5.0.** Do you drink alcohol?
- db_table: inte_subject_otherbaselinedata
- column: alcohol
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**6.0.** If yes, how often do you drink alcohol?
- db_table: inte_subject_otherbaselinedata
- column: alcohol_consumption
- type: CharField
- length: 25
- responses:
  - `ocassionally`: *Ocassionally* 
  - `1_2_per_week`: *1-2 times a week* 
  - `3_4_per_week`: *3-4 times a week* 
  - `daily`: *Daily* 
  - `N/A`: *Not applicable* 
---

**Section: Other**

**7.0.** What is the patient's employment status?
- db_table: inte_subject_otherbaselinedata
- column: employment_status
- type: CharField
- length: 25
- responses:
  - `professional`: *Professional / office work / business* 
  - `manual_work`: *Skilled / Unskilled manual work* 
  - `housewife`: *Housewife* 
  - `unemployed`: *Not working / seeking work* 
  - `retired`: *Retired* 
  - `OTHER`: *Other, please specify* 
---

**7.1.** If other, please specify ...
- db_table: inte_subject_otherbaselinedata
- column: employment_status_other
- type: CharField
- length: 35
- responses: *free text*
---

**8.0.** How much formal education does the patient have?
- db_table: inte_subject_otherbaselinedata
- column: education
- type: CharField
- length: 25
- responses:
  - `no_formal_education`: *No Formal Education* 
  - `primary`: *Up to primary* 
  - `secondary`: *Up to secondary / high school* 
  - `tertiary`: *university educated* 
---

**9.0.** Personal status?
- db_table: inte_subject_otherbaselinedata
- column: marital_status
- type: CharField
- length: 25
- responses:
  - `married`: *Married or living with someone* 
  - `single`: *Single* 
  - `divorced`: *Divorced* 
  - `widowed`: *Widow / Spinster* 
---

**Section: CRF status**

**10.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_otherbaselinedata
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**11.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_otherbaselinedata
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Complications: Baseline
*[missing model class docstring]*


*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_complicationsbaseline
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_complicationsbaseline
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: Complications**

**3.0.** Stroke
- db_table: inte_subject_complicationsbaseline
- column: stroke
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**4.0.** If yes, how long ago

&nbsp;&nbsp;&nbsp;&nbsp; * Format is `YYyMMm` or `DDd`. For example 3y10m, 12y7m ... or 7d, 0d ...*
- db_table: inte_subject_complicationsbaseline
- column: stroke_ago
- type: CharField
- length: 8
- responses: *free text*
---

**5.0.** Heart attack / heart failure
- db_table: inte_subject_complicationsbaseline
- column: heart_attack
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**6.0.** If yes, how long ago

&nbsp;&nbsp;&nbsp;&nbsp; * Format is `YYyMMm` or `DDd`. For example 3y10m, 12y7m ... or 7d, 0d ...*
- db_table: inte_subject_complicationsbaseline
- column: heart_attack_ago
- type: CharField
- length: 8
- responses: *free text*
---

**7.0.** Renal (kidney) disease
- db_table: inte_subject_complicationsbaseline
- column: renal_disease
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**8.0.** If yes, how long ago

&nbsp;&nbsp;&nbsp;&nbsp; * Format is `YYyMMm` or `DDd`. For example 3y10m, 12y7m ... or 7d, 0d ...*
- db_table: inte_subject_complicationsbaseline
- column: renal_disease_ago
- type: CharField
- length: 8
- responses: *free text*
---

**9.0.** Vision problems (e.g. blurred vision)
- db_table: inte_subject_complicationsbaseline
- column: vision
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**10.0.** If yes, how long ago

&nbsp;&nbsp;&nbsp;&nbsp; * Format is `YYyMMm` or `DDd`. For example 3y10m, 12y7m ... or 7d, 0d ...*
- db_table: inte_subject_complicationsbaseline
- column: vision_ago
- type: CharField
- length: 8
- responses: *free text*
---

**11.0.** Numbness / burning sensation
- db_table: inte_subject_complicationsbaseline
- column: numbness
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**12.0.** If yes, how long ago

&nbsp;&nbsp;&nbsp;&nbsp; * Format is `YYyMMm` or `DDd`. For example 3y10m, 12y7m ... or 7d, 0d ...*
- db_table: inte_subject_complicationsbaseline
- column: numbness_ago
- type: CharField
- length: 8
- responses: *free text*
---

**13.0.** Foot ulcers
- db_table: inte_subject_complicationsbaseline
- column: foot_ulcers
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**14.0.** If yes, how long ago

&nbsp;&nbsp;&nbsp;&nbsp; * Format is `YYyMMm` or `DDd`. For example 3y10m, 12y7m ... or 7d, 0d ...*
- db_table: inte_subject_complicationsbaseline
- column: foot_ulcers_ago
- type: CharField
- length: 8
- responses: *free text*
---

**15.0.** Are there any other major complications to report?
- db_table: inte_subject_complicationsbaseline
- column: complications
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**15.1.** complications other

&nbsp;&nbsp;&nbsp;&nbsp; *Please include dates*
- db_table: inte_subject_complicationsbaseline
- column: complications_other
- type: TextField
---

**Section: CRF status**

**16.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_complicationsbaseline
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**17.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_complicationsbaseline
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Routine Appointment
*[missing model class docstring]*


*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_nextappointment
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_nextappointment
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: HIV**

**3.0.** HIV clinic: next scheduled routine appointment

&nbsp;&nbsp;&nbsp;&nbsp; *if applicable.*
- db_table: inte_subject_nextappointment
- column: hiv_clinic_appt_date
- type: DateField
- format: YYYY-MM-DD
---

**Section: NCD (Joint Diabetes/Hypertension)**

**4.0.** NCD clinic: next scheduled routine appointment

&nbsp;&nbsp;&nbsp;&nbsp; *if applicable.*
- db_table: inte_subject_nextappointment
- column: ncd_clinic_appt_date
- type: DateField
- format: YYYY-MM-DD
---

**Section: Diabetes-only**

**5.0.** Diabetes-only clinic: next scheduled routine appointment

&nbsp;&nbsp;&nbsp;&nbsp; *if applicable.*
- db_table: inte_subject_nextappointment
- column: dm_clinic_appt_date
- type: DateField
- format: YYYY-MM-DD
---

**Section: Hypertension-only**

**6.0.** Hypertension-only clinic: next scheduled routine appointment

&nbsp;&nbsp;&nbsp;&nbsp; *if applicable.*
- db_table: inte_subject_nextappointment
- column: htn_clinic_appt_date
- type: DateField
- format: YYYY-MM-DD
---

**Section: Integrated Clinic**

**7.0.** Integrated clinic: next scheduled routine appointment

&nbsp;&nbsp;&nbsp;&nbsp; *if applicable.*
- db_table: inte_subject_nextappointment
- column: integrated_clinic_appt_date
- type: DateField
- format: YYYY-MM-DD
---

**Section: CRF status**

**8.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_nextappointment
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**9.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_nextappointment
- column: crf_status_comments
- type: TextField
---


#### Requisitions

### 1060



*Rendered on 2022-05-06 16:14*

#### Clinical Review
*[missing model class docstring]*


*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_clinicalreview
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_clinicalreview
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: HYPERTENSION**

**3.0.** Since last seen, was the patient tested for hypertension?

&nbsp;&nbsp;&nbsp;&nbsp; *Note: Select `not applicable` if diagnosis previously reported. <BR>`Since last seen` includes today.<BR>If `yes', complete the initial review CRF<BR>If `not applicable`, complete the review CRF.*
- db_table: inte_subject_clinicalreview
- column: htn_test
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**4.0.** Date test requested
- db_table: inte_subject_clinicalreview
- column: htn_test_date
- type: DateField
- format: YYYY-MM-DD
---

**5.0.** Why was the patient tested for hypertension?
- db_table: inte_subject_clinicalreview
- column: htn_reason
- type: ManyToManyField
- responses: *Select all that apply*
  - `patient_request`: *Patient was well and made a request* 
  - `patient_complication`: *Patient had a clinical complication* 
  - `signs_symptoms`: *Patient had suggestive signs and symptoms* 
  - `OTHER`: *Other reason (specify below)* 
---

**5.1.** If other, please specify ...
- db_table: inte_subject_clinicalreview
- column: htn_reason_other
- type: CharField
- length: 35
- responses: *free text*
---

**6.0.** As of today, was the patient <u>newly</u> diagnosed with hypertension?
- db_table: inte_subject_clinicalreview
- column: htn_dx
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**Section: DIABETES**

**7.0.** Since last seen, was the patient tested for diabetes?

&nbsp;&nbsp;&nbsp;&nbsp; *Note: Select `not applicable` if diagnosis previously reported. <BR>`Since last seen` includes today.<BR>If `yes', complete the initial review CRF<BR>If `not applicable`, complete the review CRF.*
- db_table: inte_subject_clinicalreview
- column: dm_test
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**8.0.** Date test requested
- db_table: inte_subject_clinicalreview
- column: dm_test_date
- type: DateField
- format: YYYY-MM-DD
---

**9.0.** Why was the patient tested for diabetes?
- db_table: inte_subject_clinicalreview
- column: dm_reason
- type: ManyToManyField
- responses: *Select all that apply*
  - `patient_request`: *Patient was well and made a request* 
  - `patient_complication`: *Patient had a clinical complication* 
  - `signs_symptoms`: *Patient had suggestive signs and symptoms* 
  - `OTHER`: *Other reason (specify below)* 
---

**9.1.** If other, please specify ...
- db_table: inte_subject_clinicalreview
- column: dm_reason_other
- type: CharField
- length: 35
- responses: *free text*
---

**10.0.** As of today, was the patient <u>newly</u> diagnosed with diabetes?
- db_table: inte_subject_clinicalreview
- column: dm_dx
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**Section: HIV**

**11.0.** Since last seen, was the patient tested for HIV infection?

&nbsp;&nbsp;&nbsp;&nbsp; *Note: Select `not applicable` if diagnosis previously reported. <BR>`Since last seen` includes today.<BR>If `yes', complete the initial review CRF<BR>If `not applicable`, complete the review CRF.*
- db_table: inte_subject_clinicalreview
- column: hiv_test
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**12.0.** Date test requested
- db_table: inte_subject_clinicalreview
- column: hiv_test_date
- type: DateField
- format: YYYY-MM-DD
---

**13.0.** Why was the patient tested for HIV infection?
- db_table: inte_subject_clinicalreview
- column: hiv_reason
- type: ManyToManyField
- responses: *Select all that apply*
  - `patient_request`: *Patient was well and made a request* 
  - `patient_complication`: *Patient had a clinical complication* 
  - `signs_symptoms`: *Patient had suggestive signs and symptoms* 
  - `OTHER`: *Other reason (specify below)* 
---

**13.1.** If other, please specify ...
- db_table: inte_subject_clinicalreview
- column: hiv_reason_other
- type: CharField
- length: 35
- responses: *free text*
---

**14.0.** As of today, was the patient <u>newly</u> diagnosed with HIV infection?
- db_table: inte_subject_clinicalreview
- column: hiv_dx
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**Section: Complications**

**15.0.** Since last seen, has the patient had any complications

&nbsp;&nbsp;&nbsp;&nbsp; *If Yes, complete the `Complications` CRF*
- db_table: inte_subject_clinicalreview
- column: complications
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**Section: Other**

**16.0.** Does the patient have any private or work-place health insurance?
- db_table: inte_subject_clinicalreview
- column: health_insurance
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**17.0.** In the last month, how much has the patient spent on health insurance

&nbsp;&nbsp;&nbsp;&nbsp; *amount in local currency*
- db_table: inte_subject_clinicalreview
- column: health_insurance_monthly_pay
- type: IntegerField
---

**18.0.** Does the patient belong to a ‘club’ that supports medicines purchase?
- db_table: inte_subject_clinicalreview
- column: patient_club
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**19.0.** In the last month, how much has the patient spent on club membership

&nbsp;&nbsp;&nbsp;&nbsp; *amount in local currency*
- db_table: inte_subject_clinicalreview
- column: patient_club_monthly_pay
- type: IntegerField
---

**Section: CRF status**

**20.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_clinicalreview
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**21.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_clinicalreview
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Hiv Initial Review
*[missing model class docstring]*


*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_hivinitialreview
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_hivinitialreview
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: Diagnosis and Care**

**3.0.** How long ago was the patient diagnosed?

&nbsp;&nbsp;&nbsp;&nbsp; *If possible, provide the exact date below instead of estimating here. Format is `YYyMMm` or `DDd`. For example 3y10m, 12y7m ... or 7d, 0d ...*
- db_table: inte_subject_hivinitialreview
- column: dx_ago
- type: CharField
- length: 8
- responses: *free text*
---

**4.0.** Date patient diagnosed

&nbsp;&nbsp;&nbsp;&nbsp; *If possible, provide the exact date here instead of estimating above.*
- db_table: inte_subject_hivinitialreview
- column: dx_date
- type: DateField
- format: YYYY-MM-DD
---

**5.0.** Is the patient receiving care for HIV?
- db_table: inte_subject_hivinitialreview
- column: receives_care
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**6.0.** Where does the patient receive care for HIV
- db_table: inte_subject_hivinitialreview
- column: clinic
- type: CharField
- length: 15
- responses:
  - `this_clinic`: *Patient comes to this facility for their care* 
  - `OTHER`: *Patient goes to a different clinic* 
  - `N/A`: *Not applicable* 
---

**6.1.** If <u>not</u> attending here, where does the patient attend?
- db_table: inte_subject_hivinitialreview
- column: clinic_other
- type: CharField
- length: 50
- responses: *free text*
---

**Section: Monitoring and Treatment**

**7.0.** Has the patient started antiretroviral therapy (ART)?
- db_table: inte_subject_hivinitialreview
- column: arv_initiated
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**8.0.** How long ago did the patient start ART?

&nbsp;&nbsp;&nbsp;&nbsp; *If possible, provide the exact date below instead of estimating here. Format is `YYyMMm` or `DDd`. For example 3y10m, 12y7m ... or 7d, 0d ...*
- db_table: inte_subject_hivinitialreview
- column: arv_initiation_ago
- type: CharField
- length: 8
- responses: *free text*
---

**9.0.** Date started antiretroviral therapy (ART)

&nbsp;&nbsp;&nbsp;&nbsp; *If possible, provide the exact date here instead of estimating above.*
- db_table: inte_subject_hivinitialreview
- column: arv_initiation_actual_date
- type: DateField
- format: YYYY-MM-DD
---

**10.0.** Is the patient's most recent viral load result available?
- db_table: inte_subject_hivinitialreview
- column: has_vl
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `PENDING`: *Pending* 
  - `N/A`: *Not applicable* 
---

**11.0.** Most recent viral load

&nbsp;&nbsp;&nbsp;&nbsp; *copies/mL*
- db_table: inte_subject_hivinitialreview
- column: vl
- type: IntegerField
---

**12.0.** vl quantifier
- db_table: inte_subject_hivinitialreview
- column: vl_quantifier
- type: CharField
- length: 10
- responses:
  - `=`: *=* 
  - `>`: *>* 
  - `<`: *<* 
---

**13.0.** Date of most recent viral load
- db_table: inte_subject_hivinitialreview
- column: vl_date
- type: DateField
- format: YYYY-MM-DD
---

**14.0.** Is the patient's most recent CD4 result available?
- db_table: inte_subject_hivinitialreview
- column: has_cd4
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**15.0.** Most recent CD4

&nbsp;&nbsp;&nbsp;&nbsp; *cells/mm<sup>3</sup>*
- db_table: inte_subject_hivinitialreview
- column: cd4
- type: IntegerField
---

**16.0.** Date of most recent CD4
- db_table: inte_subject_hivinitialreview
- column: cd4_date
- type: DateField
- format: YYYY-MM-DD
---

**Section: CRF status**

**17.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_hivinitialreview
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**18.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_hivinitialreview
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Diabetes Initial Review
*[missing model class docstring]*


*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_dminitialreview
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_dminitialreview
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: Diagnosis and Treatment**

**3.0.** How long ago was the patient diagnosed?

&nbsp;&nbsp;&nbsp;&nbsp; *If possible, provide the exact date below instead of estimating here. Format is `YYyMMm` or `DDd`. For example 3y10m, 12y7m ... or 7d, 0d ...*
- db_table: inte_subject_dminitialreview
- column: dx_ago
- type: CharField
- length: 8
- responses: *free text*
---

**4.0.** Date patient diagnosed

&nbsp;&nbsp;&nbsp;&nbsp; *If possible, provide the exact date here instead of estimating above.*
- db_table: inte_subject_dminitialreview
- column: dx_date
- type: DateField
- format: YYYY-MM-DD
---

**5.0.** How is the patient's diabetes managed?
- db_table: inte_subject_dminitialreview
- column: managed_by
- type: CharField
- length: 25
- responses:
  - `insulin`: *Insulin injections* 
  - `drugs`: *Oral drugs* 
  - `diet_lifestyle`: *Diet and lifestyle alone* 
---

**6.0.** If the patient is taking medicines for diabetes, how long have they been taking these?

&nbsp;&nbsp;&nbsp;&nbsp; * Format is `YYyMMm` or `DDd`. For example 3y10m, 12y7m ... or 7d, 0d ...*
- db_table: inte_subject_dminitialreview
- column: med_start_ago
- type: CharField
- length: 8
- responses: *free text*
---

**Section: Blood Sugar Measurement**

**7.0.** Has the patient had their glucose measured in the last few months?
- db_table: inte_subject_dminitialreview
- column: glucose_performed
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**8.0.** Had the participant fasted?
- db_table: inte_subject_dminitialreview
- column: glucose_fasted
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**9.0.** glucose date
- db_table: inte_subject_dminitialreview
- column: glucose_date
- type: DateField
- format: YYYY-MM-DD
---

**10.0.** Glucose result
- db_table: inte_subject_dminitialreview
- column: glucose
- type: DecimalField
---

**11.0.** glucose quantifier
- db_table: inte_subject_dminitialreview
- column: glucose_quantifier
- type: CharField
- length: 10
- responses:
  - `N/A`: ** 
  - `=`: *=* 
  - `>`: *>* 
  - `>=`: *>=* 
  - `<`: *<* 
  - `<=`: *<=* 
---

**12.0.** Units (glucose)
- db_table: inte_subject_dminitialreview
- column: glucose_units
- type: CharField
- length: 15
- responses:
  - `mg/dL`: *mg/dL* 
  - `mmol/L`: *mmol/L (millimoles/L)* 
  - `N/A`: *Not applicable* 
---

**Section: CRF status**

**13.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_dminitialreview
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**14.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_dminitialreview
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Indicators
*[missing model class docstring]*


*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_indicators
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_indicators
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: Weight and Height**

**3.0.** Weight:

&nbsp;&nbsp;&nbsp;&nbsp; *in kg*
- db_table: inte_subject_indicators
- column: weight
- type: DecimalField
---

**4.0.** Height:

&nbsp;&nbsp;&nbsp;&nbsp; *in centimeters*
- db_table: inte_subject_indicators
- column: height
- type: DecimalField
---

**Section: Blood Pressure: Reading 1**

**5.0.** Was a blood pressure reading taken
- db_table: inte_subject_indicators
- column: r1_taken
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**6.0.** reason not taken
- db_table: inte_subject_indicators
- column: r1_reason_not_taken
- type: TextField
- length: 250
---

**7.0.** Blood pressure: systolic

&nbsp;&nbsp;&nbsp;&nbsp; *in mm. format SYS, e.g. 120*
- db_table: inte_subject_indicators
- column: sys_blood_pressure_r1
- type: IntegerField
---

**8.0.** Blood pressure: diastolic

&nbsp;&nbsp;&nbsp;&nbsp; *in Hg. format DIA, e.g. 80*
- db_table: inte_subject_indicators
- column: dia_blood_pressure_r1
- type: IntegerField
---

**Section: Blood Pressure: Reading 2**

**9.0.** Was a <u>second</u> blood pressure reading taken
- db_table: inte_subject_indicators
- column: r2_taken
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `not_required`: *Not required* 
---

**10.0.** r2 reason not taken
- db_table: inte_subject_indicators
- column: r2_reason_not_taken
- type: TextField
- length: 250
---

**11.0.** Blood pressure: systolic

&nbsp;&nbsp;&nbsp;&nbsp; *in mm. format SYS, e.g. 120*
- db_table: inte_subject_indicators
- column: sys_blood_pressure_r2
- type: IntegerField
---

**12.0.** Blood pressure: diastolic

&nbsp;&nbsp;&nbsp;&nbsp; *in Hg. format DIA, e.g. 80*
- db_table: inte_subject_indicators
- column: dia_blood_pressure_r2
- type: IntegerField
---

**Section: CRF status**

**13.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_indicators
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**14.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_indicators
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Hypertension Initial Review
*[missing model class docstring]*


*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_htninitialreview
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_htninitialreview
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: Diagnosis and Treatment**

**3.0.** How long ago was the patient diagnosed?

&nbsp;&nbsp;&nbsp;&nbsp; *If possible, provide the exact date below instead of estimating here. Format is `YYyMMm` or `DDd`. For example 3y10m, 12y7m ... or 7d, 0d ...*
- db_table: inte_subject_htninitialreview
- column: dx_ago
- type: CharField
- length: 8
- responses: *free text*
---

**4.0.** Date patient diagnosed

&nbsp;&nbsp;&nbsp;&nbsp; *If possible, provide the exact date here instead of estimating above.*
- db_table: inte_subject_htninitialreview
- column: dx_date
- type: DateField
- format: YYYY-MM-DD
---

**5.0.** How is the patient's hypertension managed?
- db_table: inte_subject_htninitialreview
- column: managed_by
- type: CharField
- length: 15
- responses:
  - `drugs`: *Drugs / Medicine* 
  - `diet_lifestyle`: *Diet and lifestyle alone* 
---

**6.0.** If the patient is taking medicines for hypertension, how long have they been taking these?

&nbsp;&nbsp;&nbsp;&nbsp; * Format is `YYyMMm` or `DDd`. For example 3y10m, 12y7m ... or 7d, 0d ...*
- db_table: inte_subject_htninitialreview
- column: med_start_ago
- type: CharField
- length: 8
- responses: *free text*
---

**Section: CRF status**

**7.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_htninitialreview
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**8.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_htninitialreview
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Hiv Review
*[missing model class docstring]*


*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_hivreview
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_hivreview
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: Care**

**3.0.** Was care for this `condition` delivered in an integrated care clinic today?

&nbsp;&nbsp;&nbsp;&nbsp; *Select `not applicable` if site was not selected for integrated care.*
- db_table: inte_subject_hivreview
- column: care_delivery
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**3.1.** If no, please explain
- db_table: inte_subject_hivreview
- column: care_delivery_other
- type: TextField
---

**Section: Anit-retroviral therapy (ART)**

**4.0.** Has the patient started antiretroviral therapy (ART)?

&nbsp;&nbsp;&nbsp;&nbsp; *Select `not applicable` if previously reported.*
- db_table: inte_subject_hivreview
- column: arv_initiated
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**5.0.** Date started antiretroviral therapy (ART)
- db_table: inte_subject_hivreview
- column: arv_initiation_actual_date
- type: DateField
- format: YYYY-MM-DD
---

**Section: CRF status**

**6.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_hivreview
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**7.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_hivreview
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Diabetes Review
*[missing model class docstring]*


*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_dmreview
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_dmreview
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: Care**

**3.0.** How will the patient's diabetes be managed going forward?
- db_table: inte_subject_dmreview
- column: managed_by
- type: CharField
- length: 25
- responses:
  - `insulin`: *Insulin injections* 
  - `drugs`: *Oral drugs* 
  - `diet_lifestyle`: *Diet and lifestyle alone* 
---

**4.0.** Was care for this `condition` delivered in an integrated care clinic today?

&nbsp;&nbsp;&nbsp;&nbsp; *Select `not applicable` if site was not selected for integrated care.*
- db_table: inte_subject_dmreview
- column: care_delivery
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**4.1.** If no, please explain
- db_table: inte_subject_dmreview
- column: care_delivery_other
- type: TextField
---

**Section: Blood Sugar Measurement**

**5.0.** Had the participant fasted?
- db_table: inte_subject_dmreview
- column: glucose_fasted
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**6.0.** glucose date
- db_table: inte_subject_dmreview
- column: glucose_date
- type: DateField
- format: YYYY-MM-DD
---

**7.0.** Glucose result
- db_table: inte_subject_dmreview
- column: glucose
- type: DecimalField
---

**8.0.** glucose quantifier
- db_table: inte_subject_dmreview
- column: glucose_quantifier
- type: CharField
- length: 10
- responses:
  - `N/A`: ** 
  - `=`: *=* 
  - `>`: *>* 
  - `>=`: *>=* 
  - `<`: *<* 
  - `<=`: *<=* 
---

**9.0.** Units (glucose)
- db_table: inte_subject_dmreview
- column: glucose_units
- type: CharField
- length: 15
- responses:
  - `mg/dL`: *mg/dL* 
  - `mmol/L`: *mmol/L (millimoles/L)* 
  - `N/A`: *Not applicable* 
---

**Section: CRF status**

**10.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_dmreview
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**11.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_dmreview
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Hypertension Review
*[missing model class docstring]*


*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_htnreview
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_htnreview
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: Care**

**3.0.** How will the patient's hypertension be managed going forward?
- db_table: inte_subject_htnreview
- column: managed_by
- type: CharField
- length: 25
- responses:
  - `drugs`: *Drugs / Medicine* 
  - `diet_lifestyle`: *Diet and lifestyle alone* 
---

**4.0.** Was care for this `condition` delivered in an integrated care clinic today?

&nbsp;&nbsp;&nbsp;&nbsp; *Select `not applicable` if site was not selected for integrated care.*
- db_table: inte_subject_htnreview
- column: care_delivery
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**4.1.** If no, please explain
- db_table: inte_subject_htnreview
- column: care_delivery_other
- type: TextField
---

**Section: Blood Pressure Measurement**

**5.0.** Blood pressure: systolic

&nbsp;&nbsp;&nbsp;&nbsp; *in mm. format SYS, e.g. 120*
- db_table: inte_subject_htnreview
- column: sys_blood_pressure
- type: IntegerField
---

**6.0.** Blood pressure: diastolic

&nbsp;&nbsp;&nbsp;&nbsp; *in Hg. format DIA, e.g. 80*
- db_table: inte_subject_htnreview
- column: dia_blood_pressure
- type: IntegerField
---

**Section: CRF status**

**7.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_htnreview
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**8.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_htnreview
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Medications
*[missing model class docstring]*


*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_medications
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_medications
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: Prescriptions**

**3.0.** Is the patient filling / refilling Hypertension medications?

&nbsp;&nbsp;&nbsp;&nbsp; *Select `not applicable` if subject has not been diagnosed and prescribed medication for Hypertension.*
- db_table: inte_subject_medications
- column: refill_htn
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**4.0.** Is the patient filling / refilling Diabetes medications?

&nbsp;&nbsp;&nbsp;&nbsp; *Select `not applicable` if subject has not been diagnosed and prescribed medication for Diabetes.*
- db_table: inte_subject_medications
- column: refill_dm
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**5.0.** Is the patient filling / refilling HIV medications?

&nbsp;&nbsp;&nbsp;&nbsp; *Select `not applicable` if subject has not been diagnosed and prescribed medication for HIV infection.*
- db_table: inte_subject_medications
- column: refill_hiv
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**Section: CRF status**

**6.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_medications
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**7.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_medications
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Drug Refill: Hypertension
*[missing model class docstring]*


*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.

*Additional instructions*: <span style="color:orange">Note: Medications CRF must be completed first.</span>


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_drugrefillhtn
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_drugrefillhtn
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: Hypertension Drug Refill Today**

**3.0.** Which medicine did the patient receive today?
- db_table: inte_subject_drugrefillhtn
- column: rx
- type: ManyToManyField
- responses: *Select all that apply*
  - `aldactone`: *Aldactone (Spironolactone)* 
  - `amlodipine`: *Amlodipine* 
  - `atenolol`: *Atenolol* 
  - `atorvastatin`: *Atorvastatin* 
  - `bendroflumethiazide`: *Bendroflumethiazide* 
  - `bisoprolol`: *Bisoprolol* 
  - `candesartan`: *Candesartan* 
  - `captopril`: *Captopril* 
  - `carvedilol`: *Carvedilol* 
  - `clopidogrel`: *Clopidogrel* 
  - `enalapril`: *Enalapril* 
  - `frusemide`: *Frusemide* 
  - `hydralazine`: *Hydralazine* 
  - `hydrochlorothiazide`: *Hydrochlorothiazide* 
  - `irbesartan`: *Irbesartan* 
  - `irbesartan_hydrochlorothiazide`: *Irbesartan Hydrochlorothiazide* 
  - `junior_aspirin`: *Junior Aspirin* 
  - `lisinopril`: *Lisinopril* 
  - `losartan_h`: *losartan Hydrochlorothiazide (Losartan H/Repace H)* 
  - `losartan`: *losartan* 
  - `methyldopa`: *Methyldopa* 
  - `metoprolol`: *Metoprolol* 
  - `nifedipine`: *Nifedipine* 
  - `olmesartan`: *Olmesartan* 
  - `propanolol`: *Propanolol* 
  - `ramipril`: *Ramipril* 
  - `rosuvastatin`: *Rosuvastatin* 
  - `s-amlodipine`: *S-Amlodipine* 
  - `simvastatin`: *Simvastatin* 
  - `telmisartan`: *Telmisartan* 
  - `valsartan`: *Valsartan* 
  - `vitamin_b_folic_acid`: *Vitamin Bs + Folic Acid* 
  - `OTHER`: *Other treatment (specify below)* 
---

**3.1.** If other, please specify ...
- db_table: inte_subject_drugrefillhtn
- column: rx_other
- type: CharField
- length: 150
- responses: *free text*
---

**4.0.** Was the patient’s prescription changed at this visit compared with their prescription at the previous visit?
- db_table: inte_subject_drugrefillhtn
- column: rx_modified
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**5.0.** Which changes occurred?
- db_table: inte_subject_drugrefillhtn
- column: modifications
- type: ManyToManyField
- responses: *Select all that apply*
  - `dose_changes`: *Dose changes* 
  - `drugs_substitution`: *Drugs substitution* 
  - `drug_additions`: *Additional drugs added to existing regimen* 
  - `some_stopped`: *Some drugs stopped* 
  - `OTHER`: *Other, specify* 
---

**5.1.** If other, please specify ...
- db_table: inte_subject_drugrefillhtn
- column: modifications_other
- type: CharField
- length: 150
- responses: *free text*
---

**6.0.** Why did the patient’s previous prescription change?
- db_table: inte_subject_drugrefillhtn
- column: modifications_reason
- type: ManyToManyField
- responses: *Select all that apply*
  - `availability`: *Limited availability of drugs* 
  - `side_effects`: *Had side-effects* 
  - `feel_better`: *Felt well and stopped/reduced drug prescription* 
  - `OTHER`: *Other, specify* 
---

**6.1.** If other, please specify ...
- db_table: inte_subject_drugrefillhtn
- column: modifications_reason_other
- type: CharField
- length: 150
- responses: *free text*
---

**7.0.** In how many days has the patient been asked to return to clinic for a drug refill?
- db_table: inte_subject_drugrefillhtn
- column: return_in_days
- type: IntegerField
---

**Section: CRF status**

**8.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_drugrefillhtn
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**9.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_drugrefillhtn
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Drug Refill: Diabetes
*[missing model class docstring]*


*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.

*Additional instructions*: <span style="color:orange">Note: Medications CRF must be completed first.</span>


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_drugrefilldm
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_drugrefilldm
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: Diabetes Drug Refill Today**

**3.0.** Which medicine did the patient receive today?
- db_table: inte_subject_drugrefilldm
- column: rx
- type: ManyToManyField
- responses: *Select all that apply*
  - `glibenclamide_metformin`: *Glibenclamide + Metformin combo* 
  - `glibenclamide_s`: *Glibenclamide (S)* 
  - `gliclazide_s`: *Gliclazide (S)* 
  - `glimepiride_1mg_metformin`: *Glimepiride (1mg) + Metformin combo* 
  - `glimepiride_2mg_metformin`: *Glimepiride (2mg) + Metformin combo* 
  - `glimepiride_s`: *Glimepiride (S)* 
  - `glipizide_s`: *Glipizide (S)* 
  - `insulin`: *Insulin* 
  - `metformin_b`: *Metformin (B)* 
  - `pioglitazone`: *Pioglitazone* 
  - `pregabalin`: *Pregabalin (diabetic neuropathy)* 
  - `vitamin_b_folic_acid`: *Vitamin Bs + Folic Acid (Neuroton- diabetic neuropathy)* 
  - `OTHER`: *Other, specify* 
---

**3.1.** If other, please specify ...
- db_table: inte_subject_drugrefilldm
- column: rx_other
- type: CharField
- length: 150
- responses: *free text*
---

**4.0.** Was the patient’s prescription changed at this visit compared with their prescription at the previous visit?
- db_table: inte_subject_drugrefilldm
- column: rx_modified
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**5.0.** Which changes occurred?
- db_table: inte_subject_drugrefilldm
- column: modifications
- type: ManyToManyField
- responses: *Select all that apply*
  - `dose_changes`: *Dose changes* 
  - `drugs_substitution`: *Drugs substitution* 
  - `drug_additions`: *Additional drugs added to existing regimen* 
  - `some_stopped`: *Some drugs stopped* 
  - `OTHER`: *Other, specify* 
---

**5.1.** If other, please specify ...
- db_table: inte_subject_drugrefilldm
- column: modifications_other
- type: CharField
- length: 150
- responses: *free text*
---

**6.0.** Why did the patient’s previous prescription change?
- db_table: inte_subject_drugrefilldm
- column: modifications_reason
- type: ManyToManyField
- responses: *Select all that apply*
  - `availability`: *Limited availability of drugs* 
  - `side_effects`: *Had side-effects* 
  - `feel_better`: *Felt well and stopped/reduced drug prescription* 
  - `OTHER`: *Other, specify* 
---

**6.1.** If other, please specify ...
- db_table: inte_subject_drugrefilldm
- column: modifications_reason_other
- type: CharField
- length: 150
- responses: *free text*
---

**7.0.** In how many days has the patient been asked to return to clinic for a drug refill?
- db_table: inte_subject_drugrefilldm
- column: return_in_days
- type: IntegerField
---

**Section: CRF status**

**8.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_drugrefilldm
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**9.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_drugrefilldm
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Drug Refill: Hiv
*[missing model class docstring]*


*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.

*Additional instructions*: <span style="color:orange">Note: Medications CRF must be completed first.</span>


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_drugrefillhiv
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_drugrefillhiv
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: ART Drug Refill Today**

**3.0.** Which medicine did the patient receive today?
- db_table: inte_subject_drugrefillhiv
- column: rx
- type: ForeignKey
---

**3.1.** If other, please specify ...
- db_table: inte_subject_drugrefillhiv
- column: rx_other
- type: CharField
- length: 150
- responses: *free text*
---

**4.0.** Was the patient’s prescription changed at this visit compared with their prescription at the previous visit?
- db_table: inte_subject_drugrefillhiv
- column: rx_modified
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**5.0.** Which changes occurred?
- db_table: inte_subject_drugrefillhiv
- column: modifications
- type: ManyToManyField
- responses: *Select all that apply*
  - `dose_changes`: *Dose changes* 
  - `drugs_substitution`: *Drugs substitution* 
  - `drug_additions`: *Additional drugs added to existing regimen* 
  - `some_stopped`: *Some drugs stopped* 
  - `OTHER`: *Other, specify* 
---

**5.1.** If other, please specify ...
- db_table: inte_subject_drugrefillhiv
- column: modifications_other
- type: CharField
- length: 150
- responses: *free text*
---

**6.0.** Why did the patient’s previous prescription change?
- db_table: inte_subject_drugrefillhiv
- column: modifications_reason
- type: ManyToManyField
- responses: *Select all that apply*
  - `availability`: *Limited availability of drugs* 
  - `side_effects`: *Had side-effects* 
  - `feel_better`: *Felt well and stopped/reduced drug prescription* 
  - `OTHER`: *Other, specify* 
---

**6.1.** If other, please specify ...
- db_table: inte_subject_drugrefillhiv
- column: modifications_reason_other
- type: CharField
- length: 150
- responses: *free text*
---

**Section: Supply**

**7.0.** In how many days has the patient been asked to return to clinic for a drug refill?
- db_table: inte_subject_drugrefillhiv
- column: return_in_days
- type: IntegerField
---

**8.0.** How many days supplied by the clinic

&nbsp;&nbsp;&nbsp;&nbsp; *days*
- db_table: inte_subject_drugrefillhiv
- column: clinic_days
- type: IntegerField
---

**9.0.** How many days supplied by a club

&nbsp;&nbsp;&nbsp;&nbsp; *days*
- db_table: inte_subject_drugrefillhiv
- column: club_days
- type: IntegerField
---

**10.0.** How many days supplied by to be purchased

&nbsp;&nbsp;&nbsp;&nbsp; *This can be purchased by patient, through a medicines club that the patient belong to, through insurance or someone else has paid. *
- db_table: inte_subject_drugrefillhiv
- column: purchased_days
- type: IntegerField
---

**Section: CRF status**

**11.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_drugrefillhiv
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**12.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_drugrefillhiv
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Hiv Medication Adherence
*[missing model class docstring]*


*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_hivmedicationadherence
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_hivmedicationadherence
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: Visual Score**

**3.0.** Visual adherence score for <U>condition_label</U> medication

&nbsp;&nbsp;&nbsp;&nbsp; *%*
- db_table: inte_subject_hivmedicationadherence
- column: visual_score_slider
- type: CharField
- length: 3
- responses: *free text*
---

**4.0.** <B><font color='orange'>Interviewer</font></B>: please confirm the score indicated from above.

&nbsp;&nbsp;&nbsp;&nbsp; *%*
- db_table: inte_subject_hivmedicationadherence
- column: visual_score_confirmed
- type: IntegerField
---

**Section: Missed Medications**

**5.0.** When was the last time you missed taking your <U>condition_label</U> medication?
- db_table: inte_subject_hivmedicationadherence
- column: last_missed_pill
- type: CharField
- length: 25
- responses:
  - `today`: *today* 
  - `yesterday`: *yesterday* 
  - `earlier_this_week`: *earlier this week* 
  - `last_week`: *last week* 
  - `lt_month_ago`: *less than a month ago* 
  - `gt_month_ago`: *more than a month ago* 
  - `NEVER`: *have never missed taking my study pills* 
---

**6.0.** Reasons for miss taking medication
- db_table: inte_subject_hivmedicationadherence
- column: missed_pill_reason
- type: ManyToManyField
- responses: *Select all that apply*
  - `forgot_to_take`: *I simply forgot to take my medication* 
  - `travelled`: *I travelled and forgot my medication* 
  - `feel_better`: *I felt better and stopped taking my medication* 
  - `insufficient_supply`: *I did not get enough medication from hospital/clinic, could not buy more* 
  - `feel_ill`: *The medications were making me feel sick* 
  - `too_many_pills`: *Too many pills so I stopped / reduced* 
  - `OTHER`: *Other, please specify ...* 
---

**7.0.** If other, please specify ...
- db_table: inte_subject_hivmedicationadherence
- column: other_missed_pill_reason
- type: CharField
- length: 35
- responses: *free text*
---

**Section: CRF status**

**8.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_hivmedicationadherence
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**9.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_hivmedicationadherence
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Diabetes Medication Adherence
*[missing model class docstring]*


*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_dmmedicationadherence
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_dmmedicationadherence
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: Visual Score**

**3.0.** Visual adherence score for <U>condition_label</U> medication

&nbsp;&nbsp;&nbsp;&nbsp; *%*
- db_table: inte_subject_dmmedicationadherence
- column: visual_score_slider
- type: CharField
- length: 3
- responses: *free text*
---

**4.0.** <B><font color='orange'>Interviewer</font></B>: please confirm the score indicated from above.

&nbsp;&nbsp;&nbsp;&nbsp; *%*
- db_table: inte_subject_dmmedicationadherence
- column: visual_score_confirmed
- type: IntegerField
---

**Section: Missed Medications**

**5.0.** When was the last time you missed taking your <U>condition_label</U> medication?
- db_table: inte_subject_dmmedicationadherence
- column: last_missed_pill
- type: CharField
- length: 25
- responses:
  - `today`: *today* 
  - `yesterday`: *yesterday* 
  - `earlier_this_week`: *earlier this week* 
  - `last_week`: *last week* 
  - `lt_month_ago`: *less than a month ago* 
  - `gt_month_ago`: *more than a month ago* 
  - `NEVER`: *have never missed taking my study pills* 
---

**6.0.** Reasons for miss taking medication
- db_table: inte_subject_dmmedicationadherence
- column: missed_pill_reason
- type: ManyToManyField
- responses: *Select all that apply*
  - `forgot_to_take`: *I simply forgot to take my medication* 
  - `travelled`: *I travelled and forgot my medication* 
  - `feel_better`: *I felt better and stopped taking my medication* 
  - `insufficient_supply`: *I did not get enough medication from hospital/clinic, could not buy more* 
  - `feel_ill`: *The medications were making me feel sick* 
  - `too_many_pills`: *Too many pills so I stopped / reduced* 
  - `OTHER`: *Other, please specify ...* 
---

**7.0.** If other, please specify ...
- db_table: inte_subject_dmmedicationadherence
- column: other_missed_pill_reason
- type: CharField
- length: 35
- responses: *free text*
---

**Section: CRF status**

**8.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_dmmedicationadherence
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**9.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_dmmedicationadherence
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Hypertension Medication Adherence
*[missing model class docstring]*


*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_htnmedicationadherence
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_htnmedicationadherence
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: Visual Score**

**3.0.** Visual adherence score for <U>condition_label</U> medication

&nbsp;&nbsp;&nbsp;&nbsp; *%*
- db_table: inte_subject_htnmedicationadherence
- column: visual_score_slider
- type: CharField
- length: 3
- responses: *free text*
---

**4.0.** <B><font color='orange'>Interviewer</font></B>: please confirm the score indicated from above.

&nbsp;&nbsp;&nbsp;&nbsp; *%*
- db_table: inte_subject_htnmedicationadherence
- column: visual_score_confirmed
- type: IntegerField
---

**Section: Missed Medications**

**5.0.** When was the last time you missed taking your <U>condition_label</U> medication?
- db_table: inte_subject_htnmedicationadherence
- column: last_missed_pill
- type: CharField
- length: 25
- responses:
  - `today`: *today* 
  - `yesterday`: *yesterday* 
  - `earlier_this_week`: *earlier this week* 
  - `last_week`: *last week* 
  - `lt_month_ago`: *less than a month ago* 
  - `gt_month_ago`: *more than a month ago* 
  - `NEVER`: *have never missed taking my study pills* 
---

**6.0.** Reasons for miss taking medication
- db_table: inte_subject_htnmedicationadherence
- column: missed_pill_reason
- type: ManyToManyField
- responses: *Select all that apply*
  - `forgot_to_take`: *I simply forgot to take my medication* 
  - `travelled`: *I travelled and forgot my medication* 
  - `feel_better`: *I felt better and stopped taking my medication* 
  - `insufficient_supply`: *I did not get enough medication from hospital/clinic, could not buy more* 
  - `feel_ill`: *The medications were making me feel sick* 
  - `too_many_pills`: *Too many pills so I stopped / reduced* 
  - `OTHER`: *Other, please specify ...* 
---

**7.0.** If other, please specify ...
- db_table: inte_subject_htnmedicationadherence
- column: other_missed_pill_reason
- type: CharField
- length: 35
- responses: *free text*
---

**Section: CRF status**

**8.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_htnmedicationadherence
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**9.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_htnmedicationadherence
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Complications: Followup
*[missing model class docstring]*


*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_complicationsfollowup
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_complicationsfollowup
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: Complications**

**3.0.** Stroke
- db_table: inte_subject_complicationsfollowup
- column: stroke
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**4.0.** If yes, date

&nbsp;&nbsp;&nbsp;&nbsp; *If exact date not known, see SOP on how to estimate a date.*
- db_table: inte_subject_complicationsfollowup
- column: stroke_date
- type: DateField
- format: YYYY-MM-DD
---

**5.0.** Heart attack / heart failure
- db_table: inte_subject_complicationsfollowup
- column: heart_attack
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**6.0.** If yes, date

&nbsp;&nbsp;&nbsp;&nbsp; *If exact date not known, see SOP on how to estimate a date.*
- db_table: inte_subject_complicationsfollowup
- column: heart_attack_date
- type: DateField
- format: YYYY-MM-DD
---

**7.0.** Renal (kidney) disease
- db_table: inte_subject_complicationsfollowup
- column: renal_disease
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**8.0.** If yes, date

&nbsp;&nbsp;&nbsp;&nbsp; *If exact date not known, see SOP on how to estimate a date.*
- db_table: inte_subject_complicationsfollowup
- column: renal_disease_date
- type: DateField
- format: YYYY-MM-DD
---

**9.0.** Vision problems (e.g. blurred vision)
- db_table: inte_subject_complicationsfollowup
- column: vision
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**10.0.** If yes, date

&nbsp;&nbsp;&nbsp;&nbsp; *If exact date not known, see SOP on how to estimate a date.*
- db_table: inte_subject_complicationsfollowup
- column: vision_date
- type: DateField
- format: YYYY-MM-DD
---

**11.0.** Numbness / burning sensation
- db_table: inte_subject_complicationsfollowup
- column: numbness
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**12.0.** If yes, date

&nbsp;&nbsp;&nbsp;&nbsp; *If exact date not known, see SOP on how to estimate a date.*
- db_table: inte_subject_complicationsfollowup
- column: numbness_date
- type: DateField
- format: YYYY-MM-DD
---

**13.0.** Foot ulcers
- db_table: inte_subject_complicationsfollowup
- column: foot_ulcers
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**14.0.** If yes, date

&nbsp;&nbsp;&nbsp;&nbsp; *If exact date not known, see SOP on how to estimate a date.*
- db_table: inte_subject_complicationsfollowup
- column: foot_ulcers_date
- type: DateField
- format: YYYY-MM-DD
---

**15.0.** Are there any other major complications to report?
- db_table: inte_subject_complicationsfollowup
- column: complications
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**15.1.** complications other

&nbsp;&nbsp;&nbsp;&nbsp; *Please include dates*
- db_table: inte_subject_complicationsfollowup
- column: complications_other
- type: TextField
---

**Section: CRF status**

**16.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_complicationsfollowup
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**17.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_complicationsfollowup
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Health Economics (Rev 1)
Second iteration of HE form.

    Retired April 2021.
*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_healtheconomicsrevised
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_healtheconomicsrevised
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: Part 1: Education**

**3.0.** What is your occupation/profession?
- db_table: inte_subject_healtheconomicsrevised
- column: occupation
- type: CharField
- length: 50
- responses: *free text*
---

**4.0.** How many years of education did you complete?
- db_table: inte_subject_healtheconomicsrevised
- column: education_in_years
- type: IntegerField
---

**5.0.** What is your highest education certificate?
- db_table: inte_subject_healtheconomicsrevised
- column: education_certificate
- type: CharField
- length: 50
- responses: *free text*
---

**6.0.** Did you go to primary/elementary school?
- db_table: inte_subject_healtheconomicsrevised
- column: primary_school
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**7.0.** If YES, for how many years
- db_table: inte_subject_healtheconomicsrevised
- column: primary_school_in_years
- type: IntegerField
---

**8.0.** Did you go to secondary school?
- db_table: inte_subject_healtheconomicsrevised
- column: secondary_school
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**9.0.** If YES, for how many years
- db_table: inte_subject_healtheconomicsrevised
- column: secondary_school_in_years
- type: IntegerField
---

**10.0.** Did you go to higher education?
- db_table: inte_subject_healtheconomicsrevised
- column: higher_education
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**11.0.** If YES, for how many years
- db_table: inte_subject_healtheconomicsrevised
- column: higher_education_in_years
- type: IntegerField
---

**Section: Part 2: Income**

**12.0.** Do you receive any welfare or social service support
- db_table: inte_subject_healtheconomicsrevised
- column: welfare
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**13.0.** How much do you earn (take home) per month?

&nbsp;&nbsp;&nbsp;&nbsp; *in local currency*
- db_table: inte_subject_healtheconomicsrevised
- column: income_per_month
- type: IntegerField
---

**14.0.** What is the total income in your household per month?

&nbsp;&nbsp;&nbsp;&nbsp; *in local currency*
- db_table: inte_subject_healtheconomicsrevised
- column: household_income_per_month
- type: IntegerField
---

**15.0.** Are you the person who earns the highest income in your household?
- db_table: inte_subject_healtheconomicsrevised
- column: is_highest_earner
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**16.0.** If NO, what is the profession of the person who earns the highest income?
- db_table: inte_subject_healtheconomicsrevised
- column: highest_earner
- type: CharField
- length: 50
- responses: *free text*
---

**Section: Part 3: General Expenses**

**17.0.** How much do you/your family spend on food in a month?

&nbsp;&nbsp;&nbsp;&nbsp; *in local currency*
- db_table: inte_subject_healtheconomicsrevised
- column: food_per_month
- type: IntegerField
---

**18.0.** How much do you/your family spend on rent (or house loan/mortgage) and utilities in a month?

&nbsp;&nbsp;&nbsp;&nbsp; *in local currency*
- db_table: inte_subject_healtheconomicsrevised
- column: accomodation_per_month
- type: IntegerField
---

**19.0.** How much have you spent on large items in the last year

&nbsp;&nbsp;&nbsp;&nbsp; *e.g. furniture, electrical items, cars (in local currency)*
- db_table: inte_subject_healtheconomicsrevised
- column: large_expenditure_year
- type: IntegerField
---

**Section: Part 4: Previous Healthcare Expenses: Medication**

**20.0.** Over the last month, did you get any drugs on your visit to the health facility?

&nbsp;&nbsp;&nbsp;&nbsp; *not including today*
- db_table: inte_subject_healtheconomicsrevised
- column: received_rx_month
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**Section: Part 4a: Previous Healthcare Expenses: Medication (Diabetes - DM)**

**21.0.** Did you receive drugs for raised blood sugar (diabetes) over the last month?

&nbsp;&nbsp;&nbsp;&nbsp; *not including today*
- db_table: inte_subject_healtheconomicsrevised
- column: rx_dm_month
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**22.0.** If YES, how were these paid for?
- db_table: inte_subject_healtheconomicsrevised
- column: rx_dm_paid_month
- type: ManyToManyField
- responses: *Select all that apply*
  - `own_cash`: *Own cash* 
  - `insurance`: *Insurance* 
  - `club`: *Patient support group / club* 
  - `relative`: *Relative or others paying* 
  - `free`: *Free drugs from the pharmacy* 
  - `OTHER`: *Other pay source (specify below)* 
---

**22.1.** If `other pay source`, please specify ... (DM)
- db_table: inte_subject_healtheconomicsrevised
- column: rx_dm_paid_month_other
- type: CharField
- length: 35
- responses: *free text*
---

**23.0.** If these drugs were not free, how much did you pay?

&nbsp;&nbsp;&nbsp;&nbsp; *In local currency*
- db_table: inte_subject_healtheconomicsrevised
- column: rx_dm_cost_month
- type: IntegerField
---

**Section: Part 4b: Previous Healthcare Expenses: Medication (Hypertension - HTN)**

**24.0.** Did you receive drugs for raised blood pressure (hypertension) over the last month?

&nbsp;&nbsp;&nbsp;&nbsp; *not including today*
- db_table: inte_subject_healtheconomicsrevised
- column: rx_htn_month
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**25.0.** If YES, how were these paid for?
- db_table: inte_subject_healtheconomicsrevised
- column: rx_htn_paid_month
- type: ManyToManyField
- responses: *Select all that apply*
  - `own_cash`: *Own cash* 
  - `insurance`: *Insurance* 
  - `club`: *Patient support group / club* 
  - `relative`: *Relative or others paying* 
  - `free`: *Free drugs from the pharmacy* 
  - `OTHER`: *Other pay source (specify below)* 
---

**25.1.** If `other pay source`, please specify ...(HTN)
- db_table: inte_subject_healtheconomicsrevised
- column: rx_htn_paid_month_other
- type: CharField
- length: 35
- responses: *free text*
---

**26.0.** If these drugs were not free, how much did you pay?

&nbsp;&nbsp;&nbsp;&nbsp; *In local currency*
- db_table: inte_subject_healtheconomicsrevised
- column: rx_htn_cost_month
- type: IntegerField
---

**Section: Part 4c: Previous Healthcare Expenses: Medication (HIV)**

**27.0.** Did you receive anti-retroviral drugs for HIV over the last month?

&nbsp;&nbsp;&nbsp;&nbsp; *not including today*
- db_table: inte_subject_healtheconomicsrevised
- column: rx_hiv_month
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**28.0.** If YES, how were these paid for?
- db_table: inte_subject_healtheconomicsrevised
- column: rx_hiv_paid_month
- type: ManyToManyField
- length: 25
- responses: *Select all that apply*
  - `own_cash`: *Own cash* 
  - `insurance`: *Insurance* 
  - `club`: *Patient support group / club* 
  - `relative`: *Relative or others paying* 
  - `free`: *Free drugs from the pharmacy* 
  - `OTHER`: *Other pay source (specify below)* 
---

**28.1.** If `other pay source`, please specify ... (HIV)
- db_table: inte_subject_healtheconomicsrevised
- column: rx_hiv_paid_month_other
- type: CharField
- length: 35
- responses: *free text*
---

**29.0.** If these drugs were not free, how much did you pay?

&nbsp;&nbsp;&nbsp;&nbsp; *In local currency*
- db_table: inte_subject_healtheconomicsrevised
- column: rx_hiv_cost_month
- type: IntegerField
---

**Section: Part 4d: Previous Healthcare Expenses: Other Medications**

**29.1.** Did you receive any 'other' drugs?
- db_table: inte_subject_healtheconomicsrevised
- column: rx_other_month
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**29.200000000000003.** If YES, received 'other' drugs, how were these paid for?
- db_table: inte_subject_healtheconomicsrevised
- column: rx_other_paid_month
- type: ManyToManyField
- responses: *Select all that apply*
  - `own_cash`: *Own cash* 
  - `insurance`: *Insurance* 
  - `club`: *Patient support group / club* 
  - `relative`: *Relative or others paying* 
  - `free`: *Free drugs from the pharmacy* 
  - `OTHER`: *Other pay source (specify below)* 
---

**29.300000000000004.** If `other pay source`, please specify ...
- db_table: inte_subject_healtheconomicsrevised
- column: rx_other_paid_month_other
- type: CharField
- length: 35
- responses: *free text*
---

**29.400000000000006.** If not free, how much did you pay for these 'other' drugs?

&nbsp;&nbsp;&nbsp;&nbsp; *In local currency*
- db_table: inte_subject_healtheconomicsrevised
- column: rx_other_cost_month
- type: IntegerField
---

**Section: Part 5: Previous Healthcare Expenses: Non-medication**

**30.0.** Over the last month, did you spend money on other activities (not drugs) relating to your health?
- db_table: inte_subject_healtheconomicsrevised
- column: non_drug_activities_month
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**31.0.** If YES, what was the activity
- db_table: inte_subject_healtheconomicsrevised
- column: non_drug_activities_detail_month
- type: TextField
---

**32.0.** If YES, how much was spent on other activities (not drugs) relating to your health?

&nbsp;&nbsp;&nbsp;&nbsp; *In local currency*
- db_table: inte_subject_healtheconomicsrevised
- column: non_drug_activities_cost_month
- type: IntegerField
---

**33.0.** How much in total has been spent on your healthcare in the last month?

&nbsp;&nbsp;&nbsp;&nbsp; *In local currency*
- db_table: inte_subject_healtheconomicsrevised
- column: healthcare_expenditure_total_month
- type: IntegerField
---

**Section: Part 6: Family Loss of Productivity and Earnings**

**34.0.** What would you be doing if you had not come to the health facility today?
- db_table: inte_subject_healtheconomicsrevised
- column: missed_routine_activities
- type: CharField
- length: 25
- responses:
  - `working`: *Working* 
  - `studying`: *Studying* 
  - `caring_for_children`: *Caring for children* 
  - `house_maintenance`: *House maintenance* 
  - `nothing`: *Nothing* 
  - `OTHER`: *Other, please specify* 
---

**34.1.** If OTHER, please specify
- db_table: inte_subject_healtheconomicsrevised
- column: missed_routine_activities_other
- type: CharField
- length: 50
- responses: *free text*
---

**35.0.** How much time did you take off work?

&nbsp;&nbsp;&nbsp;&nbsp; *in days. (1,2,3 etc. If half-day 0.5)*
- db_table: inte_subject_healtheconomicsrevised
- column: off_work_days
- type: DecimalField
---

**36.0.** How long did it take you to reach here?

&nbsp;&nbsp;&nbsp;&nbsp; *in hours and minutes (format HH:MM)*
- db_table: inte_subject_healtheconomicsrevised
- column: travel_time
- type: CharField
- length: 5
- responses: *free text*
---

**37.0.** How much time did you spend at the health care facility?

&nbsp;&nbsp;&nbsp;&nbsp; *in hours and minutes (format HH:MM)*
- db_table: inte_subject_healtheconomicsrevised
- column: hospital_time
- type: CharField
- length: 5
- responses: *free text*
---

**38.0.** Did you lose earnings as a result of coming here today? 
- db_table: inte_subject_healtheconomicsrevised
- column: lost_income
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**39.0.** If Yes, how much did you lose?

&nbsp;&nbsp;&nbsp;&nbsp; *In local currency*
- db_table: inte_subject_healtheconomicsrevised
- column: lost_income_amount
- type: IntegerField
---

**Section: Part 7: Work, Childcare, Transport**

**40.0.** Did you ask anyone else, such as your family member/friend to look after your child/children in order to come here?
- db_table: inte_subject_healtheconomicsrevised
- column: childcare
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**41.0.** If Yes, what would they have been doing if they had not stayed to look after your child or children?
- db_table: inte_subject_healtheconomicsrevised
- column: childcare_source
- type: CharField
- length: 25
- responses:
  - `N/A`: *Not applicable* 
  - `working`: *Working* 
  - `studying`: *Studying* 
  - `caring_for_children`: *Caring for children* 
  - `house_maintenance`: *House maintenance* 
  - `nothing`: *Nothing* 
  - `OTHER`: *Other, specify* 
---

**41.1.** If other, please specify ...
- db_table: inte_subject_healtheconomicsrevised
- column: childcare_source_other
- type: CharField
- length: 35
- responses: *free text*
---

**42.0.** How much time did a family member or friend take off?

&nbsp;&nbsp;&nbsp;&nbsp; *in days. (1,2,3 etc. If half-day 0.5)*
- db_table: inte_subject_healtheconomicsrevised
- column: childcare_source_timeoff
- type: DecimalField
---

**43.0.** Which form of transport did you take to get to the hospital today?
- db_table: inte_subject_healtheconomicsrevised
- column: transport
- type: ManyToManyField
- length: 25
- responses: *Select all that apply*
  - `bus`: *Bus* 
  - `train`: *Train* 
  - `ambulance`: *Ambulance* 
  - `private_taxi`: *Private taxi* 
  - `own_bicycle`: *Own bicycle* 
  - `hired_motorbike`: *Hired motorbike* 
  - `own_car`: *Own car* 
  - `own_motorbike`: *Own motorbike* 
  - `hired_bicycle`: *Hired bicycle* 
  - `foot`: *Foot* 
  - `OTHER`: *Other reason (specify below)* 
---

**43.1.** If `other reason`, please specify ...
- db_table: inte_subject_healtheconomicsrevised
- column: transport_other
- type: CharField
- length: 35
- responses: *free text*
---

**44.0.** How much did you spend on transport in total?

&nbsp;&nbsp;&nbsp;&nbsp; *Coming to the health care facility going back home. (In local currency)*
- db_table: inte_subject_healtheconomicsrevised
- column: transport_cost
- type: IntegerField
---

**45.0.** How much did you spend on food while you were at the health care faility today?

&nbsp;&nbsp;&nbsp;&nbsp; *In local currency*
- db_table: inte_subject_healtheconomicsrevised
- column: food_cost
- type: IntegerField
---

**Section: Part 8: Current Visit Healthcare Expenses: Medications**

**46.0.** Did you get any drugs on your visit to the health facility today?
- db_table: inte_subject_healtheconomicsrevised
- column: received_rx_today
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**Section: Part 8a: Current Visit Healthcare Expenses: Medications (Diabetes - DM)**

**47.0.** Did you receive drugs for raised blood sugar (diabetes) today?
- db_table: inte_subject_healtheconomicsrevised
- column: rx_dm_today
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**48.0.** If YES, received raised blood sugar (diabetes) drugs, how were these paid for?
- db_table: inte_subject_healtheconomicsrevised
- column: rx_dm_paid_today
- type: ManyToManyField
- responses: *Select all that apply*
  - `own_cash`: *Own cash* 
  - `insurance`: *Insurance* 
  - `club`: *Patient support group / club* 
  - `relative`: *Relative or others paying* 
  - `free`: *Free drugs from the pharmacy* 
  - `OTHER`: *Other pay source (specify below)* 
---

**48.1.** If `other pay source`, please specify ...
- db_table: inte_subject_healtheconomicsrevised
- column: rx_dm_paid_today_other
- type: CharField
- length: 35
- responses: *free text*
---

**49.0.** If not free, how much did you pay for raised blood sugar (diabetes) drugs?

&nbsp;&nbsp;&nbsp;&nbsp; *In local currency*
- db_table: inte_subject_healtheconomicsrevised
- column: rx_dm_cost_today
- type: IntegerField
---

**Section: Part 8b: Current Visit Healthcare Expenses: Medications (Hypertension - HTN)**

**50.0.** Did you receive raised blood pressure (hypertension) drugs today?
- db_table: inte_subject_healtheconomicsrevised
- column: rx_htn_today
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**51.0.** If YES, received high blood pressure (Hypertension) drugs, how were these paid for?
- db_table: inte_subject_healtheconomicsrevised
- column: rx_htn_paid_today
- type: ManyToManyField
- responses: *Select all that apply*
  - `own_cash`: *Own cash* 
  - `insurance`: *Insurance* 
  - `club`: *Patient support group / club* 
  - `relative`: *Relative or others paying* 
  - `free`: *Free drugs from the pharmacy* 
  - `OTHER`: *Other pay source (specify below)* 
---

**51.1.** If `other pay source`, please specify ...
- db_table: inte_subject_healtheconomicsrevised
- column: rx_htn_paid_today_other
- type: CharField
- length: 35
- responses: *free text*
---

**52.0.** If not free, how much did you pay for high blood pressure (Hypertension) drugs?

&nbsp;&nbsp;&nbsp;&nbsp; *In local currency*
- db_table: inte_subject_healtheconomicsrevised
- column: rx_htn_cost_today
- type: IntegerField
---

**Section: Part 8c: Current Visit Healthcare Expenses: Medications (HIV)**

**53.0.** Did you receive ARVs (HIV) today?
- db_table: inte_subject_healtheconomicsrevised
- column: rx_hiv_today
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**54.0.** If YES, received ARV (HIV) drugs, how were these paid for?
- db_table: inte_subject_healtheconomicsrevised
- column: rx_hiv_paid_today
- type: ManyToManyField
- length: 25
- responses: *Select all that apply*
  - `own_cash`: *Own cash* 
  - `insurance`: *Insurance* 
  - `club`: *Patient support group / club* 
  - `relative`: *Relative or others paying* 
  - `free`: *Free drugs from the pharmacy* 
  - `OTHER`: *Other pay source (specify below)* 
---

**54.1.** If `other pay source`, please specify ...
- db_table: inte_subject_healtheconomicsrevised
- column: rx_hiv_paid_today_other
- type: CharField
- length: 35
- responses: *free text*
---

**55.0.** If not free, how much did you pay for ARV (HIV) drugs?

&nbsp;&nbsp;&nbsp;&nbsp; *In local currency*
- db_table: inte_subject_healtheconomicsrevised
- column: rx_hiv_cost_today
- type: IntegerField
---

**Section: Part 8d: Current Visit Healthcare Expenses: Other Medications**

**55.1.** Did you receive 'other' drugs today?
- db_table: inte_subject_healtheconomicsrevised
- column: rx_other_today
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**55.2.** If YES, received 'other' drugs, how were these paid for?
- db_table: inte_subject_healtheconomicsrevised
- column: rx_other_paid_today
- type: ManyToManyField
- responses: *Select all that apply*
  - `own_cash`: *Own cash* 
  - `insurance`: *Insurance* 
  - `club`: *Patient support group / club* 
  - `relative`: *Relative or others paying* 
  - `free`: *Free drugs from the pharmacy* 
  - `OTHER`: *Other pay source (specify below)* 
---

**55.300000000000004.** If `other pay source`, please specify ...
- db_table: inte_subject_healtheconomicsrevised
- column: rx_other_paid_today_other
- type: CharField
- length: 35
- responses: *free text*
---

**55.400000000000006.** If not free, how much did you pay for these 'other' drugs?

&nbsp;&nbsp;&nbsp;&nbsp; *In local currency*
- db_table: inte_subject_healtheconomicsrevised
- column: rx_other_cost_today
- type: IntegerField
---

**Section: Part 9: Current Visit Healthcare Expenses: Non-medications**

**56.0.** Did you spend money on other activities (not drugs) relating to your health today?
- db_table: inte_subject_healtheconomicsrevised
- column: non_drug_activities_today
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**57.0.** If YES, what was the activity
- db_table: inte_subject_healtheconomicsrevised
- column: non_drug_activities_detail_today
- type: TextField
---

**58.0.** If YES, how much did you spend?

&nbsp;&nbsp;&nbsp;&nbsp; *In local currency*
- db_table: inte_subject_healtheconomicsrevised
- column: non_drug_activities_cost_today
- type: IntegerField
---

**59.0.** How much in total has been spent on your healthcare in the last month?

&nbsp;&nbsp;&nbsp;&nbsp; *In local currency*
- db_table: inte_subject_healtheconomicsrevised
- column: healthcare_expenditure_total_month_today
- type: IntegerField
---

**Section: Part 10: Health Care Financing**

**60.0.** Do you sell anything to pay for your visit today?
- db_table: inte_subject_healtheconomicsrevised
- column: finance_by_sale
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**61.0.** Did you take any loans to pay for your visit?
- db_table: inte_subject_healtheconomicsrevised
- column: finance_by_loan
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**62.0.** Do you have private healthcare insurance?
- db_table: inte_subject_healtheconomicsrevised
- column: health_insurance
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**63.0.** If Yes, how much do you pay towards your contributions to healthcare insurance every month?

&nbsp;&nbsp;&nbsp;&nbsp; *in local currency*
- db_table: inte_subject_healtheconomicsrevised
- column: health_insurance_cost
- type: IntegerField
---

**64.0.** Do you contribute to a patient club?
- db_table: inte_subject_healtheconomicsrevised
- column: patient_club
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**65.0.** If Yes, how much do you pay towards your contributions to the patient club every month?

&nbsp;&nbsp;&nbsp;&nbsp; *in local currency*
- db_table: inte_subject_healtheconomicsrevised
- column: patient_club_cost
- type: IntegerField
---

**Section: CRF status**

**66.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_healtheconomicsrevised
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**67.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_healtheconomicsrevised
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Health Economics (Rev 2)
Third iteration of HE form.
*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_healtheconomicsrevised
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_healtheconomicsrevised
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: Part 1: Education**

**3.0.** What is your occupation/profession?
- db_table: inte_subject_healtheconomicsrevised
- column: occupation
- type: CharField
- length: 50
- responses: *free text*
---

**4.0.** How many years of education did you complete?
- db_table: inte_subject_healtheconomicsrevised
- column: education_in_years
- type: IntegerField
---

**5.0.** What is your highest education certificate?
- db_table: inte_subject_healtheconomicsrevised
- column: education_certificate
- type: CharField
- length: 50
- responses: *free text*
---

**6.0.** Did you go to primary/elementary school?
- db_table: inte_subject_healtheconomicsrevised
- column: primary_school
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**7.0.** If YES, for how many years
- db_table: inte_subject_healtheconomicsrevised
- column: primary_school_in_years
- type: IntegerField
---

**8.0.** Did you go to secondary school?
- db_table: inte_subject_healtheconomicsrevised
- column: secondary_school
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**9.0.** If YES, for how many years
- db_table: inte_subject_healtheconomicsrevised
- column: secondary_school_in_years
- type: IntegerField
---

**10.0.** Did you go to higher education?
- db_table: inte_subject_healtheconomicsrevised
- column: higher_education
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**11.0.** If YES, for how many years
- db_table: inte_subject_healtheconomicsrevised
- column: higher_education_in_years
- type: IntegerField
---

**Section: Part 2: Income**

**12.0.** Do you receive any welfare or social service support
- db_table: inte_subject_healtheconomicsrevised
- column: welfare
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**Section: Part 3: Previous Healthcare Expenses: Medication**

**13.0.** Over the last month, did you get any drugs on your visit to the health facility?

&nbsp;&nbsp;&nbsp;&nbsp; *not including today*
- db_table: inte_subject_healtheconomicsrevised
- column: received_rx_month
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**Section: Part 3a: Previous Healthcare Expenses: Medication (Diabetes - DM)**

**14.0.** Did you receive drugs for raised blood sugar (diabetes) over the last month?

&nbsp;&nbsp;&nbsp;&nbsp; *not including today*
- db_table: inte_subject_healtheconomicsrevised
- column: rx_dm_month
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**15.0.** If YES, how were these paid for?
- db_table: inte_subject_healtheconomicsrevised
- column: rx_dm_paid_month
- type: ManyToManyField
- responses: *Select all that apply*
  - `own_cash`: *Own cash* 
  - `insurance`: *Insurance* 
  - `club`: *Patient support group / club* 
  - `relative`: *Relative or others paying* 
  - `free`: *Free drugs from the pharmacy* 
  - `OTHER`: *Other pay source (specify below)* 
---

**15.1.** If `other pay source`, please specify ... (DM)
- db_table: inte_subject_healtheconomicsrevised
- column: rx_dm_paid_month_other
- type: CharField
- length: 35
- responses: *free text*
---

**16.0.** If these drugs were not free, how much did you pay?

&nbsp;&nbsp;&nbsp;&nbsp; *In local currency*
- db_table: inte_subject_healtheconomicsrevised
- column: rx_dm_cost_month
- type: IntegerField
---

**Section: Part 3b: Previous Healthcare Expenses: Medication (Hypertension - HTN)**

**17.0.** Did you receive drugs for raised blood pressure (hypertension) over the last month?

&nbsp;&nbsp;&nbsp;&nbsp; *not including today*
- db_table: inte_subject_healtheconomicsrevised
- column: rx_htn_month
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**18.0.** If YES, how were these paid for?
- db_table: inte_subject_healtheconomicsrevised
- column: rx_htn_paid_month
- type: ManyToManyField
- responses: *Select all that apply*
  - `own_cash`: *Own cash* 
  - `insurance`: *Insurance* 
  - `club`: *Patient support group / club* 
  - `relative`: *Relative or others paying* 
  - `free`: *Free drugs from the pharmacy* 
  - `OTHER`: *Other pay source (specify below)* 
---

**18.1.** If `other pay source`, please specify ...(HTN)
- db_table: inte_subject_healtheconomicsrevised
- column: rx_htn_paid_month_other
- type: CharField
- length: 35
- responses: *free text*
---

**19.0.** If these drugs were not free, how much did you pay?

&nbsp;&nbsp;&nbsp;&nbsp; *In local currency*
- db_table: inte_subject_healtheconomicsrevised
- column: rx_htn_cost_month
- type: IntegerField
---

**Section: Part 3c: Previous Healthcare Expenses: Medication (HIV)**

**20.0.** Did you receive anti-retroviral drugs for HIV over the last month?

&nbsp;&nbsp;&nbsp;&nbsp; *not including today*
- db_table: inte_subject_healtheconomicsrevised
- column: rx_hiv_month
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**21.0.** If YES, how were these paid for?
- db_table: inte_subject_healtheconomicsrevised
- column: rx_hiv_paid_month
- type: ManyToManyField
- length: 25
- responses: *Select all that apply*
  - `own_cash`: *Own cash* 
  - `insurance`: *Insurance* 
  - `club`: *Patient support group / club* 
  - `relative`: *Relative or others paying* 
  - `free`: *Free drugs from the pharmacy* 
  - `OTHER`: *Other pay source (specify below)* 
---

**21.1.** If `other pay source`, please specify ... (HIV)
- db_table: inte_subject_healtheconomicsrevised
- column: rx_hiv_paid_month_other
- type: CharField
- length: 35
- responses: *free text*
---

**22.0.** If these drugs were not free, how much did you pay?

&nbsp;&nbsp;&nbsp;&nbsp; *In local currency*
- db_table: inte_subject_healtheconomicsrevised
- column: rx_hiv_cost_month
- type: IntegerField
---

**Section: Part 3d: Previous Healthcare Expenses: Other Medications**

**22.1.** Did you receive any 'other' drugs?
- db_table: inte_subject_healtheconomicsrevised
- column: rx_other_month
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**22.200000000000003.** If YES, received 'other' drugs, how were these paid for?
- db_table: inte_subject_healtheconomicsrevised
- column: rx_other_paid_month
- type: ManyToManyField
- responses: *Select all that apply*
  - `own_cash`: *Own cash* 
  - `insurance`: *Insurance* 
  - `club`: *Patient support group / club* 
  - `relative`: *Relative or others paying* 
  - `free`: *Free drugs from the pharmacy* 
  - `OTHER`: *Other pay source (specify below)* 
---

**22.300000000000004.** If `other pay source`, please specify ...
- db_table: inte_subject_healtheconomicsrevised
- column: rx_other_paid_month_other
- type: CharField
- length: 35
- responses: *free text*
---

**22.400000000000006.** If not free, how much did you pay for these 'other' drugs?

&nbsp;&nbsp;&nbsp;&nbsp; *In local currency*
- db_table: inte_subject_healtheconomicsrevised
- column: rx_other_cost_month
- type: IntegerField
---

**Section: Part 4: Current Visit Healthcare Expenses: Medications**

**23.0.** Did you get any drugs on your visit to the health facility today?
- db_table: inte_subject_healtheconomicsrevised
- column: received_rx_today
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**Section: Part 4a: Current Visit Healthcare Expenses: Medications (Diabetes - DM)**

**24.0.** Did you receive drugs for raised blood sugar (diabetes) today?
- db_table: inte_subject_healtheconomicsrevised
- column: rx_dm_today
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**25.0.** If YES, received raised blood sugar (diabetes) drugs, how were these paid for?
- db_table: inte_subject_healtheconomicsrevised
- column: rx_dm_paid_today
- type: ManyToManyField
- responses: *Select all that apply*
  - `own_cash`: *Own cash* 
  - `insurance`: *Insurance* 
  - `club`: *Patient support group / club* 
  - `relative`: *Relative or others paying* 
  - `free`: *Free drugs from the pharmacy* 
  - `OTHER`: *Other pay source (specify below)* 
---

**25.1.** If `other pay source`, please specify ...
- db_table: inte_subject_healtheconomicsrevised
- column: rx_dm_paid_today_other
- type: CharField
- length: 35
- responses: *free text*
---

**26.0.** If not free, how much did you pay for raised blood sugar (diabetes) drugs?

&nbsp;&nbsp;&nbsp;&nbsp; *In local currency*
- db_table: inte_subject_healtheconomicsrevised
- column: rx_dm_cost_today
- type: IntegerField
---

**Section: Part 4b: Current Visit Healthcare Expenses: Medications (Hypertension - HTN)**

**27.0.** Did you receive raised blood pressure (hypertension) drugs today?
- db_table: inte_subject_healtheconomicsrevised
- column: rx_htn_today
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**28.0.** If YES, received high blood pressure (Hypertension) drugs, how were these paid for?
- db_table: inte_subject_healtheconomicsrevised
- column: rx_htn_paid_today
- type: ManyToManyField
- responses: *Select all that apply*
  - `own_cash`: *Own cash* 
  - `insurance`: *Insurance* 
  - `club`: *Patient support group / club* 
  - `relative`: *Relative or others paying* 
  - `free`: *Free drugs from the pharmacy* 
  - `OTHER`: *Other pay source (specify below)* 
---

**28.1.** If `other pay source`, please specify ...
- db_table: inte_subject_healtheconomicsrevised
- column: rx_htn_paid_today_other
- type: CharField
- length: 35
- responses: *free text*
---

**29.0.** If not free, how much did you pay for high blood pressure (Hypertension) drugs?

&nbsp;&nbsp;&nbsp;&nbsp; *In local currency*
- db_table: inte_subject_healtheconomicsrevised
- column: rx_htn_cost_today
- type: IntegerField
---

**Section: Part 4c: Current Visit Healthcare Expenses: Medications (HIV)**

**30.0.** Did you receive ARVs (HIV) today?
- db_table: inte_subject_healtheconomicsrevised
- column: rx_hiv_today
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**31.0.** If YES, received ARV (HIV) drugs, how were these paid for?
- db_table: inte_subject_healtheconomicsrevised
- column: rx_hiv_paid_today
- type: ManyToManyField
- length: 25
- responses: *Select all that apply*
  - `own_cash`: *Own cash* 
  - `insurance`: *Insurance* 
  - `club`: *Patient support group / club* 
  - `relative`: *Relative or others paying* 
  - `free`: *Free drugs from the pharmacy* 
  - `OTHER`: *Other pay source (specify below)* 
---

**31.1.** If `other pay source`, please specify ...
- db_table: inte_subject_healtheconomicsrevised
- column: rx_hiv_paid_today_other
- type: CharField
- length: 35
- responses: *free text*
---

**32.0.** If not free, how much did you pay for ARV (HIV) drugs?

&nbsp;&nbsp;&nbsp;&nbsp; *In local currency*
- db_table: inte_subject_healtheconomicsrevised
- column: rx_hiv_cost_today
- type: IntegerField
---

**Section: Part 4d: Current Visit Healthcare Expenses: Other Medications**

**32.1.** Did you receive 'other' drugs today?
- db_table: inte_subject_healtheconomicsrevised
- column: rx_other_today
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**32.2.** If YES, received 'other' drugs, how were these paid for?
- db_table: inte_subject_healtheconomicsrevised
- column: rx_other_paid_today
- type: ManyToManyField
- responses: *Select all that apply*
  - `own_cash`: *Own cash* 
  - `insurance`: *Insurance* 
  - `club`: *Patient support group / club* 
  - `relative`: *Relative or others paying* 
  - `free`: *Free drugs from the pharmacy* 
  - `OTHER`: *Other pay source (specify below)* 
---

**32.300000000000004.** If `other pay source`, please specify ...
- db_table: inte_subject_healtheconomicsrevised
- column: rx_other_paid_today_other
- type: CharField
- length: 35
- responses: *free text*
---

**32.400000000000006.** If not free, how much did you pay for these 'other' drugs?

&nbsp;&nbsp;&nbsp;&nbsp; *In local currency*
- db_table: inte_subject_healtheconomicsrevised
- column: rx_other_cost_today
- type: IntegerField
---

**Section: Part 5: Health Care Financing**

**33.0.** Do you have private healthcare insurance?
- db_table: inte_subject_healtheconomicsrevised
- column: health_insurance
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**34.0.** If Yes, how much do you pay towards your contributions to healthcare insurance every month?

&nbsp;&nbsp;&nbsp;&nbsp; *in local currency*
- db_table: inte_subject_healtheconomicsrevised
- column: health_insurance_cost
- type: IntegerField
---

**35.0.** Do you contribute to a patient club?
- db_table: inte_subject_healtheconomicsrevised
- column: patient_club
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**36.0.** If Yes, how much do you pay towards your contributions to the patient club every month?

&nbsp;&nbsp;&nbsp;&nbsp; *in local currency*
- db_table: inte_subject_healtheconomicsrevised
- column: patient_club_cost
- type: IntegerField
---

**Section: CRF status**

**37.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_healtheconomicsrevised
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**38.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_healtheconomicsrevised
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Family History And Knowledge
*[missing model class docstring]*


*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_familyhistory
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_familyhistory
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: Part 1**

**3.0.** Do you know if anyone else in your household has <u>high blood pressure</u>?
- db_table: inte_subject_familyhistory
- column: htn_in_household
- type: CharField
- length: 25
- responses:
  - `No`: *No* 
  - `yes_spouse`: *Yes, my spouse* 
  - `yes_parents`: *Yes, one of my parents living with me* 
  - `yes_relative`: *Yes, another relative living with me* 
---

**4.0.** Do you know if anyone else in your household has <u>diabetes</u>?
- db_table: inte_subject_familyhistory
- column: dm_in_household
- type: CharField
- length: 25
- responses:
  - `No`: *No* 
  - `yes_spouse`: *Yes, my spouse* 
  - `yes_parents`: *Yes, one of my parents living with me* 
  - `yes_relative`: *Yes, another relative living with me* 
---

**5.0.** Do you know if anyone else in your household has <u>HIV</u>?
- db_table: inte_subject_familyhistory
- column: hiv_in_household
- type: CharField
- length: 25
- responses:
  - `No`: *No* 
  - `yes_spouse`: *Yes, my spouse* 
  - `yes_parents`: *Yes, one of my parents living with me* 
  - `yes_relative`: *Yes, another relative living with me* 
---

**Section: Part 2**

**6.0.** High blood pressure and high blood sugar can cause many illnesses like heart attacks, stroke, kidney failure
- db_table: inte_subject_familyhistory
- column: high_bp_bs_tf
- type: CharField
- length: 25
- responses:
  - `true`: *True* 
  - `false`: *False* 
  - `dont_know`: *Don't know* 
---

**7.0.** Being overweight protects from high blood pressure and high blood sugar
- db_table: inte_subject_familyhistory
- column: overweight_tf
- type: CharField
- length: 25
- responses:
  - `true`: *True* 
  - `false`: *False* 
  - `dont_know`: *Don't know* 
---

**8.0.** Salty food protects from high blood sugar
- db_table: inte_subject_familyhistory
- column: salty_foods_tf
- type: CharField
- length: 25
- responses:
  - `true`: *True* 
  - `false`: *False* 
  - `dont_know`: *Don't know* 
---

**9.0.** Regular exercise is important for people with <u>high blood pressure</u> or <u>high blood sugar</u> even if they are taking medicines for these conditions.
- db_table: inte_subject_familyhistory
- column: excercise_tf
- type: CharField
- length: 25
- responses:
  - `true`: *True* 
  - `false`: *False* 
  - `dont_know`: *Don't know* 
---

**10.0.** Drugs for <u>blood sugar</u> and <u>blood pressure</u> can make you unwell
- db_table: inte_subject_familyhistory
- column: take_medicine_tf
- type: CharField
- length: 25
- responses:
  - `true`: *True* 
  - `false`: *False* 
  - `dont_know`: *Don't know* 
---

**11.0.** It is best to stop taking <u>blood pressure</u> pills when you feel better and start pill taking again when you feel sick
- db_table: inte_subject_familyhistory
- column: stop_htn_meds_tf
- type: CharField
- length: 25
- responses:
  - `true`: *True* 
  - `false`: *False* 
  - `dont_know`: *Don't know* 
---

**12.0.** Herbs and traditional medicine are better for managing <u>blood pressure</u> than pills and medicines
- db_table: inte_subject_familyhistory
- column: traditional_htn_tf
- type: CharField
- length: 25
- responses:
  - `true`: *True* 
  - `false`: *False* 
  - `dont_know`: *Don't know* 
---

**13.0.** It is best to stop taking <u>blood sugar</u> medicines when you feel better and start pill taking again when you feel sick
- db_table: inte_subject_familyhistory
- column: stop_dm_meds_tf
- type: CharField
- length: 25
- responses:
  - `true`: *True* 
  - `false`: *False* 
  - `dont_know`: *Don't know* 
---

**14.0.** Herbs and traditional medicine are better for managing <u>diabetes</u> than pills and medicines
- db_table: inte_subject_familyhistory
- column: traditional_dm_tf
- type: CharField
- length: 25
- responses:
  - `true`: *True* 
  - `false`: *False* 
  - `dont_know`: *Don't know* 
---

**15.0.** Having drinks with sugar (e.g. tea/coffee) causes diabetes
- db_table: inte_subject_familyhistory
- column: dm_cause_tf
- type: CharField
- length: 25
- responses:
  - `true`: *True* 
  - `false`: *False* 
  - `dont_know`: *Don't know* 
---

**Section: CRF status**

**16.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_familyhistory
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**17.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_familyhistory
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Integrated Care Review
FORM 26 - Participant Review of Integrated Care.
*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_integratedcarereview
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_integratedcarereview
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: Part 1a: Counselling - Health Talks**

**3.0.** Did you receive a health talk when attending the clinic today?
- db_table: inte_subject_integratedcarereview
- column: receive_health_talk_messages
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**4.0.** If YES, what disease conditions were discussed?
- db_table: inte_subject_integratedcarereview
- column: health_talk_conditions
- type: ManyToManyField
- responses: *Select all that apply*
  - `HIV`: *HIV infection* 
  - `diabetes`: *Diabetes* 
  - `hypertension`: *Hypertension* 
  - `OTHER`: *Other condition (specify below)* 
---

**4.1.** If other, please specify ...
- db_table: inte_subject_integratedcarereview
- column: health_talk_conditions_other
- type: CharField
- length: 35
- responses: *free text*
---

**5.0.** If YES, what type of messages were covered?
- db_table: inte_subject_integratedcarereview
- column: health_talk_focus
- type: ManyToManyField
- responses: *Select all that apply*
  - `lifestyle`: *Lifestyle* 
  - `diet`: *Diet* 
  - `medicines`: *Medicines* 
  - `OTHER`: *Other (specify below)* 
---

**5.1.** If other, please specify ...
- db_table: inte_subject_integratedcarereview
- column: health_talk_focus_other
- type: CharField
- length: 35
- responses: *free text*
---

**6.0.** If YES, who gave the health talk?
- db_table: inte_subject_integratedcarereview
- column: health_talk_presenters
- type: ManyToManyField
- responses: *Select all that apply*
  - `nurse`: *Nurse* 
  - `expert_patient_or_volunteer`: *Expert patient/Volunteer* 
  - `clinical_or_medical_officer`: *Clinical or medical officer* 
  - `OTHER`: *Other (specify below)* 
---

**6.1.** If other, please specify ...
- db_table: inte_subject_integratedcarereview
- column: health_talk_presenters_other
- type: CharField
- length: 35
- responses: *free text*
---

**Section: Part 1b: Counselling - Additional Health Advice**

**7.0.** Did you receive any additional health advice during your visit?
- db_table: inte_subject_integratedcarereview
- column: additional_health_advice
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**8.0.** If YES, who gave this health advice?
- db_table: inte_subject_integratedcarereview
- column: health_advice_advisor
- type: ManyToManyField
- responses: *Select all that apply*
  - `nurse`: *Nurse* 
  - `expert_patient_or_volunteer`: *Expert patient/Volunteer* 
  - `clinical_or_medical_officer`: *Clinical or medical officer* 
  - `OTHER`: *Other (specify below)* 
---

**8.1.** If other, please specify ...
- db_table: inte_subject_integratedcarereview
- column: health_advice_advisor_other
- type: CharField
- length: 35
- responses: *free text*
---

**9.0.** If YES, what was the focus of the advice?
- db_table: inte_subject_integratedcarereview
- column: health_advice_focus
- type: ManyToManyField
- responses: *Select all that apply*
  - `lifestyle`: *Lifestyle* 
  - `diet`: *Diet* 
  - `medicines`: *Medicines* 
  - `OTHER`: *Other (specify below)* 
---

**9.1.** If other, please specify ...
- db_table: inte_subject_integratedcarereview
- column: health_advice_focus_other
- type: CharField
- length: 35
- responses: *free text*
---

**Section: Part 2: Pharmacy Services**

**10.0.** Did you receive a drug prescription today?
- db_table: inte_subject_integratedcarereview
- column: receive_rx_today
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**11.0.** If YES, are you collecting it from this healthcare facility?
- db_table: inte_subject_integratedcarereview
- column: rx_collection_hcf
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No, I buy my own drugs* 
  - `N/A`: *Not applicable* 
---

**12.0.** If YES, where in this healthcare facility are your drugs dispensed from?
- db_table: inte_subject_integratedcarereview
- column: where_rx_dispensed
- type: ManyToManyField
- responses: *Select all that apply*
  - `pharmacy`: *Pharmacy* 
  - `consulting_room`: *Consulting room* 
  - `club`: *Patient club* 
  - `OTHER`: *Other (specify below)* 
---

**12.1.** If other, please specify ...
- db_table: inte_subject_integratedcarereview
- column: where_rx_dispensed_other
- type: CharField
- length: 35
- responses: *free text*
---

**13.0.** If YES, who in this healthcare facility is responsible for dispensing your drugs?
- db_table: inte_subject_integratedcarereview
- column: who_dispenses_rx
- type: ManyToManyField
- responses: *Select all that apply*
  - `pharmacist`: *Pharmacist* 
  - `doctor`: *Doctor* 
  - `nurse`: *Nurse* 
  - `OTHER`: *Other (specify below)* 
---

**13.1.** If other, please specify ...
- db_table: inte_subject_integratedcarereview
- column: who_dispenses_rx_other
- type: CharField
- length: 35
- responses: *free text*
---

**Section: Part 3: Managing Clinic Records and Appointments**

**14.0.** Do you have a hospital record stored in the clinic?
- db_table: inte_subject_integratedcarereview
- column: hospital_card
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `Dont_know`: *Do not know* 
---

**15.0.** If YES, what type of hospital record is this?
- db_table: inte_subject_integratedcarereview
- column: hospital_card_type
- type: CharField
- length: 15
- responses:
  - `paper_based`: *Paper-based* 
  - `electronic`: *Electronic* 
  - `both`: *Both* 
  - `N/A`: *Not Applicable* 
---

**16.0.** Have you missed an appointment since attending this clinic?
- db_table: inte_subject_integratedcarereview
- column: missed_appt
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**17.0.** If YES, did you get a phone call from the clinic about the missed appointment?
- db_table: inte_subject_integratedcarereview
- column: missed_appt_call
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**18.0.** If YES, who called you about the missed appointment?
- db_table: inte_subject_integratedcarereview
- column: missed_appt_call_who
- type: CharField
- length: 15
- responses:
  - `nurse`: *Nurse* 
  - `OTHER`: *Other* 
  - `N/A`: *Not applicable* 
---

**18.1.** If other, please specify ...
- db_table: inte_subject_integratedcarereview
- column: missed_appt_call_who_other
- type: CharField
- length: 35
- responses: *free text*
---

**Section: Part 4: Laboratory Services**

**19.0.** Have you done any laboratory tests since you started in this clinic?
- db_table: inte_subject_integratedcarereview
- column: lab_tests
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**20.0.** If YES, did you pay for any of these tests?
- db_table: inte_subject_integratedcarereview
- column: pay_for_lab_tests
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**21.0.** If YES, which tests were you charged for?
- db_table: inte_subject_integratedcarereview
- column: which_lab_tests_charged_for
- type: ManyToManyField
- responses: *Select all that apply*
  - `blood_pressure_checks`: *Blood pressure checks* 
  - `blood_sugar_checks`: *Blood sugar checks* 
  - `viral_load_checks`: *Viral load checks* 
  - `OTHER`: *Other test (specify below)* 
---

**21.1.** If other, please specify ...
- db_table: inte_subject_integratedcarereview
- column: which_lab_tests_charged_for_other
- type: CharField
- length: 35
- responses: *free text*
---

**Section: CRF status**

**22.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_integratedcarereview
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**23.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_integratedcarereview
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Routine Appointment
*[missing model class docstring]*


*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_nextappointment
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_nextappointment
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: HIV**

**3.0.** HIV clinic: next scheduled routine appointment

&nbsp;&nbsp;&nbsp;&nbsp; *if applicable.*
- db_table: inte_subject_nextappointment
- column: hiv_clinic_appt_date
- type: DateField
- format: YYYY-MM-DD
---

**Section: NCD (Joint Diabetes/Hypertension)**

**4.0.** NCD clinic: next scheduled routine appointment

&nbsp;&nbsp;&nbsp;&nbsp; *if applicable.*
- db_table: inte_subject_nextappointment
- column: ncd_clinic_appt_date
- type: DateField
- format: YYYY-MM-DD
---

**Section: Diabetes-only**

**5.0.** Diabetes-only clinic: next scheduled routine appointment

&nbsp;&nbsp;&nbsp;&nbsp; *if applicable.*
- db_table: inte_subject_nextappointment
- column: dm_clinic_appt_date
- type: DateField
- format: YYYY-MM-DD
---

**Section: Hypertension-only**

**6.0.** Hypertension-only clinic: next scheduled routine appointment

&nbsp;&nbsp;&nbsp;&nbsp; *if applicable.*
- db_table: inte_subject_nextappointment
- column: htn_clinic_appt_date
- type: DateField
- format: YYYY-MM-DD
---

**Section: Integrated Clinic**

**7.0.** Integrated clinic: next scheduled routine appointment

&nbsp;&nbsp;&nbsp;&nbsp; *if applicable.*
- db_table: inte_subject_nextappointment
- column: integrated_clinic_appt_date
- type: DateField
- format: YYYY-MM-DD
---

**Section: CRF status**

**8.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_nextappointment
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**9.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_nextappointment
- column: crf_status_comments
- type: TextField
---


#### Requisitions

### 1120



*Rendered on 2022-05-06 16:14*

#### Clinical Review
*[missing model class docstring]*


*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_clinicalreview
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_clinicalreview
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: HYPERTENSION**

**3.0.** Since last seen, was the patient tested for hypertension?

&nbsp;&nbsp;&nbsp;&nbsp; *Note: Select `not applicable` if diagnosis previously reported. <BR>`Since last seen` includes today.<BR>If `yes', complete the initial review CRF<BR>If `not applicable`, complete the review CRF.*
- db_table: inte_subject_clinicalreview
- column: htn_test
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**4.0.** Date test requested
- db_table: inte_subject_clinicalreview
- column: htn_test_date
- type: DateField
- format: YYYY-MM-DD
---

**5.0.** Why was the patient tested for hypertension?
- db_table: inte_subject_clinicalreview
- column: htn_reason
- type: ManyToManyField
- responses: *Select all that apply*
  - `patient_request`: *Patient was well and made a request* 
  - `patient_complication`: *Patient had a clinical complication* 
  - `signs_symptoms`: *Patient had suggestive signs and symptoms* 
  - `OTHER`: *Other reason (specify below)* 
---

**5.1.** If other, please specify ...
- db_table: inte_subject_clinicalreview
- column: htn_reason_other
- type: CharField
- length: 35
- responses: *free text*
---

**6.0.** As of today, was the patient <u>newly</u> diagnosed with hypertension?
- db_table: inte_subject_clinicalreview
- column: htn_dx
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**Section: DIABETES**

**7.0.** Since last seen, was the patient tested for diabetes?

&nbsp;&nbsp;&nbsp;&nbsp; *Note: Select `not applicable` if diagnosis previously reported. <BR>`Since last seen` includes today.<BR>If `yes', complete the initial review CRF<BR>If `not applicable`, complete the review CRF.*
- db_table: inte_subject_clinicalreview
- column: dm_test
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**8.0.** Date test requested
- db_table: inte_subject_clinicalreview
- column: dm_test_date
- type: DateField
- format: YYYY-MM-DD
---

**9.0.** Why was the patient tested for diabetes?
- db_table: inte_subject_clinicalreview
- column: dm_reason
- type: ManyToManyField
- responses: *Select all that apply*
  - `patient_request`: *Patient was well and made a request* 
  - `patient_complication`: *Patient had a clinical complication* 
  - `signs_symptoms`: *Patient had suggestive signs and symptoms* 
  - `OTHER`: *Other reason (specify below)* 
---

**9.1.** If other, please specify ...
- db_table: inte_subject_clinicalreview
- column: dm_reason_other
- type: CharField
- length: 35
- responses: *free text*
---

**10.0.** As of today, was the patient <u>newly</u> diagnosed with diabetes?
- db_table: inte_subject_clinicalreview
- column: dm_dx
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**Section: HIV**

**11.0.** Since last seen, was the patient tested for HIV infection?

&nbsp;&nbsp;&nbsp;&nbsp; *Note: Select `not applicable` if diagnosis previously reported. <BR>`Since last seen` includes today.<BR>If `yes', complete the initial review CRF<BR>If `not applicable`, complete the review CRF.*
- db_table: inte_subject_clinicalreview
- column: hiv_test
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**12.0.** Date test requested
- db_table: inte_subject_clinicalreview
- column: hiv_test_date
- type: DateField
- format: YYYY-MM-DD
---

**13.0.** Why was the patient tested for HIV infection?
- db_table: inte_subject_clinicalreview
- column: hiv_reason
- type: ManyToManyField
- responses: *Select all that apply*
  - `patient_request`: *Patient was well and made a request* 
  - `patient_complication`: *Patient had a clinical complication* 
  - `signs_symptoms`: *Patient had suggestive signs and symptoms* 
  - `OTHER`: *Other reason (specify below)* 
---

**13.1.** If other, please specify ...
- db_table: inte_subject_clinicalreview
- column: hiv_reason_other
- type: CharField
- length: 35
- responses: *free text*
---

**14.0.** As of today, was the patient <u>newly</u> diagnosed with HIV infection?
- db_table: inte_subject_clinicalreview
- column: hiv_dx
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**Section: Complications**

**15.0.** Since last seen, has the patient had any complications

&nbsp;&nbsp;&nbsp;&nbsp; *If Yes, complete the `Complications` CRF*
- db_table: inte_subject_clinicalreview
- column: complications
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**Section: Other**

**16.0.** Does the patient have any private or work-place health insurance?
- db_table: inte_subject_clinicalreview
- column: health_insurance
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**17.0.** In the last month, how much has the patient spent on health insurance

&nbsp;&nbsp;&nbsp;&nbsp; *amount in local currency*
- db_table: inte_subject_clinicalreview
- column: health_insurance_monthly_pay
- type: IntegerField
---

**18.0.** Does the patient belong to a ‘club’ that supports medicines purchase?
- db_table: inte_subject_clinicalreview
- column: patient_club
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**19.0.** In the last month, how much has the patient spent on club membership

&nbsp;&nbsp;&nbsp;&nbsp; *amount in local currency*
- db_table: inte_subject_clinicalreview
- column: patient_club_monthly_pay
- type: IntegerField
---

**Section: CRF status**

**20.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_clinicalreview
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**21.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_clinicalreview
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Hiv Initial Review
*[missing model class docstring]*


*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_hivinitialreview
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_hivinitialreview
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: Diagnosis and Care**

**3.0.** How long ago was the patient diagnosed?

&nbsp;&nbsp;&nbsp;&nbsp; *If possible, provide the exact date below instead of estimating here. Format is `YYyMMm` or `DDd`. For example 3y10m, 12y7m ... or 7d, 0d ...*
- db_table: inte_subject_hivinitialreview
- column: dx_ago
- type: CharField
- length: 8
- responses: *free text*
---

**4.0.** Date patient diagnosed

&nbsp;&nbsp;&nbsp;&nbsp; *If possible, provide the exact date here instead of estimating above.*
- db_table: inte_subject_hivinitialreview
- column: dx_date
- type: DateField
- format: YYYY-MM-DD
---

**5.0.** Is the patient receiving care for HIV?
- db_table: inte_subject_hivinitialreview
- column: receives_care
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**6.0.** Where does the patient receive care for HIV
- db_table: inte_subject_hivinitialreview
- column: clinic
- type: CharField
- length: 15
- responses:
  - `this_clinic`: *Patient comes to this facility for their care* 
  - `OTHER`: *Patient goes to a different clinic* 
  - `N/A`: *Not applicable* 
---

**6.1.** If <u>not</u> attending here, where does the patient attend?
- db_table: inte_subject_hivinitialreview
- column: clinic_other
- type: CharField
- length: 50
- responses: *free text*
---

**Section: Monitoring and Treatment**

**7.0.** Has the patient started antiretroviral therapy (ART)?
- db_table: inte_subject_hivinitialreview
- column: arv_initiated
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**8.0.** How long ago did the patient start ART?

&nbsp;&nbsp;&nbsp;&nbsp; *If possible, provide the exact date below instead of estimating here. Format is `YYyMMm` or `DDd`. For example 3y10m, 12y7m ... or 7d, 0d ...*
- db_table: inte_subject_hivinitialreview
- column: arv_initiation_ago
- type: CharField
- length: 8
- responses: *free text*
---

**9.0.** Date started antiretroviral therapy (ART)

&nbsp;&nbsp;&nbsp;&nbsp; *If possible, provide the exact date here instead of estimating above.*
- db_table: inte_subject_hivinitialreview
- column: arv_initiation_actual_date
- type: DateField
- format: YYYY-MM-DD
---

**10.0.** Is the patient's most recent viral load result available?
- db_table: inte_subject_hivinitialreview
- column: has_vl
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `PENDING`: *Pending* 
  - `N/A`: *Not applicable* 
---

**11.0.** Most recent viral load

&nbsp;&nbsp;&nbsp;&nbsp; *copies/mL*
- db_table: inte_subject_hivinitialreview
- column: vl
- type: IntegerField
---

**12.0.** vl quantifier
- db_table: inte_subject_hivinitialreview
- column: vl_quantifier
- type: CharField
- length: 10
- responses:
  - `=`: *=* 
  - `>`: *>* 
  - `<`: *<* 
---

**13.0.** Date of most recent viral load
- db_table: inte_subject_hivinitialreview
- column: vl_date
- type: DateField
- format: YYYY-MM-DD
---

**14.0.** Is the patient's most recent CD4 result available?
- db_table: inte_subject_hivinitialreview
- column: has_cd4
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**15.0.** Most recent CD4

&nbsp;&nbsp;&nbsp;&nbsp; *cells/mm<sup>3</sup>*
- db_table: inte_subject_hivinitialreview
- column: cd4
- type: IntegerField
---

**16.0.** Date of most recent CD4
- db_table: inte_subject_hivinitialreview
- column: cd4_date
- type: DateField
- format: YYYY-MM-DD
---

**Section: CRF status**

**17.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_hivinitialreview
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**18.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_hivinitialreview
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Diabetes Initial Review
*[missing model class docstring]*


*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_dminitialreview
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_dminitialreview
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: Diagnosis and Treatment**

**3.0.** How long ago was the patient diagnosed?

&nbsp;&nbsp;&nbsp;&nbsp; *If possible, provide the exact date below instead of estimating here. Format is `YYyMMm` or `DDd`. For example 3y10m, 12y7m ... or 7d, 0d ...*
- db_table: inte_subject_dminitialreview
- column: dx_ago
- type: CharField
- length: 8
- responses: *free text*
---

**4.0.** Date patient diagnosed

&nbsp;&nbsp;&nbsp;&nbsp; *If possible, provide the exact date here instead of estimating above.*
- db_table: inte_subject_dminitialreview
- column: dx_date
- type: DateField
- format: YYYY-MM-DD
---

**5.0.** How is the patient's diabetes managed?
- db_table: inte_subject_dminitialreview
- column: managed_by
- type: CharField
- length: 25
- responses:
  - `insulin`: *Insulin injections* 
  - `drugs`: *Oral drugs* 
  - `diet_lifestyle`: *Diet and lifestyle alone* 
---

**6.0.** If the patient is taking medicines for diabetes, how long have they been taking these?

&nbsp;&nbsp;&nbsp;&nbsp; * Format is `YYyMMm` or `DDd`. For example 3y10m, 12y7m ... or 7d, 0d ...*
- db_table: inte_subject_dminitialreview
- column: med_start_ago
- type: CharField
- length: 8
- responses: *free text*
---

**Section: Blood Sugar Measurement**

**7.0.** Has the patient had their glucose measured in the last few months?
- db_table: inte_subject_dminitialreview
- column: glucose_performed
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**8.0.** Had the participant fasted?
- db_table: inte_subject_dminitialreview
- column: glucose_fasted
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**9.0.** glucose date
- db_table: inte_subject_dminitialreview
- column: glucose_date
- type: DateField
- format: YYYY-MM-DD
---

**10.0.** Glucose result
- db_table: inte_subject_dminitialreview
- column: glucose
- type: DecimalField
---

**11.0.** glucose quantifier
- db_table: inte_subject_dminitialreview
- column: glucose_quantifier
- type: CharField
- length: 10
- responses:
  - `N/A`: ** 
  - `=`: *=* 
  - `>`: *>* 
  - `>=`: *>=* 
  - `<`: *<* 
  - `<=`: *<=* 
---

**12.0.** Units (glucose)
- db_table: inte_subject_dminitialreview
- column: glucose_units
- type: CharField
- length: 15
- responses:
  - `mg/dL`: *mg/dL* 
  - `mmol/L`: *mmol/L (millimoles/L)* 
  - `N/A`: *Not applicable* 
---

**Section: CRF status**

**13.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_dminitialreview
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**14.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_dminitialreview
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Indicators
*[missing model class docstring]*


*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_indicators
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_indicators
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: Weight and Height**

**3.0.** Weight:

&nbsp;&nbsp;&nbsp;&nbsp; *in kg*
- db_table: inte_subject_indicators
- column: weight
- type: DecimalField
---

**4.0.** Height:

&nbsp;&nbsp;&nbsp;&nbsp; *in centimeters*
- db_table: inte_subject_indicators
- column: height
- type: DecimalField
---

**Section: Blood Pressure: Reading 1**

**5.0.** Was a blood pressure reading taken
- db_table: inte_subject_indicators
- column: r1_taken
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**6.0.** reason not taken
- db_table: inte_subject_indicators
- column: r1_reason_not_taken
- type: TextField
- length: 250
---

**7.0.** Blood pressure: systolic

&nbsp;&nbsp;&nbsp;&nbsp; *in mm. format SYS, e.g. 120*
- db_table: inte_subject_indicators
- column: sys_blood_pressure_r1
- type: IntegerField
---

**8.0.** Blood pressure: diastolic

&nbsp;&nbsp;&nbsp;&nbsp; *in Hg. format DIA, e.g. 80*
- db_table: inte_subject_indicators
- column: dia_blood_pressure_r1
- type: IntegerField
---

**Section: Blood Pressure: Reading 2**

**9.0.** Was a <u>second</u> blood pressure reading taken
- db_table: inte_subject_indicators
- column: r2_taken
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `not_required`: *Not required* 
---

**10.0.** r2 reason not taken
- db_table: inte_subject_indicators
- column: r2_reason_not_taken
- type: TextField
- length: 250
---

**11.0.** Blood pressure: systolic

&nbsp;&nbsp;&nbsp;&nbsp; *in mm. format SYS, e.g. 120*
- db_table: inte_subject_indicators
- column: sys_blood_pressure_r2
- type: IntegerField
---

**12.0.** Blood pressure: diastolic

&nbsp;&nbsp;&nbsp;&nbsp; *in Hg. format DIA, e.g. 80*
- db_table: inte_subject_indicators
- column: dia_blood_pressure_r2
- type: IntegerField
---

**Section: CRF status**

**13.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_indicators
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**14.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_indicators
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Hypertension Initial Review
*[missing model class docstring]*


*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_htninitialreview
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_htninitialreview
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: Diagnosis and Treatment**

**3.0.** How long ago was the patient diagnosed?

&nbsp;&nbsp;&nbsp;&nbsp; *If possible, provide the exact date below instead of estimating here. Format is `YYyMMm` or `DDd`. For example 3y10m, 12y7m ... or 7d, 0d ...*
- db_table: inte_subject_htninitialreview
- column: dx_ago
- type: CharField
- length: 8
- responses: *free text*
---

**4.0.** Date patient diagnosed

&nbsp;&nbsp;&nbsp;&nbsp; *If possible, provide the exact date here instead of estimating above.*
- db_table: inte_subject_htninitialreview
- column: dx_date
- type: DateField
- format: YYYY-MM-DD
---

**5.0.** How is the patient's hypertension managed?
- db_table: inte_subject_htninitialreview
- column: managed_by
- type: CharField
- length: 15
- responses:
  - `drugs`: *Drugs / Medicine* 
  - `diet_lifestyle`: *Diet and lifestyle alone* 
---

**6.0.** If the patient is taking medicines for hypertension, how long have they been taking these?

&nbsp;&nbsp;&nbsp;&nbsp; * Format is `YYyMMm` or `DDd`. For example 3y10m, 12y7m ... or 7d, 0d ...*
- db_table: inte_subject_htninitialreview
- column: med_start_ago
- type: CharField
- length: 8
- responses: *free text*
---

**Section: CRF status**

**7.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_htninitialreview
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**8.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_htninitialreview
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Hiv Review
*[missing model class docstring]*


*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_hivreview
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_hivreview
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: Care**

**3.0.** Was care for this `condition` delivered in an integrated care clinic today?

&nbsp;&nbsp;&nbsp;&nbsp; *Select `not applicable` if site was not selected for integrated care.*
- db_table: inte_subject_hivreview
- column: care_delivery
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**3.1.** If no, please explain
- db_table: inte_subject_hivreview
- column: care_delivery_other
- type: TextField
---

**Section: Anit-retroviral therapy (ART)**

**4.0.** Has the patient started antiretroviral therapy (ART)?

&nbsp;&nbsp;&nbsp;&nbsp; *Select `not applicable` if previously reported.*
- db_table: inte_subject_hivreview
- column: arv_initiated
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**5.0.** Date started antiretroviral therapy (ART)
- db_table: inte_subject_hivreview
- column: arv_initiation_actual_date
- type: DateField
- format: YYYY-MM-DD
---

**Section: CRF status**

**6.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_hivreview
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**7.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_hivreview
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Diabetes Review
*[missing model class docstring]*


*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_dmreview
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_dmreview
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: Care**

**3.0.** How will the patient's diabetes be managed going forward?
- db_table: inte_subject_dmreview
- column: managed_by
- type: CharField
- length: 25
- responses:
  - `insulin`: *Insulin injections* 
  - `drugs`: *Oral drugs* 
  - `diet_lifestyle`: *Diet and lifestyle alone* 
---

**4.0.** Was care for this `condition` delivered in an integrated care clinic today?

&nbsp;&nbsp;&nbsp;&nbsp; *Select `not applicable` if site was not selected for integrated care.*
- db_table: inte_subject_dmreview
- column: care_delivery
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**4.1.** If no, please explain
- db_table: inte_subject_dmreview
- column: care_delivery_other
- type: TextField
---

**Section: Blood Sugar Measurement**

**5.0.** Had the participant fasted?
- db_table: inte_subject_dmreview
- column: glucose_fasted
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**6.0.** glucose date
- db_table: inte_subject_dmreview
- column: glucose_date
- type: DateField
- format: YYYY-MM-DD
---

**7.0.** Glucose result
- db_table: inte_subject_dmreview
- column: glucose
- type: DecimalField
---

**8.0.** glucose quantifier
- db_table: inte_subject_dmreview
- column: glucose_quantifier
- type: CharField
- length: 10
- responses:
  - `N/A`: ** 
  - `=`: *=* 
  - `>`: *>* 
  - `>=`: *>=* 
  - `<`: *<* 
  - `<=`: *<=* 
---

**9.0.** Units (glucose)
- db_table: inte_subject_dmreview
- column: glucose_units
- type: CharField
- length: 15
- responses:
  - `mg/dL`: *mg/dL* 
  - `mmol/L`: *mmol/L (millimoles/L)* 
  - `N/A`: *Not applicable* 
---

**Section: CRF status**

**10.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_dmreview
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**11.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_dmreview
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Hypertension Review
*[missing model class docstring]*


*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_htnreview
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_htnreview
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: Care**

**3.0.** How will the patient's hypertension be managed going forward?
- db_table: inte_subject_htnreview
- column: managed_by
- type: CharField
- length: 25
- responses:
  - `drugs`: *Drugs / Medicine* 
  - `diet_lifestyle`: *Diet and lifestyle alone* 
---

**4.0.** Was care for this `condition` delivered in an integrated care clinic today?

&nbsp;&nbsp;&nbsp;&nbsp; *Select `not applicable` if site was not selected for integrated care.*
- db_table: inte_subject_htnreview
- column: care_delivery
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**4.1.** If no, please explain
- db_table: inte_subject_htnreview
- column: care_delivery_other
- type: TextField
---

**Section: Blood Pressure Measurement**

**5.0.** Blood pressure: systolic

&nbsp;&nbsp;&nbsp;&nbsp; *in mm. format SYS, e.g. 120*
- db_table: inte_subject_htnreview
- column: sys_blood_pressure
- type: IntegerField
---

**6.0.** Blood pressure: diastolic

&nbsp;&nbsp;&nbsp;&nbsp; *in Hg. format DIA, e.g. 80*
- db_table: inte_subject_htnreview
- column: dia_blood_pressure
- type: IntegerField
---

**Section: CRF status**

**7.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_htnreview
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**8.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_htnreview
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Medications
*[missing model class docstring]*


*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_medications
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_medications
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: Prescriptions**

**3.0.** Is the patient filling / refilling Hypertension medications?

&nbsp;&nbsp;&nbsp;&nbsp; *Select `not applicable` if subject has not been diagnosed and prescribed medication for Hypertension.*
- db_table: inte_subject_medications
- column: refill_htn
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**4.0.** Is the patient filling / refilling Diabetes medications?

&nbsp;&nbsp;&nbsp;&nbsp; *Select `not applicable` if subject has not been diagnosed and prescribed medication for Diabetes.*
- db_table: inte_subject_medications
- column: refill_dm
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**5.0.** Is the patient filling / refilling HIV medications?

&nbsp;&nbsp;&nbsp;&nbsp; *Select `not applicable` if subject has not been diagnosed and prescribed medication for HIV infection.*
- db_table: inte_subject_medications
- column: refill_hiv
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**Section: CRF status**

**6.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_medications
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**7.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_medications
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Drug Refill: Hypertension
*[missing model class docstring]*


*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.

*Additional instructions*: <span style="color:orange">Note: Medications CRF must be completed first.</span>


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_drugrefillhtn
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_drugrefillhtn
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: Hypertension Drug Refill Today**

**3.0.** Which medicine did the patient receive today?
- db_table: inte_subject_drugrefillhtn
- column: rx
- type: ManyToManyField
- responses: *Select all that apply*
  - `aldactone`: *Aldactone (Spironolactone)* 
  - `amlodipine`: *Amlodipine* 
  - `atenolol`: *Atenolol* 
  - `atorvastatin`: *Atorvastatin* 
  - `bendroflumethiazide`: *Bendroflumethiazide* 
  - `bisoprolol`: *Bisoprolol* 
  - `candesartan`: *Candesartan* 
  - `captopril`: *Captopril* 
  - `carvedilol`: *Carvedilol* 
  - `clopidogrel`: *Clopidogrel* 
  - `enalapril`: *Enalapril* 
  - `frusemide`: *Frusemide* 
  - `hydralazine`: *Hydralazine* 
  - `hydrochlorothiazide`: *Hydrochlorothiazide* 
  - `irbesartan`: *Irbesartan* 
  - `irbesartan_hydrochlorothiazide`: *Irbesartan Hydrochlorothiazide* 
  - `junior_aspirin`: *Junior Aspirin* 
  - `lisinopril`: *Lisinopril* 
  - `losartan_h`: *losartan Hydrochlorothiazide (Losartan H/Repace H)* 
  - `losartan`: *losartan* 
  - `methyldopa`: *Methyldopa* 
  - `metoprolol`: *Metoprolol* 
  - `nifedipine`: *Nifedipine* 
  - `olmesartan`: *Olmesartan* 
  - `propanolol`: *Propanolol* 
  - `ramipril`: *Ramipril* 
  - `rosuvastatin`: *Rosuvastatin* 
  - `s-amlodipine`: *S-Amlodipine* 
  - `simvastatin`: *Simvastatin* 
  - `telmisartan`: *Telmisartan* 
  - `valsartan`: *Valsartan* 
  - `vitamin_b_folic_acid`: *Vitamin Bs + Folic Acid* 
  - `OTHER`: *Other treatment (specify below)* 
---

**3.1.** If other, please specify ...
- db_table: inte_subject_drugrefillhtn
- column: rx_other
- type: CharField
- length: 150
- responses: *free text*
---

**4.0.** Was the patient’s prescription changed at this visit compared with their prescription at the previous visit?
- db_table: inte_subject_drugrefillhtn
- column: rx_modified
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**5.0.** Which changes occurred?
- db_table: inte_subject_drugrefillhtn
- column: modifications
- type: ManyToManyField
- responses: *Select all that apply*
  - `dose_changes`: *Dose changes* 
  - `drugs_substitution`: *Drugs substitution* 
  - `drug_additions`: *Additional drugs added to existing regimen* 
  - `some_stopped`: *Some drugs stopped* 
  - `OTHER`: *Other, specify* 
---

**5.1.** If other, please specify ...
- db_table: inte_subject_drugrefillhtn
- column: modifications_other
- type: CharField
- length: 150
- responses: *free text*
---

**6.0.** Why did the patient’s previous prescription change?
- db_table: inte_subject_drugrefillhtn
- column: modifications_reason
- type: ManyToManyField
- responses: *Select all that apply*
  - `availability`: *Limited availability of drugs* 
  - `side_effects`: *Had side-effects* 
  - `feel_better`: *Felt well and stopped/reduced drug prescription* 
  - `OTHER`: *Other, specify* 
---

**6.1.** If other, please specify ...
- db_table: inte_subject_drugrefillhtn
- column: modifications_reason_other
- type: CharField
- length: 150
- responses: *free text*
---

**7.0.** In how many days has the patient been asked to return to clinic for a drug refill?
- db_table: inte_subject_drugrefillhtn
- column: return_in_days
- type: IntegerField
---

**Section: CRF status**

**8.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_drugrefillhtn
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**9.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_drugrefillhtn
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Drug Refill: Diabetes
*[missing model class docstring]*


*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.

*Additional instructions*: <span style="color:orange">Note: Medications CRF must be completed first.</span>


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_drugrefilldm
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_drugrefilldm
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: Diabetes Drug Refill Today**

**3.0.** Which medicine did the patient receive today?
- db_table: inte_subject_drugrefilldm
- column: rx
- type: ManyToManyField
- responses: *Select all that apply*
  - `glibenclamide_metformin`: *Glibenclamide + Metformin combo* 
  - `glibenclamide_s`: *Glibenclamide (S)* 
  - `gliclazide_s`: *Gliclazide (S)* 
  - `glimepiride_1mg_metformin`: *Glimepiride (1mg) + Metformin combo* 
  - `glimepiride_2mg_metformin`: *Glimepiride (2mg) + Metformin combo* 
  - `glimepiride_s`: *Glimepiride (S)* 
  - `glipizide_s`: *Glipizide (S)* 
  - `insulin`: *Insulin* 
  - `metformin_b`: *Metformin (B)* 
  - `pioglitazone`: *Pioglitazone* 
  - `pregabalin`: *Pregabalin (diabetic neuropathy)* 
  - `vitamin_b_folic_acid`: *Vitamin Bs + Folic Acid (Neuroton- diabetic neuropathy)* 
  - `OTHER`: *Other, specify* 
---

**3.1.** If other, please specify ...
- db_table: inte_subject_drugrefilldm
- column: rx_other
- type: CharField
- length: 150
- responses: *free text*
---

**4.0.** Was the patient’s prescription changed at this visit compared with their prescription at the previous visit?
- db_table: inte_subject_drugrefilldm
- column: rx_modified
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**5.0.** Which changes occurred?
- db_table: inte_subject_drugrefilldm
- column: modifications
- type: ManyToManyField
- responses: *Select all that apply*
  - `dose_changes`: *Dose changes* 
  - `drugs_substitution`: *Drugs substitution* 
  - `drug_additions`: *Additional drugs added to existing regimen* 
  - `some_stopped`: *Some drugs stopped* 
  - `OTHER`: *Other, specify* 
---

**5.1.** If other, please specify ...
- db_table: inte_subject_drugrefilldm
- column: modifications_other
- type: CharField
- length: 150
- responses: *free text*
---

**6.0.** Why did the patient’s previous prescription change?
- db_table: inte_subject_drugrefilldm
- column: modifications_reason
- type: ManyToManyField
- responses: *Select all that apply*
  - `availability`: *Limited availability of drugs* 
  - `side_effects`: *Had side-effects* 
  - `feel_better`: *Felt well and stopped/reduced drug prescription* 
  - `OTHER`: *Other, specify* 
---

**6.1.** If other, please specify ...
- db_table: inte_subject_drugrefilldm
- column: modifications_reason_other
- type: CharField
- length: 150
- responses: *free text*
---

**7.0.** In how many days has the patient been asked to return to clinic for a drug refill?
- db_table: inte_subject_drugrefilldm
- column: return_in_days
- type: IntegerField
---

**Section: CRF status**

**8.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_drugrefilldm
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**9.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_drugrefilldm
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Drug Refill: Hiv
*[missing model class docstring]*


*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.

*Additional instructions*: <span style="color:orange">Note: Medications CRF must be completed first.</span>


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_drugrefillhiv
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_drugrefillhiv
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: ART Drug Refill Today**

**3.0.** Which medicine did the patient receive today?
- db_table: inte_subject_drugrefillhiv
- column: rx
- type: ForeignKey
---

**3.1.** If other, please specify ...
- db_table: inte_subject_drugrefillhiv
- column: rx_other
- type: CharField
- length: 150
- responses: *free text*
---

**4.0.** Was the patient’s prescription changed at this visit compared with their prescription at the previous visit?
- db_table: inte_subject_drugrefillhiv
- column: rx_modified
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**5.0.** Which changes occurred?
- db_table: inte_subject_drugrefillhiv
- column: modifications
- type: ManyToManyField
- responses: *Select all that apply*
  - `dose_changes`: *Dose changes* 
  - `drugs_substitution`: *Drugs substitution* 
  - `drug_additions`: *Additional drugs added to existing regimen* 
  - `some_stopped`: *Some drugs stopped* 
  - `OTHER`: *Other, specify* 
---

**5.1.** If other, please specify ...
- db_table: inte_subject_drugrefillhiv
- column: modifications_other
- type: CharField
- length: 150
- responses: *free text*
---

**6.0.** Why did the patient’s previous prescription change?
- db_table: inte_subject_drugrefillhiv
- column: modifications_reason
- type: ManyToManyField
- responses: *Select all that apply*
  - `availability`: *Limited availability of drugs* 
  - `side_effects`: *Had side-effects* 
  - `feel_better`: *Felt well and stopped/reduced drug prescription* 
  - `OTHER`: *Other, specify* 
---

**6.1.** If other, please specify ...
- db_table: inte_subject_drugrefillhiv
- column: modifications_reason_other
- type: CharField
- length: 150
- responses: *free text*
---

**Section: Supply**

**7.0.** In how many days has the patient been asked to return to clinic for a drug refill?
- db_table: inte_subject_drugrefillhiv
- column: return_in_days
- type: IntegerField
---

**8.0.** How many days supplied by the clinic

&nbsp;&nbsp;&nbsp;&nbsp; *days*
- db_table: inte_subject_drugrefillhiv
- column: clinic_days
- type: IntegerField
---

**9.0.** How many days supplied by a club

&nbsp;&nbsp;&nbsp;&nbsp; *days*
- db_table: inte_subject_drugrefillhiv
- column: club_days
- type: IntegerField
---

**10.0.** How many days supplied by to be purchased

&nbsp;&nbsp;&nbsp;&nbsp; *This can be purchased by patient, through a medicines club that the patient belong to, through insurance or someone else has paid. *
- db_table: inte_subject_drugrefillhiv
- column: purchased_days
- type: IntegerField
---

**Section: CRF status**

**11.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_drugrefillhiv
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**12.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_drugrefillhiv
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Hiv Medication Adherence
*[missing model class docstring]*


*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_hivmedicationadherence
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_hivmedicationadherence
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: Visual Score**

**3.0.** Visual adherence score for <U>condition_label</U> medication

&nbsp;&nbsp;&nbsp;&nbsp; *%*
- db_table: inte_subject_hivmedicationadherence
- column: visual_score_slider
- type: CharField
- length: 3
- responses: *free text*
---

**4.0.** <B><font color='orange'>Interviewer</font></B>: please confirm the score indicated from above.

&nbsp;&nbsp;&nbsp;&nbsp; *%*
- db_table: inte_subject_hivmedicationadherence
- column: visual_score_confirmed
- type: IntegerField
---

**Section: Missed Medications**

**5.0.** When was the last time you missed taking your <U>condition_label</U> medication?
- db_table: inte_subject_hivmedicationadherence
- column: last_missed_pill
- type: CharField
- length: 25
- responses:
  - `today`: *today* 
  - `yesterday`: *yesterday* 
  - `earlier_this_week`: *earlier this week* 
  - `last_week`: *last week* 
  - `lt_month_ago`: *less than a month ago* 
  - `gt_month_ago`: *more than a month ago* 
  - `NEVER`: *have never missed taking my study pills* 
---

**6.0.** Reasons for miss taking medication
- db_table: inte_subject_hivmedicationadherence
- column: missed_pill_reason
- type: ManyToManyField
- responses: *Select all that apply*
  - `forgot_to_take`: *I simply forgot to take my medication* 
  - `travelled`: *I travelled and forgot my medication* 
  - `feel_better`: *I felt better and stopped taking my medication* 
  - `insufficient_supply`: *I did not get enough medication from hospital/clinic, could not buy more* 
  - `feel_ill`: *The medications were making me feel sick* 
  - `too_many_pills`: *Too many pills so I stopped / reduced* 
  - `OTHER`: *Other, please specify ...* 
---

**7.0.** If other, please specify ...
- db_table: inte_subject_hivmedicationadherence
- column: other_missed_pill_reason
- type: CharField
- length: 35
- responses: *free text*
---

**Section: CRF status**

**8.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_hivmedicationadherence
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**9.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_hivmedicationadherence
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Diabetes Medication Adherence
*[missing model class docstring]*


*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_dmmedicationadherence
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_dmmedicationadherence
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: Visual Score**

**3.0.** Visual adherence score for <U>condition_label</U> medication

&nbsp;&nbsp;&nbsp;&nbsp; *%*
- db_table: inte_subject_dmmedicationadherence
- column: visual_score_slider
- type: CharField
- length: 3
- responses: *free text*
---

**4.0.** <B><font color='orange'>Interviewer</font></B>: please confirm the score indicated from above.

&nbsp;&nbsp;&nbsp;&nbsp; *%*
- db_table: inte_subject_dmmedicationadherence
- column: visual_score_confirmed
- type: IntegerField
---

**Section: Missed Medications**

**5.0.** When was the last time you missed taking your <U>condition_label</U> medication?
- db_table: inte_subject_dmmedicationadherence
- column: last_missed_pill
- type: CharField
- length: 25
- responses:
  - `today`: *today* 
  - `yesterday`: *yesterday* 
  - `earlier_this_week`: *earlier this week* 
  - `last_week`: *last week* 
  - `lt_month_ago`: *less than a month ago* 
  - `gt_month_ago`: *more than a month ago* 
  - `NEVER`: *have never missed taking my study pills* 
---

**6.0.** Reasons for miss taking medication
- db_table: inte_subject_dmmedicationadherence
- column: missed_pill_reason
- type: ManyToManyField
- responses: *Select all that apply*
  - `forgot_to_take`: *I simply forgot to take my medication* 
  - `travelled`: *I travelled and forgot my medication* 
  - `feel_better`: *I felt better and stopped taking my medication* 
  - `insufficient_supply`: *I did not get enough medication from hospital/clinic, could not buy more* 
  - `feel_ill`: *The medications were making me feel sick* 
  - `too_many_pills`: *Too many pills so I stopped / reduced* 
  - `OTHER`: *Other, please specify ...* 
---

**7.0.** If other, please specify ...
- db_table: inte_subject_dmmedicationadherence
- column: other_missed_pill_reason
- type: CharField
- length: 35
- responses: *free text*
---

**Section: CRF status**

**8.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_dmmedicationadherence
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**9.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_dmmedicationadherence
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Hypertension Medication Adherence
*[missing model class docstring]*


*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_htnmedicationadherence
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_htnmedicationadherence
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: Visual Score**

**3.0.** Visual adherence score for <U>condition_label</U> medication

&nbsp;&nbsp;&nbsp;&nbsp; *%*
- db_table: inte_subject_htnmedicationadherence
- column: visual_score_slider
- type: CharField
- length: 3
- responses: *free text*
---

**4.0.** <B><font color='orange'>Interviewer</font></B>: please confirm the score indicated from above.

&nbsp;&nbsp;&nbsp;&nbsp; *%*
- db_table: inte_subject_htnmedicationadherence
- column: visual_score_confirmed
- type: IntegerField
---

**Section: Missed Medications**

**5.0.** When was the last time you missed taking your <U>condition_label</U> medication?
- db_table: inte_subject_htnmedicationadherence
- column: last_missed_pill
- type: CharField
- length: 25
- responses:
  - `today`: *today* 
  - `yesterday`: *yesterday* 
  - `earlier_this_week`: *earlier this week* 
  - `last_week`: *last week* 
  - `lt_month_ago`: *less than a month ago* 
  - `gt_month_ago`: *more than a month ago* 
  - `NEVER`: *have never missed taking my study pills* 
---

**6.0.** Reasons for miss taking medication
- db_table: inte_subject_htnmedicationadherence
- column: missed_pill_reason
- type: ManyToManyField
- responses: *Select all that apply*
  - `forgot_to_take`: *I simply forgot to take my medication* 
  - `travelled`: *I travelled and forgot my medication* 
  - `feel_better`: *I felt better and stopped taking my medication* 
  - `insufficient_supply`: *I did not get enough medication from hospital/clinic, could not buy more* 
  - `feel_ill`: *The medications were making me feel sick* 
  - `too_many_pills`: *Too many pills so I stopped / reduced* 
  - `OTHER`: *Other, please specify ...* 
---

**7.0.** If other, please specify ...
- db_table: inte_subject_htnmedicationadherence
- column: other_missed_pill_reason
- type: CharField
- length: 35
- responses: *free text*
---

**Section: CRF status**

**8.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_htnmedicationadherence
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**9.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_htnmedicationadherence
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Complications: Followup
*[missing model class docstring]*


*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_complicationsfollowup
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_complicationsfollowup
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: Complications**

**3.0.** Stroke
- db_table: inte_subject_complicationsfollowup
- column: stroke
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**4.0.** If yes, date

&nbsp;&nbsp;&nbsp;&nbsp; *If exact date not known, see SOP on how to estimate a date.*
- db_table: inte_subject_complicationsfollowup
- column: stroke_date
- type: DateField
- format: YYYY-MM-DD
---

**5.0.** Heart attack / heart failure
- db_table: inte_subject_complicationsfollowup
- column: heart_attack
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**6.0.** If yes, date

&nbsp;&nbsp;&nbsp;&nbsp; *If exact date not known, see SOP on how to estimate a date.*
- db_table: inte_subject_complicationsfollowup
- column: heart_attack_date
- type: DateField
- format: YYYY-MM-DD
---

**7.0.** Renal (kidney) disease
- db_table: inte_subject_complicationsfollowup
- column: renal_disease
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**8.0.** If yes, date

&nbsp;&nbsp;&nbsp;&nbsp; *If exact date not known, see SOP on how to estimate a date.*
- db_table: inte_subject_complicationsfollowup
- column: renal_disease_date
- type: DateField
- format: YYYY-MM-DD
---

**9.0.** Vision problems (e.g. blurred vision)
- db_table: inte_subject_complicationsfollowup
- column: vision
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**10.0.** If yes, date

&nbsp;&nbsp;&nbsp;&nbsp; *If exact date not known, see SOP on how to estimate a date.*
- db_table: inte_subject_complicationsfollowup
- column: vision_date
- type: DateField
- format: YYYY-MM-DD
---

**11.0.** Numbness / burning sensation
- db_table: inte_subject_complicationsfollowup
- column: numbness
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**12.0.** If yes, date

&nbsp;&nbsp;&nbsp;&nbsp; *If exact date not known, see SOP on how to estimate a date.*
- db_table: inte_subject_complicationsfollowup
- column: numbness_date
- type: DateField
- format: YYYY-MM-DD
---

**13.0.** Foot ulcers
- db_table: inte_subject_complicationsfollowup
- column: foot_ulcers
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**14.0.** If yes, date

&nbsp;&nbsp;&nbsp;&nbsp; *If exact date not known, see SOP on how to estimate a date.*
- db_table: inte_subject_complicationsfollowup
- column: foot_ulcers_date
- type: DateField
- format: YYYY-MM-DD
---

**15.0.** Are there any other major complications to report?
- db_table: inte_subject_complicationsfollowup
- column: complications
- type: CharField
- length: 25
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**15.1.** complications other

&nbsp;&nbsp;&nbsp;&nbsp; *Please include dates*
- db_table: inte_subject_complicationsfollowup
- column: complications_other
- type: TextField
---

**Section: CRF status**

**16.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_complicationsfollowup
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**17.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_complicationsfollowup
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Family History And Knowledge
*[missing model class docstring]*


*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_familyhistory
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_familyhistory
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: Part 1**

**3.0.** Do you know if anyone else in your household has <u>high blood pressure</u>?
- db_table: inte_subject_familyhistory
- column: htn_in_household
- type: CharField
- length: 25
- responses:
  - `No`: *No* 
  - `yes_spouse`: *Yes, my spouse* 
  - `yes_parents`: *Yes, one of my parents living with me* 
  - `yes_relative`: *Yes, another relative living with me* 
---

**4.0.** Do you know if anyone else in your household has <u>diabetes</u>?
- db_table: inte_subject_familyhistory
- column: dm_in_household
- type: CharField
- length: 25
- responses:
  - `No`: *No* 
  - `yes_spouse`: *Yes, my spouse* 
  - `yes_parents`: *Yes, one of my parents living with me* 
  - `yes_relative`: *Yes, another relative living with me* 
---

**5.0.** Do you know if anyone else in your household has <u>HIV</u>?
- db_table: inte_subject_familyhistory
- column: hiv_in_household
- type: CharField
- length: 25
- responses:
  - `No`: *No* 
  - `yes_spouse`: *Yes, my spouse* 
  - `yes_parents`: *Yes, one of my parents living with me* 
  - `yes_relative`: *Yes, another relative living with me* 
---

**Section: Part 2**

**6.0.** High blood pressure and high blood sugar can cause many illnesses like heart attacks, stroke, kidney failure
- db_table: inte_subject_familyhistory
- column: high_bp_bs_tf
- type: CharField
- length: 25
- responses:
  - `true`: *True* 
  - `false`: *False* 
  - `dont_know`: *Don't know* 
---

**7.0.** Being overweight protects from high blood pressure and high blood sugar
- db_table: inte_subject_familyhistory
- column: overweight_tf
- type: CharField
- length: 25
- responses:
  - `true`: *True* 
  - `false`: *False* 
  - `dont_know`: *Don't know* 
---

**8.0.** Salty food protects from high blood sugar
- db_table: inte_subject_familyhistory
- column: salty_foods_tf
- type: CharField
- length: 25
- responses:
  - `true`: *True* 
  - `false`: *False* 
  - `dont_know`: *Don't know* 
---

**9.0.** Regular exercise is important for people with <u>high blood pressure</u> or <u>high blood sugar</u> even if they are taking medicines for these conditions.
- db_table: inte_subject_familyhistory
- column: excercise_tf
- type: CharField
- length: 25
- responses:
  - `true`: *True* 
  - `false`: *False* 
  - `dont_know`: *Don't know* 
---

**10.0.** Drugs for <u>blood sugar</u> and <u>blood pressure</u> can make you unwell
- db_table: inte_subject_familyhistory
- column: take_medicine_tf
- type: CharField
- length: 25
- responses:
  - `true`: *True* 
  - `false`: *False* 
  - `dont_know`: *Don't know* 
---

**11.0.** It is best to stop taking <u>blood pressure</u> pills when you feel better and start pill taking again when you feel sick
- db_table: inte_subject_familyhistory
- column: stop_htn_meds_tf
- type: CharField
- length: 25
- responses:
  - `true`: *True* 
  - `false`: *False* 
  - `dont_know`: *Don't know* 
---

**12.0.** Herbs and traditional medicine are better for managing <u>blood pressure</u> than pills and medicines
- db_table: inte_subject_familyhistory
- column: traditional_htn_tf
- type: CharField
- length: 25
- responses:
  - `true`: *True* 
  - `false`: *False* 
  - `dont_know`: *Don't know* 
---

**13.0.** It is best to stop taking <u>blood sugar</u> medicines when you feel better and start pill taking again when you feel sick
- db_table: inte_subject_familyhistory
- column: stop_dm_meds_tf
- type: CharField
- length: 25
- responses:
  - `true`: *True* 
  - `false`: *False* 
  - `dont_know`: *Don't know* 
---

**14.0.** Herbs and traditional medicine are better for managing <u>diabetes</u> than pills and medicines
- db_table: inte_subject_familyhistory
- column: traditional_dm_tf
- type: CharField
- length: 25
- responses:
  - `true`: *True* 
  - `false`: *False* 
  - `dont_know`: *Don't know* 
---

**15.0.** Having drinks with sugar (e.g. tea/coffee) causes diabetes
- db_table: inte_subject_familyhistory
- column: dm_cause_tf
- type: CharField
- length: 25
- responses:
  - `true`: *True* 
  - `false`: *False* 
  - `dont_know`: *Don't know* 
---

**Section: CRF status**

**16.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_familyhistory
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**17.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_familyhistory
- column: crf_status_comments
- type: TextField
---




*Rendered on 2022-05-06 16:14*

#### Integrated Care Review
FORM 26 - Participant Review of Integrated Care.
*Instructions*: Please complete the form below. Required questions are in bold. When all required questions are complete click SAVE or, if available, SAVE NEXT. Based on your responses, additional questions may be required or some answers may need to be corrected.


**Section: Main**

**1.0.** subject visit
- db_table: inte_subject_integratedcarereview
- column: subject_visit
- type: OneToOneField
---

**2.0.** Report Date

&nbsp;&nbsp;&nbsp;&nbsp; *If reporting today, use today's date/time, otherwise use the date/time this information was reported.*
- db_table: inte_subject_integratedcarereview
- column: report_datetime
- type: DateTimeField
- format: YYYY-MM-DD HH:MM:SS.sss (tz=UTC)
---

**Section: Part 1a: Counselling - Health Talks**

**3.0.** Did you receive a health talk when attending the clinic today?
- db_table: inte_subject_integratedcarereview
- column: receive_health_talk_messages
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**4.0.** If YES, what disease conditions were discussed?
- db_table: inte_subject_integratedcarereview
- column: health_talk_conditions
- type: ManyToManyField
- responses: *Select all that apply*
  - `HIV`: *HIV infection* 
  - `diabetes`: *Diabetes* 
  - `hypertension`: *Hypertension* 
  - `OTHER`: *Other condition (specify below)* 
---

**4.1.** If other, please specify ...
- db_table: inte_subject_integratedcarereview
- column: health_talk_conditions_other
- type: CharField
- length: 35
- responses: *free text*
---

**5.0.** If YES, what type of messages were covered?
- db_table: inte_subject_integratedcarereview
- column: health_talk_focus
- type: ManyToManyField
- responses: *Select all that apply*
  - `lifestyle`: *Lifestyle* 
  - `diet`: *Diet* 
  - `medicines`: *Medicines* 
  - `OTHER`: *Other (specify below)* 
---

**5.1.** If other, please specify ...
- db_table: inte_subject_integratedcarereview
- column: health_talk_focus_other
- type: CharField
- length: 35
- responses: *free text*
---

**6.0.** If YES, who gave the health talk?
- db_table: inte_subject_integratedcarereview
- column: health_talk_presenters
- type: ManyToManyField
- responses: *Select all that apply*
  - `nurse`: *Nurse* 
  - `expert_patient_or_volunteer`: *Expert patient/Volunteer* 
  - `clinical_or_medical_officer`: *Clinical or medical officer* 
  - `OTHER`: *Other (specify below)* 
---

**6.1.** If other, please specify ...
- db_table: inte_subject_integratedcarereview
- column: health_talk_presenters_other
- type: CharField
- length: 35
- responses: *free text*
---

**Section: Part 1b: Counselling - Additional Health Advice**

**7.0.** Did you receive any additional health advice during your visit?
- db_table: inte_subject_integratedcarereview
- column: additional_health_advice
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**8.0.** If YES, who gave this health advice?
- db_table: inte_subject_integratedcarereview
- column: health_advice_advisor
- type: ManyToManyField
- responses: *Select all that apply*
  - `nurse`: *Nurse* 
  - `expert_patient_or_volunteer`: *Expert patient/Volunteer* 
  - `clinical_or_medical_officer`: *Clinical or medical officer* 
  - `OTHER`: *Other (specify below)* 
---

**8.1.** If other, please specify ...
- db_table: inte_subject_integratedcarereview
- column: health_advice_advisor_other
- type: CharField
- length: 35
- responses: *free text*
---

**9.0.** If YES, what was the focus of the advice?
- db_table: inte_subject_integratedcarereview
- column: health_advice_focus
- type: ManyToManyField
- responses: *Select all that apply*
  - `lifestyle`: *Lifestyle* 
  - `diet`: *Diet* 
  - `medicines`: *Medicines* 
  - `OTHER`: *Other (specify below)* 
---

**9.1.** If other, please specify ...
- db_table: inte_subject_integratedcarereview
- column: health_advice_focus_other
- type: CharField
- length: 35
- responses: *free text*
---

**Section: Part 2: Pharmacy Services**

**10.0.** Did you receive a drug prescription today?
- db_table: inte_subject_integratedcarereview
- column: receive_rx_today
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**11.0.** If YES, are you collecting it from this healthcare facility?
- db_table: inte_subject_integratedcarereview
- column: rx_collection_hcf
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No, I buy my own drugs* 
  - `N/A`: *Not applicable* 
---

**12.0.** If YES, where in this healthcare facility are your drugs dispensed from?
- db_table: inte_subject_integratedcarereview
- column: where_rx_dispensed
- type: ManyToManyField
- responses: *Select all that apply*
  - `pharmacy`: *Pharmacy* 
  - `consulting_room`: *Consulting room* 
  - `club`: *Patient club* 
  - `OTHER`: *Other (specify below)* 
---

**12.1.** If other, please specify ...
- db_table: inte_subject_integratedcarereview
- column: where_rx_dispensed_other
- type: CharField
- length: 35
- responses: *free text*
---

**13.0.** If YES, who in this healthcare facility is responsible for dispensing your drugs?
- db_table: inte_subject_integratedcarereview
- column: who_dispenses_rx
- type: ManyToManyField
- responses: *Select all that apply*
  - `pharmacist`: *Pharmacist* 
  - `doctor`: *Doctor* 
  - `nurse`: *Nurse* 
  - `OTHER`: *Other (specify below)* 
---

**13.1.** If other, please specify ...
- db_table: inte_subject_integratedcarereview
- column: who_dispenses_rx_other
- type: CharField
- length: 35
- responses: *free text*
---

**Section: Part 3: Managing Clinic Records and Appointments**

**14.0.** Do you have a hospital record stored in the clinic?
- db_table: inte_subject_integratedcarereview
- column: hospital_card
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `Dont_know`: *Do not know* 
---

**15.0.** If YES, what type of hospital record is this?
- db_table: inte_subject_integratedcarereview
- column: hospital_card_type
- type: CharField
- length: 15
- responses:
  - `paper_based`: *Paper-based* 
  - `electronic`: *Electronic* 
  - `both`: *Both* 
  - `N/A`: *Not Applicable* 
---

**16.0.** Have you missed an appointment since attending this clinic?
- db_table: inte_subject_integratedcarereview
- column: missed_appt
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**17.0.** If YES, did you get a phone call from the clinic about the missed appointment?
- db_table: inte_subject_integratedcarereview
- column: missed_appt_call
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**18.0.** If YES, who called you about the missed appointment?
- db_table: inte_subject_integratedcarereview
- column: missed_appt_call_who
- type: CharField
- length: 15
- responses:
  - `nurse`: *Nurse* 
  - `OTHER`: *Other* 
  - `N/A`: *Not applicable* 
---

**18.1.** If other, please specify ...
- db_table: inte_subject_integratedcarereview
- column: missed_appt_call_who_other
- type: CharField
- length: 35
- responses: *free text*
---

**Section: Part 4: Laboratory Services**

**19.0.** Have you done any laboratory tests since you started in this clinic?
- db_table: inte_subject_integratedcarereview
- column: lab_tests
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
---

**20.0.** If YES, did you pay for any of these tests?
- db_table: inte_subject_integratedcarereview
- column: pay_for_lab_tests
- type: CharField
- length: 15
- responses:
  - `Yes`: *Yes* 
  - `No`: *No* 
  - `N/A`: *Not applicable* 
---

**21.0.** If YES, which tests were you charged for?
- db_table: inte_subject_integratedcarereview
- column: which_lab_tests_charged_for
- type: ManyToManyField
- responses: *Select all that apply*
  - `blood_pressure_checks`: *Blood pressure checks* 
  - `blood_sugar_checks`: *Blood sugar checks* 
  - `viral_load_checks`: *Viral load checks* 
  - `OTHER`: *Other test (specify below)* 
---

**21.1.** If other, please specify ...
- db_table: inte_subject_integratedcarereview
- column: which_lab_tests_charged_for_other
- type: CharField
- length: 35
- responses: *free text*
---

**Section: CRF status**

**22.0.** CRF status

&nbsp;&nbsp;&nbsp;&nbsp; *If some data is still pending, flag this CRF as incomplete*
- db_table: inte_subject_integratedcarereview
- column: crf_status
- type: CharField
- length: 25
- responses:
  - `INCOMPLETE`: *Incomplete (some data pending)* 
  - `COMPLETE`: *Complete* 
---

**23.0.** Any comments related to status of this CRF

&nbsp;&nbsp;&nbsp;&nbsp; *for example, why some data is still pending*
- db_table: inte_subject_integratedcarereview
- column: crf_status_comments
- type: TextField
---


#### Requisitions



*Rendered on 2022-05-06 16:14*


