from django import forms
from django.contrib import admin
from edc_model_admin import SimpleHistoryAdmin

from ..admin_site import inte_prn_admin
from ..forms import EndOfStudyForm
from ..models import EndOfStudy, OffScheduleHiv, OffScheduleNcd
from .modeladmin_mixins import EndOfStudyModelAdminMixin


class EndOfStudyNoSaveForm(EndOfStudyForm):
    def clean(self):
        raise forms.ValidationError(
            "Form cannot be saved. See forms "
            f"`{OffScheduleHiv._meta.verbose_name}` or `{OffScheduleNcd._meta.verbose_name}` "
            "instead."
        )


@admin.register(EndOfStudy, site=inte_prn_admin)
class EndOfStudyAdmin(EndOfStudyModelAdminMixin, SimpleHistoryAdmin):

    form = EndOfStudyNoSaveForm

    def has_delete_permission(self, request, obj=None):
        return False
