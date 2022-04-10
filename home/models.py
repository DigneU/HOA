from unittest.util import _MAX_LENGTH
from django.db import models
import email
# Create your models here.

CHOICES= [('slider','slider'),('welcome','welcome'),('homebody','homebody')]
class Page(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.CharField(choices=CHOICES, max_length=255)
    
    def __str__(self):
        return self.title

class Contact(models.Model):
    name= models.CharField(max_length=100)
    email= models.EmailField()
    content= models.TextField()

    def __str__(self):
        #return self.name
        return f'{self.name} With {self.email} said that: {self.content} '

class Room(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to='static/images')
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    user_name = models.CharField(max_length=100)
    user_phone = models.CharField(max_length=16)
    user_email = models.EmailField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    rooms = models.IntegerField(default=1)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()  
    adults = models.IntegerField(default=1)
    children = models.IntegerField(default=0)
    approved = models. BooleanField(default=True)

    def __str__(self):
        return f'{self.user_name} has booked {self.room} from {self.check_in} to {self.check_out} {self.approved}'
