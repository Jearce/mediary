from django.db import transaction
from django import forms
from .models import (Trip,
                     TripDestinations,
                     Employee,
                     Booking,
                     LocalLodging,
                     LocalAttraction,
                     LocalTransportation,
                     LocalGuide,
                     )


class DateInput(forms.DateInput):
    input_type = 'date'

class PlanTripForm(forms.Form):

    trip_name = forms.CharField(max_length=120)
    start_date = forms.DateField(
        widget=forms.widgets.DateInput(attrs={'type':'date'})
    )

    end_date = forms.DateField(
       widget=forms.widgets.DateInput(attrs={'type':'date'})
    )

    lodging = forms.ModelChoiceField(
        queryset=LocalLodging.objects.none(),
        widget=forms.RadioSelect(),
        empty_label=None
    )

    destinations = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=LocalAttraction.objects.none()
    )

    def __init__(self,cities,*args, **kwargs):
        super(PlanTripForm,self).__init__(*args, **kwargs)
        self.fields['destinations'].queryset = LocalAttraction.objects.filter(city__in=cities)
        self.fields['lodging'].queryset = LocalLodging.objects.filter(city__in=cities)
        print(self.fields['lodging'].queryset)





