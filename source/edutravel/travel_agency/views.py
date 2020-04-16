from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Country,Subdivision,City,LocalTransportation, LocalGuide, LocalLodging, LocalAttraction

# Create your views here.
def home(request):
    return render(request, 'travel_agency/home.html')

def plan_trip(request):
    countries = Country.objects.all()
    return render(request, 'travel_agency/plan_trip.html',{'countries':countries})

def get_states(request):
    countries = Country.objects.all()
    states = Subdivision.objects.filter(country=request.GET['choice'])
    return render(request,'travel_agency/state-by-country.html',{'states':states,'countries':countries})

def get_cities(request):

    countries = Country.objects.all()
    states = Subdivision.objects.filter(country=Subdivision.objects.get(pk=request.GET["state"]).country_id)
    cities = City.objects.filter(subdivision=request.GET["state"])
    return render(request,'travel_agency/city-by-state.html',{'states':states, 'countries':countries,'cities':cities})

def get_local_items(request):
    guides = LocalGuide.objects.filter(city=request.GET["city"])
    lodging = LocalLodging.objects.filter(city=request.GET["city"])
    transportation = LocalTransportation.objects.filter(city=request.GET["city"])
    attaction = LocalAttraction.objects.filter(city=request.GET["city"])
    return render(request, 'travel_agency/select-trip-options.html', {'guides':guides, 'lodging':lodging, 'attaction':attaction, 'transportation':transportation})

def create_account(request):
    return render(request, 'travel_agency/base_user.html')

