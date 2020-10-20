from edc_visit_schedule import FormsCollection, Crf

crfs_prn = FormsCollection(
    # Crf(show_order=175, model="inte_subject.healtheconomicsrevised"),
    Crf(show_order=178, model="inte_subject.familyhistory"),
    Crf(show_order=180, model="inte_subject.nextappointment"),
    Crf(show_order=200, model="inte_subject.cd4result"),
    Crf(show_order=210, model="inte_subject.glucose"),
    Crf(show_order=220, model="inte_subject.viralloadresult"),
    name="prn",
)

crfs_unscheduled = FormsCollection(
    Crf(show_order=110, model="inte_subject.clinicalreview"),
    Crf(show_order=111, model="inte_subject.indicators"),
    Crf(show_order=112, model="inte_subject.hivinitialreview", required=False),
    Crf(show_order=114, model="inte_subject.dminitialreview", required=False),
    Crf(show_order=116, model="inte_subject.htninitialreview", required=False),
    Crf(show_order=120, model="inte_subject.hivreview", required=False),
    Crf(show_order=130, model="inte_subject.dmreview", required=False),
    Crf(show_order=140, model="inte_subject.htnreview", required=False),
    Crf(show_order=145, model="inte_subject.medications"),
    Crf(show_order=150, model="inte_subject.drugrefillhtn", required=False),
    Crf(show_order=160, model="inte_subject.drugrefilldm", required=False),
    Crf(show_order=170, model="inte_subject.drugrefillhiv", required=False),
    Crf(show_order=185, model="inte_subject.hivmedicationadherence", required=False),
    Crf(show_order=190, model="inte_subject.dmmedicationadherence", required=False),
    Crf(show_order=195, model="inte_subject.htnmedicationadherence", required=False),
    Crf(show_order=200, model="inte_subject.complicationsfollowup", required=False),
    Crf(show_order=220, model="inte_subject.familyhistory"),
    Crf(show_order=230, model="inte_subject.nextappointment"),
    name="unscheduled",
)

crfs_missed = FormsCollection(
    Crf(show_order=10, model="inte_subject.subjectvisitmissed"), name="missed",
)


crfs_d1 = FormsCollection(
    Crf(show_order=100, model="inte_subject.clinicalreviewbaseline"),
    Crf(show_order=110, model="inte_subject.indicators"),
    Crf(show_order=120, model="inte_subject.hivinitialreview", required=False),
    Crf(show_order=130, model="inte_subject.dminitialreview", required=False),
    Crf(show_order=140, model="inte_subject.htninitialreview", required=False),
    Crf(show_order=143, model="inte_subject.medications"),
    Crf(show_order=145, model="inte_subject.drugrefillhtn", required=False),
    Crf(show_order=150, model="inte_subject.drugrefilldm", required=False),
    Crf(show_order=155, model="inte_subject.drugrefillhiv", required=False),
    Crf(show_order=160, model="inte_subject.otherbaselinedata"),
    Crf(show_order=165, model="inte_subject.complicationsbaseline"),
    Crf(show_order=170, model="inte_subject.nextappointment"),
    name="day1",
)
crfs_6m = FormsCollection(
    Crf(show_order=110, model="inte_subject.clinicalreview"),
    Crf(show_order=115, model="inte_subject.indicators"),
    Crf(show_order=112, model="inte_subject.hivinitialreview", required=False),
    Crf(show_order=114, model="inte_subject.dminitialreview", required=False),
    Crf(show_order=116, model="inte_subject.htninitialreview", required=False),
    Crf(show_order=130, model="inte_subject.hivreview", required=False),
    Crf(show_order=140, model="inte_subject.dmreview", required=False),
    Crf(show_order=150, model="inte_subject.htnreview", required=False),
    Crf(show_order=155, model="inte_subject.medications"),
    Crf(show_order=160, model="inte_subject.drugrefillhtn", required=False),
    Crf(show_order=170, model="inte_subject.drugrefilldm", required=False),
    Crf(show_order=180, model="inte_subject.drugrefillhiv", required=False),
    Crf(show_order=185, model="inte_subject.hivmedicationadherence", required=False),
    Crf(show_order=190, model="inte_subject.dmmedicationadherence", required=False),
    Crf(show_order=195, model="inte_subject.htnmedicationadherence", required=False),
    Crf(show_order=200, model="inte_subject.complicationsfollowup", required=False),
    Crf(show_order=210, model="inte_subject.healtheconomicsrevised"),
    Crf(show_order=220, model="inte_subject.familyhistory"),
    Crf(show_order=230, model="inte_subject.nextappointment"),
    name="6m",
)

crfs_12m = FormsCollection(
    Crf(show_order=110, model="inte_subject.clinicalreview"),
    Crf(show_order=115, model="inte_subject.indicators"),
    Crf(show_order=112, model="inte_subject.hivinitialreview", required=False),
    Crf(show_order=114, model="inte_subject.dminitialreview", required=False),
    Crf(show_order=116, model="inte_subject.htninitialreview", required=False),
    Crf(show_order=120, model="inte_subject.hivreview", required=False),
    Crf(show_order=130, model="inte_subject.dmreview", required=False),
    Crf(show_order=140, model="inte_subject.htnreview", required=False),
    Crf(show_order=145, model="inte_subject.medications"),
    Crf(show_order=150, model="inte_subject.drugrefillhtn", required=False),
    Crf(show_order=160, model="inte_subject.drugrefilldm", required=False),
    Crf(show_order=170, model="inte_subject.drugrefillhiv", required=False),
    Crf(show_order=185, model="inte_subject.hivmedicationadherence", required=False),
    Crf(show_order=190, model="inte_subject.dmmedicationadherence", required=False),
    Crf(show_order=195, model="inte_subject.htnmedicationadherence", required=False),
    Crf(show_order=200, model="inte_subject.complicationsfollowup", required=False),
    Crf(show_order=210, model="inte_subject.healtheconomicsrevised", required=False),
    Crf(show_order=220, model="inte_subject.familyhistory"),
    name="12m",
)
