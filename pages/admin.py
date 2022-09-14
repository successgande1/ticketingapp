from django.contrib import admin

from pages.views import contact
from . models import *
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('date', 'name', 'email', 'phone', 'subject', 'message')
    list_per_page = 25 

admin.site.register(Contact, ContactAdmin)



