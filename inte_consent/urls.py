from django.urls.conf import path
from django.views.generic.base import RedirectView

from .admin_site import inte_consent_admin

app_name = "inte_consent"

urlpatterns = [
    path("", RedirectView.as_view(url="/inte_consent_admin/"), name="home_url"),
]
