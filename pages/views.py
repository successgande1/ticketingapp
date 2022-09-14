from django.shortcuts import render, redirect
#from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from datetime import datetime
import datetime
from django.contrib.auth.models import User
from django.contrib import messages
from . models import  * 
from .forms import ContactForm

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
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['name']
            contact_email = form.cleaned_data['email']
            contact_phone = form.cleaned_data['phone']
            contact_subject = form.cleaned_data['subject']
            msg = form.cleaned_data['message']
            contact_us = Contact.objects.create(name = contact_name, email = contact_email, phone = contact_phone, subject = contact_subject,  message = msg)
            contact_us.save()
            messages.success(request, 'Thanks, Your Messsage has been Received.')
            return redirect('pages-contact')
    else:
        form = ContactForm()
    return render(request, 'pages/contact.html')

def buy_ticket(request):
    return render(request, 'pages/buy_tickets.html')