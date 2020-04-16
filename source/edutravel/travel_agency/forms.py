from django import forms
from .models import Trip,TripCity,Country,Subdivision,City

class TripForm(forms.Form):
    country = forms.ModelChoiceField(queryset=Country.objects.all())
    state = forms.ModelChoiceField(queryset=Subdivision.objects.all())
    city = forms.ModelChoiceField(queryset=City.objects.all())

    #class Meta:
    #    model = Trip
    #    fields = ('name','country','subdivision','city')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['state'].queryset = Subdivision.objects.none()
        self.fields['city'].queryset = City.objects.none()


