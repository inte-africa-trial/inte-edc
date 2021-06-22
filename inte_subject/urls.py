from django.urls.conf import path
from django.views.generic import RedirectView

app_name = "inte_subject"

urlpatterns = [
    path("", RedirectView.as_view(url="/inte_subject_admin/"), name="home_url"),
]
