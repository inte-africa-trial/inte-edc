from django import forms
from django.core.exceptions import ObjectDoesNotExist

from ..models import CareStatusBaseline


def care_status_exists_or_raise(form, model_cls=None):
    try:
        model_cls.objects.get(subject_visit=form.cleaned_data.get("subject_visit"))
    except ObjectDoesNotExist:
        raise forms.ValidationError(
            f"Complete the `{model_cls._meta.verbose_name}` CRF first."
        )
    return True


class CareStatusRequiredModelFormMixin:
    def clean(self):
        care_status_exists_or_raise(self, model_cls=CareStatusBaseline)
        return super().clean()
