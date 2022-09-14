"""ticketingapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from user import views as user_views
from pages import views as pages_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('about/', pages_views.about, name = 'pages-about'),
    path('services/', pages_views.services, name = 'pages-services'),
    path('contact/', pages_views.contact, name = 'pages-contact'), 
    path('buy/ticket/', pages_views.buy_ticket, name ='pages-buy-tickets'), 
    path('users/', include('dashboard.urls')),
    path('register/', user_views.register, name = 'user-register'),
    path('guest/register/', user_views.register_guest, name = 'register-guest'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name = 'user-login'),
    path('profile/', user_views.profile, name = 'user-profile'),
    path('profile/update/', user_views.profile_update, name = 'user-profile-update'),
    path('guest/add/drink/', user_views.Guest_Add_Drink, name = 'user-add-drink'), 
    path('guest/confirm/register/', user_views.guest_confirmation, name = "guest-confirmation"),
    path('event/add/', user_views.EventCreateView.as_view(), name = 'create-event'),
    path('event/list/', user_views.EventListView.as_view(), name='event-list'),
    path('delete/event/<int:event_id>', user_views.delete_event, name ='delete-event'),
    path('ticket/add/', user_views.TicketCreateView.as_view(), name = 'create-ticket'),
    # path('ticket/list/', user_views.TicketListView.as_view(), name='ticket-list'),
    path('list/tickets/', user_views.Ticket_list, name = 'list-ticket'),
    path("generate-pins/<int:ticket_id>", user_views.generate_pins_for_ticket, name="generate-pin"),
    path('activate/', user_views.pin_activation, name = 'pin-activation'), 
    path('pin/list/', user_views.PinListView.as_view(), name='pin-list'),
    path('list/pin/', user_views.Pin_Search_List, name = 'list-pin'),
    path('generated/pdf/pins/', user_views.GeneratePdf.as_view(), name = 'pdf-pins'),
    path('staff/list/', user_views.UserListView.as_view(), name='staff-list'), 
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name = 'user-logout'),
]+ static ( settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
