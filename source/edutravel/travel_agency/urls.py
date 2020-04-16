from django.urls import path

from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("plan/",views.plan_trip,name='plan'),
    path("ajax/load-states/",views.load_states,name='ajax_load_states'),
    path("ajax/load-cities/",views.load_cities,name='ajax_load_cities'),
    path("travler-account",views.create_account,name="create"),
]

