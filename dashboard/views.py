from django.shortcuts import render, redirect
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from datetime import datetime
import datetime
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'dashboard/index.html') 

#Event Guess Index
def guest_home(request):
    return render(request, 'dashboard/guest_index.html')
    
