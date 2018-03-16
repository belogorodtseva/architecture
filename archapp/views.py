# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from archapp.models import Project

def index(request):
    return render(request, 'home.html')

def projects(request):
    content = {
        'Projects' : Project.objects.all().order_by('name_en'),
    }
    return render(request, 'projects.html', content)

def contact(request):
    content = {

    }
    return render(request, 'contact.html', content)
