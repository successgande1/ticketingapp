from datetime import datetime
from unicodedata import category
from django.db import models
from django.urls import reverse
from PIL import Image
from phonenumber_field.modelfields import PhoneNumberField
from random import randint
import uuid
from django.contrib.auth.models import User, Group

# Create your models here.

#Ticket Category Choices
PAYMENT = (
    ('RECHARGE PIN', 'RECHARGE PIN'),
    ('DIRECT PAYMENT', 'DIRECT PAYMENT'),
)

ACTIVATION = (
    ('ACTIVATED', 'ACTIVATED'),
    ('NOT ACTIVATED', 'NOT ACTIVATED'),
)

GENDER = (
	('Male', 'Male'),
	('Female', 'Female'),
)


class Profile(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE, null = True)
    surname = models.CharField(max_length=20, null=True)
    othernames = models.CharField(max_length=40, null=True)
    gender = models.CharField(max_length=6, choices=GENDER, blank=True, null=True)
    phone = PhoneNumberField()
    image = models.ImageField(default='avatar.jpg', blank=False, null=False, upload_to ='profile_images', 
   
    )
    

    #Method to save Image
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
    #Check for Image Height and Width then resize it then save
        if img.height > 200 or img.width > 150:
            output_size = (150, 250)
            img.thumbnail(output_size)
            img.save(self.image.path)
 
    def __str__(self):
        return f'{self.staff.username}-Profile'




#Event Ticket Model
class Event(models.Model):
    event_name = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=False, auto_now=False, null=False)
    event_venue = models.CharField(max_length=200)
    event_logo = models.ImageField(default='avatar.jpg', blank=False, null=False, upload_to ='profile_images')
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.event_name} - Event"

    #Prepare the url path for the Model
    def get_absolute_url(self):
        return reverse("event_detail", args=[str(self.id)])

#Ticket Model
class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    category = models.CharField(max_length=100, choices=PAYMENT, default=None, blank=False, null=False)
    added_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.event} "

    #Prepare the url path for the Model
    def get_absolute_url(self):
        return reverse("ticket-detail", args=[str(self.id)])

def generate_pin():
    return ''.join(str(randint(0, 9)) for _ in range(6))

class Pin(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    value = models.CharField(max_length=6, default=generate_pin, blank=True)
    added = models.DateTimeField(auto_now_add=True,  blank=False)
    reference = models.UUIDField(primary_key = True, editable = False, default=uuid.uuid4)
    status = models.CharField(max_length=20, default='Not Activated')
    #Save Reference Number
    def save(self, *args, **kwargs):
         self.reference == str(uuid.uuid4())
         super().save(*args, **kwargs)

    def __unicode__(self):
        return self.ticket

    class Meta:
        unique_together = ["ticket", "value"]

    def __str__(self):
        return f"{self.ticket} | {self.value}"





    # #Method to save Image
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     img = Image.open(self.image.path)
    # #Check for Image Height and Width then resize it then save
    #     if img.height > 200 or img.width > 150:
    #         output_size = (150, 250)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
    


