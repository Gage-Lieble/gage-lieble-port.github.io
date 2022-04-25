from email import message
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ContactMe
from django.urls import reverse
from django import forms
from .forms import ContactForm
# from django.core.mail import send_mail
# Create your views here.

def index(request):
    form = ContactForm()
    
    return render(request, 'portfolio_app/index.html', {'form': form})

def handle_not_found(request, exception):
    return render(request, 'portfolio_app/404.html')

def submitted(request):
        if request.method == 'POST':
            # user_mail = request.POST['email']
            # user_msg = request.POST['message']
            form = ContactForm(request.POST)
            if 'bot' in str(form).lower() or 'robot' in str(form).lower() or 'bucks' in str(form).lower():
                return render(request, 'portfolio_app/contacterror.html')
            elif form.is_valid():
                form.save()
            
        #     send_mail(
        #         'Portfolio Contact',
        #         f"From {user_mail}: {user_msg}",
        #         user_mail,
        #         ['My_email'], 
        #         fail_silently=False,
        #     )
                return render(request, 'portfolio_app/contact_sub.html')