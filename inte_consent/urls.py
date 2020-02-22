from django.urls.conf import path
from django.views.generic.base import RedirectView

from .admin_site import inte_consent_admin

app_name = "inte_consent"

urlpatterns = [
    path("admin/", inte_consent_admin.urls),
    path("", RedirectView.as_view(url="admin/"), name="home_url"),
]
