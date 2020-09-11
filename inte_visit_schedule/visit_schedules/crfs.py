from edc_visit_schedule import FormsCollection, Crf

crfs_prn = FormsCollection(
    Crf(show_order=120, model="inte_subject.hivinitialreview"),
    Crf(show_order=130, model="inte_subject.dminitialreview"),
    Crf(show_order=140, model="inte_subject.htninitialreview"),
    # Crf(show_order=150, model="inte_subject.healtheconomicsrevised"),
    # Crf(show_order=160, model="inte_subject.dmreview"),
    # Crf(show_order=170, model="inte_subject.htnreview"),
    name="prn",
)

crfs_unscheduled = FormsCollection(
    Crf(show_order=105, model="inte_subject.indicators"),
    Crf(show_order=110, model="inte_subject.clinicalreview"),
    Crf(show_order=112, model="inte_subject.hivinitialreview"),
    Crf(show_order=114, model="inte_subject.dminitialreview"),
    Crf(show_order=116, model="inte_subject.htninitialreview"),
    Crf(show_order=120, model="inte_subject.hivreview"),
    Crf(show_order=130, model="inte_subject.dmreview"),
    Crf(show_order=140, model="inte_subject.htnreview"),
    Crf(show_order=145, model="inte_subject.medications"),
    Crf(show_order=150, model="inte_subject.drugrefillhtn"),
    Crf(show_order=160, model="inte_subject.drugrefilldm"),
    Crf(show_order=170, model="inte_subject.drugrefillhiv"),
    Crf(show_order=175, model="inte_subject.healtheconomicsrevised"),
    Crf(show_order=178, model="inte_subject.familyhistory"),
    Crf(show_order=180, model="inte_subject.nextappointment"),
    name="unscheduled",
)

crfs_missed = FormsCollection(
    Crf(show_order=10, model="inte_subject.subjectvisitmissed"), name="missed",
)

crfs_d1 = FormsCollection(
    # Crf(show_order=90, model="inte_subject.reasonforvisit"),
    Crf(show_order=100, model="inte_subject.clinicalreviewbaseline"),
    Crf(show_order=110, model="inte_subject.indicators"),
    Crf(show_order=120, model="inte_subject.hivinitialreview"),
    Crf(show_order=130, model="inte_subject.dminitialreview"),
    Crf(show_order=140, model="inte_subject.htninitialreview"),
    Crf(show_order=143, model="inte_subject.medications"),
    Crf(show_order=145, model="inte_subject.drugrefillhtn"),
    Crf(show_order=150, model="inte_subject.drugrefilldm"),
    Crf(show_order=155, model="inte_subject.drugrefillhiv"),
    Crf(show_order=160, model="inte_subject.otherbaselinedata"),
    Crf(show_order=165, model="inte_subject.complications"),
    Crf(show_order=170, model="inte_subject.nextappointment"),
    name="day1",
)
crfs_6m = FormsCollection(
    # Crf(show_order=100, model="inte_subject.reasonforvisit"),
    Crf(show_order=105, model="inte_subject.indicators"),
    Crf(show_order=110, model="inte_subject.clinicalreview"),
    Crf(show_order=130, model="inte_subject.hivreview"),
    Crf(show_order=140, model="inte_subject.dmreview"),
    Crf(show_order=150, model="inte_subject.htnreview"),
    Crf(show_order=155, model="inte_subject.medications"),
    Crf(show_order=160, model="inte_subject.drugrefillhtn"),
    Crf(show_order=170, model="inte_subject.drugrefilldm"),
    Crf(show_order=180, model="inte_subject.drugrefillhiv"),
    Crf(show_order=185, model="inte_subject.healtheconomicsrevised"),
    Crf(show_order=188, model="inte_subject.familyhistory"),
    Crf(show_order=190, model="inte_subject.nextappointment"),
    name="6m",
)

crfs_12m = FormsCollection(
    # Crf(show_order=100, model="inte_subject.reasonforvisit"),
    Crf(show_order=105, model="inte_subject.indicators"),
    Crf(show_order=110, model="inte_subject.clinicalreview"),
    Crf(show_order=120, model="inte_subject.hivreview"),
    Crf(show_order=130, model="inte_subject.dmreview"),
    Crf(show_order=140, model="inte_subject.htnreview"),
    Crf(show_order=145, model="inte_subject.medications"),
    Crf(show_order=150, model="inte_subject.drugrefillhtn"),
    Crf(show_order=160, model="inte_subject.drugrefilldm"),
    Crf(show_order=170, model="inte_subject.drugrefillhiv"),
    Crf(show_order=175, model="inte_subject.healtheconomicsrevised"),
    Crf(show_order=178, model="inte_subject.familyhistory"),
    name="12m",
)
