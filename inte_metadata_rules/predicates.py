from django.core.exceptions import ObjectDoesNotExist
from edc_constants.constants import DIABETES, HIV, HYPERTENSION, YES
from edc_metadata_rules import PredicateCollection
from inte_subject.models import ReasonForVisit


class Predicates(PredicateCollection):

    app_label = "inte_subject"
    visit_model = f"{app_label}.subjectvisit"

    @staticmethod
    def _func_drug_refill(visit=None, refill_condition=None):
        has_refill_condition = False
        try:
            reason_for_visit = ReasonForVisit.objects.get(subject_visit=visit)
        except ObjectDoesNotExist:
            pass
        else:
            for m2m_obj in reason_for_visit.refill_conditions.all():
                if m2m_obj.name == refill_condition:
                    has_refill_condition = True
                    break
        return has_refill_condition

    def drug_refill_hiv(self, visit=None, **kwargs):
        return self._func_drug_refill(visit=visit, refill_condition=HIV)

    def drug_refill_hypertension(self, visit=None, **kwargs):
        return self._func_drug_refill(visit=visit, refill_condition=HYPERTENSION)

    def drug_refill_diabetes(self, visit=None, **kwargs):
        return self._func_drug_refill(visit=visit, refill_condition=DIABETES)
