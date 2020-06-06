from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404, HttpResponseRedirect
from django.urls import reverse

from .forms import ContactForm

from django.core.mail import EmailMessage
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User

# Create your views here.

# Contact form view

def contact(request):
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

            return render(request, 'request_help/sendinghelp.html')
    return render(request, 'contactUs/contact.html', {'form':Contact_Form })

# Contact received
def contact_received(request):
    #HelpRequest.user = request.user
    return render(request, 'contactUs/sendingcontact.html')
