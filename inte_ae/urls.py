from django.urls.conf import path
from edc_adverse_event.views import AeHomeView

app_name = "inte_ae"

urlpatterns = [
    path("", AeHomeView.as_view(), name="home_url"),
]
