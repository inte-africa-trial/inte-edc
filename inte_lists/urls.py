from django.urls import path
from django.views.generic.base import RedirectView

from .admin_site import inte_lists_admin

app_name = "inte_lists"

urlpatterns = [
    path("admin/", inte_lists_admin.urls),
    path("", RedirectView.as_view(url="admin/"), name="home_url"),
]
