from email import message
from django.forms import ModelForm, Textarea, EmailField
from .models import ContactMe
from django import forms
from captcha.fields import ReCaptchaField
class ContactForm(ModelForm):
    human = ReCaptchaField(label = 'My sites are for humans')
    
    class Meta:
        model = ContactMe
        fields = '__all__'
        
        labels = {
            'message': "Project details",
        }