from django.urls.conf import path
from django.views.generic.base import RedirectView

from .admin_site import inte_screening_admin

app_name = "inte_screening"

urlpatterns = [
    path("admin/", inte_screening_admin.urls),
    path("", RedirectView.as_view(url="/inte_screening/admin/"), name="home_url"),
]
