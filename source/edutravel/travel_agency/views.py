from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Country,Subdivision,City

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


def create_account(request):
    return render(request, 'travel_agency/base_user.html')

