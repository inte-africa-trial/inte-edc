from django.contrib.admin.decorators import register
from django.contrib.sites.shortcuts import get_current_site
from edc_auth import UNBLINDING_REQUESTORS, UNBLINDING_REVIEWERS
from edc_auth.admin import UserAdmin as BaseUserAdmin

from ..admin_site import inte_prn_admin
from ..models import UnblindingRequestorUser, UnblindingReviewerUser


@register(UnblindingRequestorUser, site=inte_prn_admin)
class UnblindingRequestorUserAdmin(BaseUserAdmin):
    ordering = ("first_name", "last_name")
    search_fields = ("first_name", "last_name", "username", "email")

    inlines = []

    populate_data_dictionary = False

    def get_queryset(self, request):
        opts = dict(
            userprofile__sites__id=get_current_site(request).id,
            groups__name__in=[UNBLINDING_REQUESTORS],
        )
        return super().get_queryset(request).filter(**opts)


@register(UnblindingReviewerUser, site=inte_prn_admin)
class UnblindingReviewerUserAdmin(BaseUserAdmin):
    ordering = ("first_name", "last_name")
    search_fields = ("first_name", "last_name", "username", "email")

    inlines = []

    populate_data_dictionary = False

    def get_queryset(self, request):
        opts = dict(
            userprofile__sites__id=get_current_site(request).id,
            groups__name__in=[UNBLINDING_REVIEWERS],
        )
        return super().get_queryset(request).filter(**opts)
