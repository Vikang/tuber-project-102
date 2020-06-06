from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404, HttpResponseRedirect
from django.urls import reverse

from .forms import ContactForm

from django.core.mail import EmailMessage
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.template.loader import get_template

# Create your views here.

# Contact form view

def contact(request):
    Contact_form = ContactForm
    if request.method == 'POST':
        form = Contact_form(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name')
            contact_email = request.POST.get('contact_email')
            contact_message = request.POST.get('contact_message')
            
            template = get_template('contactUs/contact_form.txt')
            
            context = {
                'contact_name' : contact_name,
                'contact_email' : contact_email,
                'contact_message' : contact_message,
            }

            content = template.render(context)
            #send email
            email = EmailMessage (
                "New contact from " + contact_name, #subject
                content, #message
                contact_email, #from email
                ['victoriawang98@gmail.com'], #to email
                headers = { 'Reply To': contact_email }
            )

            email.send() 
            return render(request, 'contactUs/sendingcontact.html')
    return render(request, 'contactUs/contact.html', {'form':Contact_form})

# Contact received
def contact_received(request):
    #HelpRequest.user = request.user
    return render(request, 'contactUs/sendingcontact.html')
