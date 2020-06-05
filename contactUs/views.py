from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.core.mail import EmailMessage
from django.forms import ModelForm
from django.template.loader import get_template

# Create your views here.

# Contact form view

def Contact(request):
    Contact_Form = ContactForm
    if request.method == 'POST':
        form = Contact_Form(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name')
            contact_email = request.POST.get('contact_email')
            contact_content = request.POST.get('content')

            template = get_template('tuber/contact_form.txt')
            context = {
                'contact_name' : contact_name,
                'contact_email' : contact_email,
                'contact_content' : contact_content,
            }
            
            content = template.render(context)

            email = EmailMessage(
                "New contact form email",
                content,
                "Creative web" + '',
                ['victoriawang98@gmail.com'],
                headers = { 'Reply To': contact_email }
            )

            email.send()

            return redirect('tuber:success')
    return render(request, 'tuber/contact.html', {'form':Contact_Form })
