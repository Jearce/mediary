from django import forms
from .models import Trip,TripCity,Country,Subdivision,City

class TripForm(forms.Form):

    country = forms.ModelChoiceField(queryset=Country.objects.all())
    state = forms.ModelChoiceField(queryset=Subdivision.objects.all())
    #city = forms.ModelChoiceField(queryset=City.objects.all())

    #class Meta:
    #    model = Trip
    #    fields = ('name','country','subdivision','city')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['state'].queryset = Subdivision.objects.none()
        #self.fields['city'].queryset = City.objects.none()

class TravelerForm(forms.Form):
    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    email = forms.EmailField()
    passport = forms.CharField(max_length=8)
    phone_number = forms.CharField(max_length=12)

    def __init__(self, *args, **kwargs):
        super(TravelerForm,self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'



