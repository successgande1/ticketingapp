from crispy_forms.helper import FormHelper
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from . models import *


class CreateUserForm(UserCreationForm):
    email = forms.EmailField
    group = forms.ModelChoiceField(queryset=Group.objects.all(),
                                   required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'group']

#Date Picket Widgets for date field for Event Form
class EventDateField(forms.DateInput):
    input_type = 'date'

#Add Event Form
class EventCreationForm(forms.ModelForm):
    
    class Meta:
        widgets = {'date':EventDateField()}
        model = Event
        fields = ['event_name','date', 'event_venue', 'event_logo']


#Add Ticket Form
class TicketCreationForm(forms.ModelForm):
    
    
    price = forms.CharField(label="Ticket Price :", 
                    widget=forms.TextInput(attrs={'placeholder': 'Amount to be Paid on Ticket'}))
    
    # refphone = PhoneNumberField(
    #     widget = PhoneNumberPrefixWidget(initial="NG")
    # )
    
    
    class Meta:
        model = Ticket
        fields = ['event','price', 'category']

#
class PinActivationForm(forms.Form):
    pin = forms.IntegerField(label='Pin', min_value=6)

    def clean_pin(self):
        form = self.cleaned_data['pin']

        

    
