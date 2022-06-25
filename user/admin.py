from django.contrib import admin
from . models import *

# Register your models here.

#Event Table
admin.site.register(Event)

#Ticket Table
admin.site.register(Ticket)

#Pin Table
admin.site.register(Pin)

#Profile Table
admin.site.register(Profile)
