from django import forms
from django.core.exceptions import ObjectDoesNotExist

from ..models import HivInitialReview


def initial_review_exists_or_raise(form, model_cls):
    try:
        model_cls.objects.get(subject_visit=form.cleaned_data.get("subject_visit"))
    except ObjectDoesNotExist:
        raise forms.ValidationError(
            f"Complete the `{model_cls._meta.verbose_name}` CRF first."
        )
    return True


class InitialReviewRequiredModelFormMixin:
    def clean(self):
        initial_review_exists_or_raise(self, HivInitialReview)
        return super().clean()
