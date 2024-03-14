from django.urls import path
from . import views


urlpatterns =[
    # path('',views.getRoutes),
    path('',view=views.generalTest),
    path('auth_token/',view=views.obtainJwtToken),
    path("testDDOS/",view=views.testDDOS),
    path('testcsrf/',view=views.testCsrf),
    path('testInfd/',view=views.testInfoDisclosure),
    path('user_reg/',view=views.registration)
]