from dataclasses import fields
from django import forms

class ContactForm(forms.Form):
    name= forms.CharField(max_length=100,label='name')
    email= forms.EmailField()
    content=forms.Textarea()