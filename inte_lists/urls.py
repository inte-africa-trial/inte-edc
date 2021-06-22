from django.urls import path
from django.views.generic import RedirectView

app_name = "inte_lists"

urlpatterns = [
    path("", RedirectView.as_view(url="/inte_lists_admin/"), name="home_url"),
]
