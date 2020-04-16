from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Country

# Create your views here.
def home(request):
    return render(request, 'travel_agency/home.html')

def plan_trip(request):
    countries = Country.objects.all()
    return render(request, 'travel_agency/plan_trip.html',{'countries':countries})

def create_account(request):
    return render(request, 'travel_agency/base_user.html')

