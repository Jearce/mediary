from django import forms
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm

from .models import Institute,InstituteType,User

class InstituteSignUpForm(UserCreationForm):

    country_address = forms.CharField(max_length=80)
    state_address = forms.CharField(max_length=80)
    city_address = forms.CharField(max_length=80)
    state_address = forms.CharField(max_length=80)
    institute_type = forms.ModelChoiceField(
        queryset=InstituteType.objects.all()
    )

    class Meta(UserCreationForm.Meta):
        model = User

    def __init__(self, *args, **kwargs):
        super(InstituteSignUpForm,self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_institute = True
        user.save()
        institute = Institute.objects.create(
            user=user,
            country_address=self.cleaned_data.get('country_address'),
            city_address=self.cleaned_data.get('city_address'),
            state_address=self.cleaned_data.get('state_address'),
            institute_type=self.cleaned_data.get('institute_type'),
        )
        return user

