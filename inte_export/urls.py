from django.urls import path
from django.views.generic import RedirectView

app_name = "inte_export"

urlpatterns = [
    path("", RedirectView.as_view(url="/inte_export_admin/"), name="home_url"),
]
