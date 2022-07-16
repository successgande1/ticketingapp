from django.contrib import admin
from . models import *

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'date', 'event_venue', 'event_logo', 'added_date')
    list_per_page = 25

#Event Table
admin.site.register(Event, EventAdmin)


class TicketAdmin(admin.ModelAdmin):
    list_display = ('event', 'price', 'category', 'added_date')
    list_per_page = 25

#Ticket Table
admin.site.register(Ticket, TicketAdmin)

class PinAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'value', 'added', 'reference', 'status')
    list_per_page = 25
#Pin Table
admin.site.register(Pin, PinAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'surname', 'othernames', 'gender', 'phone', 'image')
    list_per_page = 25
#Profile Table
admin.site.register(Profile, ProfileAdmin)


#List Guest In Admin Table
class GuestAdmin(admin.ModelAdmin):
    list_display = ('guest_name', 'pin')
    list_per_page = 25

#Register Guest Model
admin.site.register(Guest, GuestAdmin)




  
   

admin.site.register(Drink)







    