from django.urls import path

from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("plan",views.plan_trip,name="plan"),
    path("travler-account",views.create_account,name="create"),
]

