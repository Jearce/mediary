from django.urls import path

from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("plan",views.plan_trip,name="plan"),
    path("travler-account",views.create_account,name="create"),
    path("state-by-country/",views.get_states,name="get_states"),
    path("city-by-state/",views.get_cities,name="get_cities"),
]

