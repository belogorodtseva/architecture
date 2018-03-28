# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from archapp.models import Project

def index(request):
    return render(request, 'home.html')

def archprojects(request):
    content = {
        'Projects' : Project.objects.all().order_by('name_ua'),
    }
    return render(request, 'archprojects.html', content)

def designprojects(request):
    content = {
        'Projects' : Project.objects.all().order_by('name_ua'),
    }
    return render(request, 'designprojects.html', content)

def archproject(request, pk):
    content = {

    }
    return render(request, 'project.html', content)

def designproject(request, pk):
    content = {

    }
    return render(request, 'project2.html', content)

def contact(request):
    content = {

    }
    return render(request, 'contact.html', content)

def services(request):
    content = {

    }
    return render(request, 'services.html', content)

### ru

def ruindex(request):
    return render(request, 'ruhome.html')

def ruarchprojects(request):
    content = {
        'Projects' : Project.objects.all().order_by('name_ru'),
    }
    return render(request, 'ruarchprojects.html', content)

def rudesignprojects(request):
    content = {
        'Projects' : Project.objects.all().order_by('name_ru'),
    }
    return render(request, 'rudesignprojects.html', content)

def rucontact(request):
    content = {

    }
    return render(request, 'rucontact.html', content)

def ruservices(request):
    content = {

    }
    return render(request, 'ruservices.html', content)


### en

def enindex(request):
    return render(request, 'enhome.html')

def enarchprojects(request):
    content = {
        'Projects' : Project.objects.all().order_by('name_en'),
    }
    return render(request, 'enarchprojects.html', content)

def endesignprojects(request):
    content = {
        'Projects' : Project.objects.all().order_by('name_en'),
    }
    return render(request, 'endesignprojects.html', content)

def encontact(request):
    content = {

    }
    return render(request, 'encontact.html', content)

def enservices(request):
    content = {

    }
    return render(request, 'enservices.html', content)
