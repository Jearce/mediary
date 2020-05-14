from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.db.models import prefetch_related_objects
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.http import HttpResponse,HttpResponseRedirect


from .forms import PlanTripForm
from .models import (Country,
                     Subdivision,
                     City,
                     LocalTransportation,
                     LocalGuide,
                     LocalLodging,
                     LocalAttraction)

class PlanTripView(FormView):
    form_class = PlanTripForm
    template_name = 'travel_agency/plan_trip.html'

class CountryListView(ListView):
    model = Country
    context_object_name = 'countries'
    template_name = 'travel_agency/country_list.html'

class SubdivisionListView(ListView):
    model = Subdivision
    context_object_name = "subdivisions"
    template_name = "travel_agency/subdivision_list.html"

    def get_queryset(self):
        country = self.kwargs['country_id']
        return self.model.objects.filter(country=country)

class HotelListView(FormView):

    form_class = PlanTripForm
    template_name = "travel_agency/city_list.html"


    def get_form_kwargs(self):
        kwargs = super(HotelListView, self).get_form_kwargs()
        subdivision = self.kwargs.get("subdivision_id")
        print(subdivision)
        cities = City.objects.filter(subdivision=subdivision)
        print(cities)
        kwargs['cities'] = cities
        return kwargs


    def get_context_data(self,**kwargs):
        context = super(HotelListView,self).get_context_data(**kwargs)
        subdivision = self.kwargs["subdivision_id"]
        cities = City.objects.filter(subdivision=subdivision)
        context['cities'] =  cities
        return context

def home(request):
    return render(request, 'travel_agency/home.html')

def load_hotels(request):
    city_id = request.GET.get('city')
    hotels = LocalLodging.objects.filter(city=city_id).order_by('name')
    return render(request,'travel_agency/state_dropdown_list_options.html',{'hotels':hotels})
