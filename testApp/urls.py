from django.urls import path
from . import views
urlpatterns = [
path("",view=views.home),
path("home/",view=views.homeRequest),
path("test/",view=views.requestTest),
path('requestHandler',view=views.requestHandler,name="requestHandler")
]
