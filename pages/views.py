from django.shortcuts import render, redirect
#from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from datetime import datetime
import datetime
from django.contrib.auth.models import User
from django.contrib import messages

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')