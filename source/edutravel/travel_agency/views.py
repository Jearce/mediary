from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Country

# Create your views here.
def index(request):
    return render(request, 'travel_agency/home.html')


