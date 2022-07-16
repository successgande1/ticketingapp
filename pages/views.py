from django.shortcuts import render, redirect
#from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from datetime import datetime
import datetime
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
# def login(request):
#     page_title = "User Login"

#     context = {
#         'page_title':page_title,
#     }
#     return render(request, 'user/login_page.html', context)

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')

def buy_ticket(request):
    return render(request, 'pages/buy_tickets.html')