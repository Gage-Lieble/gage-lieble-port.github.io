from email import message
from tkinter import Widget
from attr import fields
from django.forms import ModelForm, Textarea, EmailField
from .models import ContactMe
from django import forms
class ContactForm(ModelForm):
    
    class Meta:
        model = ContactMe
        fields = '__all__'
        labels = {
            'message': "Project details"
        }