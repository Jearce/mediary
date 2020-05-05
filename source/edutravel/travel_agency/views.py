from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.db.models import prefetch_related_objects
from django.views.generic import ListView
from django.http import HttpResponse,HttpResponseRedirect

from .models import (Country,
                     Subdivision,
                     City,
                     LocalTransportation,
                     LocalGuide,
                     LocalLodging,
                     LocalAttraction)

from .forms import TripForm,TravelerForm

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

class HotelListView(ListView):
    model = City
    context_object_name = 'hotels'
    template_name = "travel_agency/city_list.html"

    def get_context_data(self,**kwargs):
        subdivision = self.kwargs["subdivision_id"]
        context = super(HotelListView,self).get_context_data(**kwargs)
        cities = self.model.objects.filter(subdivision=subdivision)
        hotels = LocalLodging.objects.filter(city__in=cities)
        context['cities'] =  cities
        context['hotels'] = hotels
        return context


# Create your views here.
def home(request):
    return render(request, 'travel_agency/home.html')



def plan_trip(request):
    form = TripForm()
    return render(request, 'travel_agency/plan_trip.html',{'form':form})


def load_hotels(request):
    city_id = request.GET.get('city')
    hotels = LocalLodging.objects.filter(city=city_id).order_by('name')
    return render(request,'travel_agency/state_dropdown_list_options.html',{'hotels':hotels})

def create_account(request):

    if request.method == 'POST':

        form = TravelerForm(request.POST)

        #if form is valid redirect to users account
        if form.is_valid():
            return HttpResponseRedict('/account/')
    else:
        form = TravelerForm()

    return render(request, 'travel_agency/base_user.html',{'form':form})

