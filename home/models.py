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