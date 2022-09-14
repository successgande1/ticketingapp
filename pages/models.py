from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=60, null=True, blank=True)
    email = models.EmailField(max_length=45, null=True, blank=True)
    phone = models.CharField(max_length=18, null=True, blank=True)
    subject = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
