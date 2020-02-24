from edc_visit_schedule import FormsCollection, Crf

crfs_prn = FormsCollection(
    Crf(show_order=120, model="inte_subject.hivinitialreview"),
    Crf(show_order=130, model="inte_subject.diabetesinitialreview"),
    Crf(show_order=140, model="inte_subject.hypertensioninitialreview"),
    name="prn",
)
#
# crfs_unscheduled = FormsCollection(
#     Crf(show_order=10, model="inte_subject.bloodresultsglu"),
#     Crf(show_order=20, model="inte_subject.bloodresultsfbc"),
#     Crf(show_order=25, model="inte_subject.bloodresultslipid"),
#     Crf(show_order=30, model="inte_subject.bloodresultslft"),
#     Crf(show_order=40, model="inte_subject.bloodresultsrft"),
#     Crf(show_order=50, model="inte_subject.malariatest"),
#     Crf(show_order=60, model="inte_subject.urinedipsticktest"),
#     name="unscheduled",
# )


crfs_d1 = FormsCollection(
    Crf(show_order=100, model="inte_subject.baselinecarestatus"),
    Crf(show_order=110, model="inte_subject.anthropometry"),
    Crf(show_order=120, model="inte_subject.hivinitialreview"),
    Crf(show_order=130, model="inte_subject.diabetesinitialreview"),
    Crf(show_order=140, model="inte_subject.hypertensioninitialreview"),
    Crf(show_order=150, model="inte_subject.physicalactivity"),
    Crf(show_order=160, model="inte_subject.riskfactors"),
    name="day1",
)
crfs_1m = FormsCollection(name="1m")
crfs_2m = FormsCollection(name="2m")
crfs_3m = FormsCollection(name="3m")
crfs_4m = FormsCollection(name="4m")
crfs_5m = FormsCollection(name="5m")
crfs_6m = FormsCollection(
    Crf(show_order=110, model="inte_subject.anthropometry"),
    Crf(show_order=120, model="inte_subject.hivinitialreview"),
    Crf(show_order=130, model="inte_subject.diabetesinitialreview"),
    Crf(show_order=140, model="inte_subject.hypertensioninitialreview"),
    Crf(show_order=150, model="inte_subject.physicalactivity"),
    Crf(show_order=160, model="inte_subject.riskfactors"),
    Crf(show_order=200, model="inte_subject.healtheconomics"),
    name="6m",
)
crfs_7m = FormsCollection(name="7m")
crfs_8m = FormsCollection(name="8m")
crfs_9m = FormsCollection(name="9m")
crfs_10m = FormsCollection(name="10m")
crfs_11m = FormsCollection(name="11m")
crfs_12m = FormsCollection(
    Crf(show_order=110, model="inte_subject.anthropometry"),
    Crf(show_order=120, model="inte_subject.hivinitialreview"),
    Crf(show_order=130, model="inte_subject.diabetesinitialreview"),
    Crf(show_order=140, model="inte_subject.hypertensioninitialreview"),
    Crf(show_order=150, model="inte_subject.physicalactivity"),
    Crf(show_order=160, model="inte_subject.riskfactors"),
    Crf(show_order=200, model="inte_subject.healtheconomics"),
    name="12m",
)
