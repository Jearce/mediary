from django.urls import path

from . import views

urlpatterns = [
    path("",
         views.home,
         name="home"),
    path("plan/",
         views.CountryListView.as_view(),
         name='plan'),
    path("plan/<int:country_id>/",
         views.SubdivisionListView.as_view(),
         name='list_subdivisions'),
    path("plan/<int:country_id>/<int:subdivision_id>/",
         views.HotelListView.as_view(),
         name="list_cities"),
    path("ajax/load-hotels/",
         views.load_hotels,
         name='ajax_load_hotels'),
    path("create-traveler-account/",
         views.create_account,
         name="CreateTraveler"),
]

