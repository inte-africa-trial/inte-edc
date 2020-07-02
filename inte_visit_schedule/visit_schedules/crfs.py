from edc_visit_schedule import FormsCollection, Crf

crfs_prn = FormsCollection(
    Crf(show_order=120, model="inte_subject.hivinitialreview"),
    Crf(show_order=130, model="inte_subject.diabetesinitialreview"),
    Crf(show_order=140, model="inte_subject.hypertensioninitialreview"),
    # Crf(show_order=150, model="inte_subject.hivreview"),
    # Crf(show_order=160, model="inte_subject.diabetesreview"),
    # Crf(show_order=170, model="inte_subject.hypertensionreview"),
    name="prn",
)

crfs_unscheduled = FormsCollection(
    Crf(show_order=110, model="inte_subject.indicators"),
    Crf(show_order=120, model="inte_subject.hivinitialreview"),
    Crf(show_order=130, model="inte_subject.diabetesinitialreview"),
    Crf(show_order=140, model="inte_subject.hypertensioninitialreview"),
    name="unscheduled",
)

crfs_missed = FormsCollection(
    Crf(show_order=10, model="inte_subject.subjectvisitmissed"), name="missed",
)

crfs_d1 = FormsCollection(
    Crf(show_order=90, model="inte_subject.reasonforvisit"),
    Crf(show_order=100, model="inte_subject.carestatusbaseline"),
    Crf(show_order=110, model="inte_subject.indicators"),
    Crf(show_order=120, model="inte_subject.hivinitialreview"),
    Crf(show_order=130, model="inte_subject.diabetesinitialreview"),
    Crf(show_order=140, model="inte_subject.hypertensioninitialreview"),
    Crf(show_order=145, model="inte_subject.drugrefillhypertension"),
    Crf(show_order=150, model="inte_subject.drugrefilldiabetes"),
    Crf(show_order=155, model="inte_subject.drugrefillhiv"),
    Crf(show_order=160, model="inte_subject.otherbaselinedata"),
    Crf(show_order=165, model="inte_subject.complications"),
    Crf(show_order=170, model="inte_subject.nextappointment"),
    name="day1",
)
crfs_1m = FormsCollection(
    Crf(show_order=100, model="inte_subject.reasonforvisit"),
    Crf(show_order=110, model="inte_subject.investigations"),
    Crf(show_order=120, model="inte_subject.hivreview"),
    Crf(show_order=130, model="inte_subject.diabetesreview"),
    Crf(show_order=140, model="inte_subject.hypertensionreview"),
    Crf(show_order=150, model="inte_subject.drugrefillhypertension"),
    Crf(show_order=160, model="inte_subject.drugrefilldiabetes"),
    Crf(show_order=170, model="inte_subject.drugrefillhiv"),
    Crf(show_order=180, model="inte_subject.nextappointment"),
    name="1m",
)  # routine for NCD
crfs_2m = FormsCollection(
    Crf(show_order=100, model="inte_subject.reasonforvisit"),
    Crf(show_order=110, model="inte_subject.investigations"),
    Crf(show_order=120, model="inte_subject.hivreview"),
    Crf(show_order=130, model="inte_subject.diabetesreview"),
    Crf(show_order=140, model="inte_subject.hypertensionreview"),
    Crf(show_order=150, model="inte_subject.drugrefillhypertension"),
    Crf(show_order=160, model="inte_subject.drugrefilldiabetes"),
    Crf(show_order=170, model="inte_subject.drugrefillhiv"),
    Crf(show_order=180, model="inte_subject.nextappointment"),
    name="2m",
)  # routine for NCD
crfs_3m = FormsCollection(
    Crf(show_order=100, model="inte_subject.reasonforvisit"),
    Crf(show_order=110, model="inte_subject.investigations"),
    Crf(show_order=120, model="inte_subject.hivreview"),
    Crf(show_order=130, model="inte_subject.diabetesreview"),
    Crf(show_order=140, model="inte_subject.hypertensionreview"),
    Crf(show_order=150, model="inte_subject.drugrefillhypertension"),
    Crf(show_order=160, model="inte_subject.drugrefilldiabetes"),
    Crf(show_order=170, model="inte_subject.drugrefillhiv"),
    Crf(show_order=180, model="inte_subject.nextappointment"),
    name="3m",
)  # routine for NCD/HIV
crfs_4m = FormsCollection(
    Crf(show_order=100, model="inte_subject.reasonforvisit"),
    Crf(show_order=110, model="inte_subject.investigations"),
    Crf(show_order=120, model="inte_subject.hivreview"),
    Crf(show_order=130, model="inte_subject.diabetesreview"),
    Crf(show_order=140, model="inte_subject.hypertensionreview"),
    Crf(show_order=150, model="inte_subject.drugrefillhypertension"),
    Crf(show_order=160, model="inte_subject.drugrefilldiabetes"),
    Crf(show_order=170, model="inte_subject.drugrefillhiv"),
    Crf(show_order=180, model="inte_subject.nextappointment"),
    name="4m",
)  # routine for NCD
crfs_5m = FormsCollection(
    Crf(show_order=100, model="inte_subject.reasonforvisit"),
    Crf(show_order=110, model="inte_subject.investigations"),
    Crf(show_order=120, model="inte_subject.hivreview"),
    Crf(show_order=130, model="inte_subject.diabetesreview"),
    Crf(show_order=140, model="inte_subject.hypertensionreview"),
    Crf(show_order=150, model="inte_subject.drugrefillhypertension"),
    Crf(show_order=160, model="inte_subject.drugrefilldiabetes"),
    Crf(show_order=170, model="inte_subject.drugrefillhiv"),
    Crf(show_order=180, model="inte_subject.nextappointment"),
    name="5m",
)  # routine for NCD
crfs_6m = FormsCollection(
    Crf(show_order=100, model="inte_subject.reasonforvisit"),
    Crf(show_order=110, model="inte_subject.investigations"),
    Crf(show_order=120, model="inte_subject.indicators"),
    Crf(show_order=130, model="inte_subject.hivreview"),
    Crf(show_order=140, model="inte_subject.diabetesreview"),
    Crf(show_order=150, model="inte_subject.hypertensionreview"),
    Crf(show_order=160, model="inte_subject.drugrefillhypertension"),
    Crf(show_order=170, model="inte_subject.drugrefilldiabetes"),
    Crf(show_order=180, model="inte_subject.drugrefillhiv"),
    Crf(show_order=190, model="inte_subject.nextappointment"),
    name="6m",
)
crfs_7m = FormsCollection(
    Crf(show_order=100, model="inte_subject.reasonforvisit"),
    Crf(show_order=110, model="inte_subject.investigations"),
    Crf(show_order=120, model="inte_subject.hivreview"),
    Crf(show_order=130, model="inte_subject.diabetesreview"),
    Crf(show_order=140, model="inte_subject.hypertensionreview"),
    Crf(show_order=150, model="inte_subject.drugrefillhypertension"),
    Crf(show_order=160, model="inte_subject.drugrefilldiabetes"),
    Crf(show_order=170, model="inte_subject.drugrefillhiv"),
    Crf(show_order=180, model="inte_subject.nextappointment"),
    name="7m",
)  # routine for NCD
crfs_8m = FormsCollection(
    Crf(show_order=100, model="inte_subject.reasonforvisit"),
    Crf(show_order=110, model="inte_subject.investigations"),
    Crf(show_order=120, model="inte_subject.hivreview"),
    Crf(show_order=130, model="inte_subject.diabetesreview"),
    Crf(show_order=140, model="inte_subject.hypertensionreview"),
    Crf(show_order=150, model="inte_subject.drugrefillhypertension"),
    Crf(show_order=160, model="inte_subject.drugrefilldiabetes"),
    Crf(show_order=170, model="inte_subject.drugrefillhiv"),
    Crf(show_order=180, model="inte_subject.nextappointment"),
    name="8m",
)  # routine for NCD
crfs_9m = FormsCollection(
    Crf(show_order=100, model="inte_subject.reasonforvisit"),
    Crf(show_order=110, model="inte_subject.investigations"),
    Crf(show_order=120, model="inte_subject.hivreview"),
    Crf(show_order=130, model="inte_subject.diabetesreview"),
    Crf(show_order=140, model="inte_subject.hypertensionreview"),
    Crf(show_order=150, model="inte_subject.drugrefillhypertension"),
    Crf(show_order=160, model="inte_subject.drugrefilldiabetes"),
    Crf(show_order=170, model="inte_subject.drugrefillhiv"),
    Crf(show_order=180, model="inte_subject.nextappointment"),
    name="9m",
)  # routine for NCD/HIV
crfs_10m = FormsCollection(
    Crf(show_order=100, model="inte_subject.reasonforvisit"),
    Crf(show_order=105, model="inte_subject.indicators"),
    Crf(show_order=110, model="inte_subject.investigations"),
    Crf(show_order=120, model="inte_subject.hivreview"),
    Crf(show_order=130, model="inte_subject.diabetesreview"),
    Crf(show_order=140, model="inte_subject.hypertensionreview"),
    Crf(show_order=150, model="inte_subject.drugrefillhypertension"),
    Crf(show_order=160, model="inte_subject.drugrefilldiabetes"),
    Crf(show_order=170, model="inte_subject.drugrefillhiv"),
    name="10m",
)  # routine for NCD
crfs_11m = FormsCollection(
    Crf(show_order=100, model="inte_subject.reasonforvisit"),
    Crf(show_order=110, model="inte_subject.investigations"),
    Crf(show_order=120, model="inte_subject.hivreview"),
    Crf(show_order=130, model="inte_subject.diabetesreview"),
    Crf(show_order=140, model="inte_subject.hypertensionreview"),
    Crf(show_order=150, model="inte_subject.drugrefillhypertension"),
    Crf(show_order=160, model="inte_subject.drugrefilldiabetes"),
    Crf(show_order=170, model="inte_subject.drugrefillhiv"),
    Crf(show_order=180, model="inte_subject.nextappointment"),
    name="11m",
)  # routine for NCD
crfs_12m = FormsCollection(
    Crf(show_order=100, model="inte_subject.reasonforvisit"),
    Crf(show_order=110, model="inte_subject.investigations"),
    Crf(show_order=120, model="inte_subject.hivreview"),
    Crf(show_order=130, model="inte_subject.diabetesreview"),
    Crf(show_order=140, model="inte_subject.hypertensionreview"),
    Crf(show_order=150, model="inte_subject.drugrefillhypertension"),
    Crf(show_order=160, model="inte_subject.drugrefilldiabetes"),
    Crf(show_order=170, model="inte_subject.drugrefillhiv"),
    name="12m",
)
