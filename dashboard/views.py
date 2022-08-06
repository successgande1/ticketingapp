from django.shortcuts import render, redirect
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from datetime import datetime
import datetime
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Count, Sum
from user.models import *

# Create your views here.

def index(request):
    #count Registered Guests
    reservations = Guest.objects.all().count()
    #count Number of Ticket Pins activated
    total_pin_activated = Ticket.objects.filter(pin__status="Activated").count()

    #Total by events
    total_events = Event.objects.all().count()
    
    #Sum Ticket activated
    amount_sold_pins = Ticket.objects.filter(pin__status="Activated").aggregate(
    total=Sum('price'))['total']
    

    context = {
        'guest':reservations,
        'total':amount_sold_pins,
        'total_pin_activated':total_pin_activated,
        'total_events':total_events,
    }
    return render(request, 'user/profile.html', context) 

#Event Guess Index 
def guest_home(request):
    return render(request, 'user/profile.html')
    
