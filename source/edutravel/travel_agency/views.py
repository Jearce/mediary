from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Country,Subdivision,City
from .forms import TripForm

# Create your views here.
def home(request):
    return render(request, 'travel_agency/home.html')

def plan_trip(request):
    form = TripForm()
    return render(request, 'travel_agency/plan_trip.html',{'form':form})

def load_states(request):
    country_id = request.GET.get('country')
    states = Subdivision.objects.filter(country=country_id).order_by('name')
    return render(request,'travel_agency/state_dropdown_list_options.html',{'states':states})

def load_cities(request):
    subdivision_id = request.GET.get('state')
    cities = City.objects.filter(subdivision=subdivision_id).order_by('name')
    return render(request,'travel_agency/city_dropdown_list_options.html',{'cities':cities})

def create_account(request):
    return render(request, 'travel_agency/base_user.html')

