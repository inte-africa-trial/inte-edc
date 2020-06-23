from django import forms
from django.core.exceptions import ObjectDoesNotExist

from ..models import CareStatus


def care_status_exists_or_raise(form):
    try:
        CareStatus.objects.get(subject_visit=form.cleaned_data.get("subject_visit"))
    except ObjectDoesNotExist:
        raise forms.ValidationError(
            f"Complete the `{CareStatus._meta.verbose_name}` CRF first."
        )
    return True


class CareStatusRequiredModelFormMixin:
    def clean(self):
        care_status_exists_or_raise(self)
        return super().clean()
