from django.urls import path

from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("plan/",views.plan_trip,name='plan'),
    path("ajax/load-states/",views.load_states,name='ajax_load_states'),
    path("ajax/load-cities/",views.load_cities,name='ajax_load_cities'),
    path("signin/",views.user_login,name='login'),
    path("traveler-account/",views.register_trip,name="register"),
]

