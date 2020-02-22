from django.urls.conf import path
from django.views.generic.base import RedirectView

from .admin_site import inte_prn_admin

app_name = "inte_prn"

urlpatterns = [
    path("admin/", inte_prn_admin.urls),
    path("", RedirectView.as_view(url=f"/{app_name}/admin/"), name="home_url"),
]
