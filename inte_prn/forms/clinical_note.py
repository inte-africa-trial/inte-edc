from django import forms
from edc_form_validators import FormValidator, FormValidatorMixin
from edc_sites.forms import SiteModelFormMixin

from ..models import ClinicalNote


class ClinicalNoteFormValidator(FormValidator):
    pass


class ClinicalNoteForm(
    SiteModelFormMixin,
    FormValidatorMixin,
    forms.ModelForm,
):

    form_validator_cls = ClinicalNoteFormValidator

    subject_identifier = forms.CharField(
        label="Subject Identifier",
        required=False,
        widget=forms.TextInput(attrs={"readonly": "readonly"}),
    )

    class Meta:
        model = ClinicalNote
        fields = "__all__"
