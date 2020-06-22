from edc_visit_schedule import FormsCollection, Crf

crfs_prn = FormsCollection(
    Crf(show_order=120, model="inte_subject.hivinitialreview"),
    Crf(show_order=130, model="inte_subject.diabetesinitialreview"),
    Crf(show_order=140, model="inte_subject.hypertensioninitialreview"),
    name="prn",
)

crfs_unscheduled = FormsCollection(
    Crf(show_order=110, model="inte_subject.indicators"),
    Crf(show_order=120, model="inte_subject.hivinitialreview"),
    Crf(show_order=130, model="inte_subject.diabetesinitialreview"),
    Crf(show_order=140, model="inte_subject.hypertensioninitialreview"),
    name="unscheduled",
)


crfs_d1 = FormsCollection(
    Crf(show_order=100, model="inte_subject.carestatus"),
    Crf(show_order=110, model="inte_subject.indicators"),
    Crf(show_order=120, model="inte_subject.hivinitialreview"),
    Crf(show_order=130, model="inte_subject.diabetesinitialreview"),
    Crf(show_order=140, model="inte_subject.hypertensioninitialreview"),
    Crf(show_order=160, model="inte_subject.healthriskassessment"),
    name="day1",
)
crfs_1m = FormsCollection(name="1m")  # routine for NCD
crfs_2m = FormsCollection(name="2m")  # routine for NCD
crfs_3m = FormsCollection(name="3m")  # routine for NCD/HIV
crfs_4m = FormsCollection(name="4m")  # routine for NCD
crfs_5m = FormsCollection(name="5m")  # routine for NCD
crfs_6m = FormsCollection(
    Crf(show_order=110, model="inte_subject.indicators"),
    Crf(show_order=120, model="inte_subject.hivinitialreview"),
    Crf(show_order=130, model="inte_subject.diabetesinitialreview"),
    Crf(show_order=140, model="inte_subject.hypertensioninitialreview"),
    Crf(show_order=160, model="inte_subject.healthriskassessment"),
    Crf(show_order=200, model="inte_subject.carestatus"),
    name="6m",
)
crfs_7m = FormsCollection(name="7m")  # routine for NCD
crfs_8m = FormsCollection(name="8m")  # routine for NCD
crfs_9m = FormsCollection(name="9m")  # routine for NCD/HIV
crfs_10m = FormsCollection(name="10m")  # routine for NCD
crfs_11m = FormsCollection(name="11m")  # routine for NCD
crfs_12m = FormsCollection(
    Crf(show_order=110, model="inte_subject.indicators"),
    Crf(show_order=120, model="inte_subject.hivinitialreview"),
    Crf(show_order=130, model="inte_subject.diabetesinitialreview"),
    Crf(show_order=140, model="inte_subject.hypertensioninitialreview"),
    Crf(show_order=160, model="inte_subject.healthriskassessment"),
    Crf(show_order=200, model="inte_subject.carestatus"),
    name="12m",
)
