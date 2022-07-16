from django.shortcuts import render, redirect
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.views.generic.list import ListView
#from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from django.views.generic.detail import DetailView
from django.urls import reverse, reverse_lazy
from django.http import JsonResponse
from . models import *
from . forms import *
from django.core import paginator
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required

# def login(request):
#     page_title = "User Login"

#     context = {
#         'page_title':page_title,
#     }
#     return render(request, 'user/login_page.html', context)

#Register New User Method

def register(request):
    #Create variable and query all users
    workers = User.objects.all()
    #Page Name
    page_title = "User Register"
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registered Successfully.')
            return redirect('dashboard-index')
    else:
        form = CreateUserForm()
    context = {
        'form':form,
        'workers':workers,
        'page_title':page_title,
    }
    return render(request, 'user/register.html', context)



@login_required(login_url='user-login')
def profile(request):
    #count submited Applications
    
    
 
    return render(request, 'user/profile.html')
   
#Update Profile Method
@login_required(login_url='user-login')
def profile_update(request):
    if request.method == 'POST':
        #create user form variable
        user_form = UserUpdateForm(request.POST, instance=request.user)
        #create update form variable
        

        profile_form = ProfileUpdateForm(request.POST, request.FILES, 
        instance=request.user.profile)
    #Check if both forms are valid
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully.')
            return redirect('user-add-drink')
            #profile_form.cleaned_data['profilestatus'] ='Updated'
            
            # image = profile_form.cleaned_data['image']

            # if not image:
            #     messages.error(request, 'Passport is Needed.')
            #     return redirect('user-profile-update')

            # else:
                
        else:
            messages.error(request, 'Check Your Passport Image.')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'user/profile_update.html', context)

#Create Event View
class EventCreateView(LoginRequiredMixin, CreateView):
    #permission_required: 'Ticket.add_ticket'
    model = Event
    form_class = EventCreationForm
    template_name = 'user/add_event.html'
    success_url = reverse_lazy('event-list')
    success_message = 'Event Added Successfully'

#Event List View
class EventListView(ListView):
	template_name = 'user/event_list.html'
	queryset = Event.objects.all()
	context_object_name = 'events'

#Create Ticket View
class TicketCreateView(LoginRequiredMixin, CreateView):
    #permission_required: 'Ticket.add_ticket'
    model = Ticket
    form_class = TicketCreationForm
    template_name = 'user/add_ticket.html'
    success_url = reverse_lazy('ticket-list')
    
    # def get_success_url(self):
    #     return reverse_lazy('ticket-detail',kwargs={'pk': self.get_object().id})

#Tick List View
class TicketListView(ListView):
	template_name = 'user/ticket_list.html'
	queryset = Ticket.objects.all()
	context_object_name = 'tickets'
    #paginate_by  = 10

#Ticket Detail
class TicketDetail(LoginRequiredMixin, DetailView):
    template_name = 'user/ticket_detail.html'
    model = Ticket

    def get_success_url(self):
        return reverse_lazy('generate-pin', kwargs = {'pk' : self.get_object().id})

#Function to Generate Pin for Tickets
@login_required(login_url='user-login')
def generate_pins_for_ticket(request, ticket_id):
    if request.user.is_superuser:
        ticket = Ticket.objects.get(id=ticket_id)
        for _ in range(20):
            Pin.objects.create(ticket=ticket)
        messages.success(request, 'You have Generated 20 PINs Ticket.')
        return redirect('pin-list')
    else:
        messages.success(request, 'You are not Authorize to Generate PINs for Tickets.')
        return redirect('dashboard-index')

#PIN List View
class PinListView(ListView):
	template_name = 'user/pin_list.html'
	queryset = Pin.objects.all()
	context_object_name = 'pins'

#Pin Activation View
def pin_activation(request):

    if request.method == "POST":
        
        #Create new form with name form
        form = PinActivationForm(request.POST)

        #Check if the the form has valid data in it
        if form.is_valid():

            #Check the status of the user Pin with the one in the Database
            check_pin_status = Pin.objects.filter(value=form['pin'].value(), status='Not Activated')

            #Check if the PIN is correct and NOT ACTIVATED
            if check_pin_status:

                #Update the User Pin with a new status of Activated
                Pin.objects.filter(value=form['pin'].value()).update(status='Validated')
                #Message the User
                messages.success(request, 'Pin Validated Successfully')
                #Redirect the user to register for seat
                return redirect('register-guest')
            #Check filter the DB where the PIN status is Validated
            elif Pin.objects.filter(value=form['pin'].value(), status="Validated"):
                messages.error(request, 'Pin Already Validated. Register for Seat')
                return redirect('register-guest')
            #Check Filter PIN in DB where Status is Activated
            elif  Pin.objects.filter(value=form['pin'].value(), status="Activated"):
                messages.error(request, "Pin Already Activated, Login.")
                return redirect('user-login')
                
                   
        else:
            messages.error(request, 'Something Went Wrong. Try again')
    else:
        form = PinActivationForm()
    context = {
        'form':form,
    }
    return render(request, 'user/pin_activation.html', context)

#Register New User Method
def register_guest(request):
    #Create variable and query all users
    #user_pins = Pin.objects.all()
    page_title = "Festival Registration"
    if request.method == 'POST':
        form = GuestUserForm(request.POST)
        pin_form = PinActivationForm(request.POST)
        if form.is_valid() and pin_form.is_valid():
            Guest.objects.create(guest_name=form['username'].value(), pin=pin_form['pin'].value())
            form.save()
            Pin.objects.filter(value=pin_form['pin'].value()).update(status='Activated')
            messages.success(request, 'Registered Successfully. Login')

            #Pin.objects.filter(value=form['pin'].value()).update(status='Validated')
            return redirect('user-login')
    else:
        form = GuestUserForm()
        pin_form = PinActivationForm()
    context = {
        'form':form,
        'pin_form':pin_form,
        'page_title':page_title,
    }
    return render(request, 'user/register.html', context)

#User List View
class UserListView(ListView):
	template_name = 'user/staff_list.html'
	queryset = User.objects.all()
	context_object_name = 'users'

@login_required(login_url='user-login')
def Guest_Add_Drink(request):

    try:
        guest_drink = Drink.objects.get(user=request.user)
    except Drink.DoesNotExist:
        if request.method=='POST':
            form = DrinkForm(request.POST)
            if form.is_valid():
                drink = form.save(commit=False)
                drink.user = request.user
                drink.save()
                form.save_m2m() # needed since using commit=False
                return redirect('guest-confirmation')
            
        else:
            form = DrinkForm()
        
        context = {
            'form':form,
            'Page':'Event Drinks Preference',
        }

        return render (request, 'user/add_guest_drink.html', context )
    else:
        return redirect('guest-confirmation')
        

    

@login_required(login_url='user-login')
def guest_confirmation(request):
    #Get Guest Details
    guest_details = Guest.objects.get(guest_name=request.user)
    #Get Guest PIN from Guest Table
    guest_pin = guest_details.pin
    #Get Guest PIN from PIN Table for  Event Details
    user_event_pin = Pin.objects.get(value=guest_pin) 
   
    #Get the Guest Registered Event Name through the ticket table
    event = user_event_pin.ticket.event
    #Get the Event Date through the Ticket and Event Table
    event_date = user_event_pin.ticket.event.date

    #Get Event Venue
    venue= user_event_pin.ticket.event.event_venue

    #Get Event Logo
    event_logo = user_event_pin.ticket.event.event_logo
    

    #get Ticket Price through ticket Table
    ticket_price = user_event_pin.ticket.price

    #Get Guest Drinks
    guest_drinks = Drink.objects.get(user=request.user)

    drinks = guest_drinks.guest_drink

    context = {
        'pin':guest_pin,
        'event':event,
        'event_date':event_date,
        'event_logo':event_logo,
        'venue':venue,
        'ticket_price':ticket_price,
        'drinks':drinks,
        
    }

    return render(request, 'user/confirmation.html', context)

    