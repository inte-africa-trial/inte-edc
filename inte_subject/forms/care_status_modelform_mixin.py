from django import forms
from django.core.exceptions import ObjectDoesNotExist

from ..models import CareStatusBaseline


def care_status_exists_or_raise(form, model_cls=None):
    subject_identifier = form.cleaned_data.get("subject_visit").subject_identifier
    try:
        model_cls.objects.get(subject_visit__subject_identifier=subject_identifier)
    except ObjectDoesNotExist:
        raise forms.ValidationError(
            f"Complete the `{model_cls._meta.verbose_name}` CRF first."
        )
    return True


class CareStatusRequiredModelFormMixin:
    """Asserts Baseline Care Status exists"""

    def clean(self):
        if self.cleaned_data.get("subject_visit"):
            care_status_exists_or_raise(self, model_cls=CareStatusBaseline)
        return super().clean()
