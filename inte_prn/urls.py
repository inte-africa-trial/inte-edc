from django.urls.conf import path
from django.views.generic import RedirectView

app_name = "inte_prn"

urlpatterns = [
    path("", RedirectView.as_view(url="/inte_prn_admin/"), name="home_url"),
]
