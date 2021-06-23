from django.urls.conf import path
from django.views.generic import RedirectView

app_name = "inte_screening"

urlpatterns = [
    path("", RedirectView.as_view(url="/inte_screening_admin/"), name="home_url"),
]
