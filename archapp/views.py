# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from archapp.models import *

def index(request):
    return render(request, 'ua/home.html')

def archprojects(request):
    content = {
        'Projects' : Project.objects.all().order_by('name_ua'),
    }
    return render(request, 'ua/archprojects.html', content)

def designprojects(request):
    content = {
        'Projects' : Project.objects.all().order_by('name_ua'),
    }
    return render(request, 'ua/designprojects.html', content)

def archproject(request, pk):
    content = {

    }
    return render(request, 'ua/project.html', content)

def designproject(request, pk):
    content = {

    }
    return render(request, 'ua/project.html', content)

def contact(request):
    content = {

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
