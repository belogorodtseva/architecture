# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from archapp.models import *
from archapp.forms import ContactForm
from django.conf import settings

from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template

def index(request):
    content = {
        'Images' : HomeImage.objects.all().order_by('number'),
        'Project' : HomeProject.objects.all().order_by('number')[:6],
    }
    xx = HomeProject.objects.all().order_by('number')[:6]
    print(xx[0].archproject.name_en)
    return render(request, 'ua/home.html', content)

def archprojects(request):
    content = {
        'Types' : ArchitectureType.objects.all(),
        'Project' : ArchitectureProject.objects.all().order_by('date'),
    }

    return render(request, 'ua/archprojects.html', content)

def designprojects(request):
    content = {
        'Types' : DesignType.objects.all(),
        'Project' : DesignProject.objects.all().order_by('name_ua'),
    }
    return render(request, 'ua/designprojects.html', content)

def archproject(request, pk):
    content = {
        'Project' : ArchitectureProject.objects.filter(pk=pk),
        'Images' : ArchitectureImage.objects.all().filter(project=pk),
    }
    return render(request, 'ua/project.html', content)

def designproject(request, pk):
    content = {
        'Project' : DesignProject.objects.filter(pk=pk),
        'Images' : DesignImage.objects.all().filter(project=pk),
    }
    return render(request, 'ua/project.html', content)

def contact(request):
    form = ContactForm(request.POST or None)
    print(form)
    if form.is_valid():
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        subject = "Вопрос на сайте"
        message = form.cleaned_data.get('message')
        from_email = settings.EMAIL_HOST_USER
        contact_message= "Name: \n%s \n\nMessage: \n%s \n\n From %s"%(
                name,
                message,
                email)
        send_mail(subject,contact_message,from_email,['chernyatevich@gmail.com'],fail_silently=False)
    content = {
        'form': form,
    }
    return render(request, 'ua/contact.html', content)


def services(request):
    content = {

    }
    return render(request, 'ua/services.html', content)

### ru

def ruindex(request):
    return render(request, 'ru/ruhome.html')

def ruarchprojects(request):
    content = {
        'Projects' : Project.objects.all().order_by('name_ru'),
    }
    return render(request, 'ru/ruarchprojects.html', content)

def rudesignprojects(request):
    content = {
        'Projects' : Project.objects.all().order_by('name_ru'),
    }
    return render(request, 'ru/rudesignprojects.html', content)

def rucontact(request):
    content = {

    }
    return render(request, 'ru/rucontact.html', content)

def ruservices(request):
    content = {

    }
    return render(request, 'ru/ruservices.html', content)


### en

def enindex(request):
    return render(request, 'en/enhome.html')

def enarchprojects(request):
    content = {
        'Projects' : Project.objects.all().order_by('name_en'),
    }
    return render(request, 'en/enarchprojects.html', content)

def endesignprojects(request):
    content = {
        'Projects' : Project.objects.all().order_by('name_en'),
    }
    return render(request, 'en/endesignprojects.html', content)

def encontact(request):
    content = {

    }
    return render(request, 'en/encontact.html', content)

def enservices(request):
    content = {

    }
    return render(request, 'en/enservices.html', content)
