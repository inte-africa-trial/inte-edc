from django.urls.conf import path
from django.views.generic.base import RedirectView

from .admin_site import inte_subject_admin

app_name = "inte_subject"

urlpatterns = [
    path("admin/", inte_subject_admin.urls),
    path("", RedirectView.as_view(url="admin/"), name="home_url"),
]
