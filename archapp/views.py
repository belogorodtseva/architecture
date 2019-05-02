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
from itertools import chain

def index(request):
    content = {
        'Images' : HomeImage.objects.all().order_by('number'),
        'People' : People.objects.all().order_by('number'),
    }
    return render(request, 'ua/home.html', content)

def projects(request):
    projects = sorted(chain(BuildingProject.objects.all(), InteriorProject.objects.all(), FloatingProject.objects.all()),
                    key=lambda instance: instance.date)
    content = {
        'Project' : projects,
    }

    return render(request, 'ua/projects.html', content)

def project(request, category, pk):
    if category=='building':
        project = BuildingProject.objects.filter(pk=pk)
        images = BuildingImage.objects.all().filter(project=pk)
    elif category=='interior':
        project = InteriorProject.objects.filter(pk=pk)
        images = InteriorImage.objects.all().filter(project=pk)
    else:
        project = FloatingProject.objects.filter(pk=pk)
        images = FloatingImage.objects.all().filter(project=pk)
    content = {
        'Project' : project,
        'Images' : images,
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

##################################     ru

def ruindex(request):
    content = {
        'Images' : HomeImage.objects.all().order_by('number'),
        'People' : People.objects.all().order_by('number'),
    }
    return render(request, 'ru/ruhome.html', content)

def ruprojects(request):
    projects = sorted(chain(BuildingProject.objects.all(), InteriorProject.objects.all(), FloatingProject.objects.all()),
                    key=lambda instance: instance.date)
    content = {
        'Project' : projects,
    }

    return render(request, 'ru/ruprojects.html', content)

def ruproject(request, category, pk):
    if category=='building':
        project = BuildingProject.objects.filter(pk=pk)
        images = BuildingImage.objects.all().filter(project=pk)
    elif category=='interior':
        project = InteriorProject.objects.filter(pk=pk)
        images = InteriorImage.objects.all().filter(project=pk)
    else:
        project = FloatingProject.objects.filter(pk=pk)
        images = FloatingImage.objects.all().filter(project=pk)
    content = {
        'Project' : project,
        'Images' : images,
    }
    return render(request, 'ru/ruproject.html', content)


def rucontact(request):
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
    return render(request, 'ru/rucontact.html', content)


##################################     en

def enindex(request):
    content = {
        'Images' : HomeImage.objects.all().order_by('number'),
        'People' : People.objects.all().order_by('number')
    }
    return render(request, 'en/enhome.html', content)

def enprojects(request):
    projects = sorted(chain(BuildingProject.objects.all(), InteriorProject.objects.all(), FloatingProject.objects.all()),
                    key=lambda instance: instance.date)
    content = {
        'Project' : projects,
    }

    return render(request, 'en/enprojects.html', content)

def enproject(request, category, pk):
    if category=='building':
        project = BuildingProject.objects.filter(pk=pk)
        images = BuildingImage.objects.all().filter(project=pk)
    elif category=='interior':
        project = InteriorProject.objects.filter(pk=pk)
        images = InteriorImage.objects.all().filter(project=pk)
    else:
        project = FloatingProject.objects.filter(pk=pk)
        images = FloatingImage.objects.all().filter(project=pk)
    content = {
        'Project' : project,
        'Images' : images,
    }
    return render(request, 'en/enproject.html', content)


def encontact(request):
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
    return render(request, 'en/encontact.html', content)
