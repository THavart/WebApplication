from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


def home(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            content = form.cleaned_data['content']

            send_mail('From ' + email + ': ' + subject,
            content,
            settings.EMAIL_HOST_USER,
            ['TH.Labrecque5@gmail.com'],
            fail_silently=False)

            form.save()
    form = ContactForm()
    return render(request, 'index.html', {'form' : form})
