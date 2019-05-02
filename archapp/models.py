# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime
from datetime import datetime

###### BuildingsProject #####

class BuildingProject(models.Model):

    title_en = models.CharField(max_length=40,blank=True, null=True)
    title_ru = models.CharField(max_length=40,blank=True, null=True)
    title_ua = models.CharField(max_length=40,blank=True, null=True)
    description_en = models.TextField(max_length=150,blank=True, null=True)
    description_ru = models.TextField(max_length=150,blank=True, null=True)
    description_ua = models.TextField(max_length=150,blank=True, null=True)

    name_en = models.CharField(max_length=100, null=False, blank=False)
    name_ru = models.CharField(max_length=100, null=False, blank=False)
    name_ua = models.CharField(max_length=100, null=False, blank=False)

    location_en = models.CharField(max_length=200,blank=True, null=True)
    location_ru = models.CharField(max_length=200,blank=True, null=True)
    location_ua = models.CharField(max_length=200,blank=True, null=True)

    architectors_en = models.CharField(max_length=400,blank=True, null=True)
    architectors_ru = models.CharField(max_length=400,blank=True, null=True)
    architectors_ua = models.CharField(max_length=400,blank=True, null=True)

    photo_en = models.CharField(max_length=200,blank=True, null=True)
    photo_ru = models.CharField(max_length=200,blank=True, null=True)
    photo_ua = models.CharField(max_length=200,blank=True, null=True)

    text_en = models.TextField(max_length=500,blank=True, null=True)
    text_ru = models.TextField(max_length=500,blank=True, null=True)
    text_ua = models.TextField(max_length=500,blank=True, null=True)

    year_en = models.CharField(max_length=100,blank=True, null=True)
    year_ru = models.CharField(max_length=100,blank=True, null=True)
    year_ua = models.CharField(max_length=100,blank=True, null=True)

    img = models.FileField(blank=False, null=False)

    date = models.DateTimeField(default=datetime.now(), null=False, blank=False)
    active = models.BooleanField(default=True)

    category = 'building'


    def __str__(self):
        return '%s - %s - %s' % (str(self.name_en), str(self.name_ru), str(self.name_ua))

###### InteriorProject #####

class InteriorProject(models.Model):

    title_en = models.CharField(max_length=40,blank=True, null=True)
    title_ru = models.CharField(max_length=40,blank=True, null=True)
    title_ua = models.CharField(max_length=40,blank=True, null=True)
    description_en = models.TextField(max_length=150,blank=True, null=True)
    description_ru = models.TextField(max_length=150,blank=True, null=True)
    description_ua = models.TextField(max_length=150,blank=True, null=True)

    name_en = models.CharField(max_length=100, null=False, blank=False)
    name_ru = models.CharField(max_length=100, null=False, blank=False)
    name_ua = models.CharField(max_length=100, null=False, blank=False)

    location_en = models.CharField(max_length=200,blank=True, null=True)
    location_ru = models.CharField(max_length=200,blank=True, null=True)
    location_ua = models.CharField(max_length=200,blank=True, null=True)

    architectors_en = models.CharField(max_length=400,blank=True, null=True)
    architectors_ru = models.CharField(max_length=400,blank=True, null=True)
    architectors_ua = models.CharField(max_length=400,blank=True, null=True)

    photo_en = models.CharField(max_length=200,blank=True, null=True)
    photo_ru = models.CharField(max_length=200,blank=True, null=True)
    photo_ua = models.CharField(max_length=200,blank=True, null=True)

    text_en = models.TextField(max_length=500,blank=True, null=True)
    text_ru = models.TextField(max_length=500,blank=True, null=True)
    text_ua = models.TextField(max_length=500,blank=True, null=True)

    year_en = models.CharField(max_length=100,blank=True, null=True)
    year_ru = models.CharField(max_length=100,blank=True, null=True)
    year_ua = models.CharField(max_length=100,blank=True, null=True)

    img = models.FileField(blank=False, null=False)

    date = models.DateTimeField(default=datetime.now(), null=False, blank=False)
    active = models.BooleanField(default=True)

    category = 'interior'


    def __str__(self):
        return '%s - %s - %s' % (str(self.name_en), str(self.name_ru), str(self.name_ua))

###### FloatingProject #####

class FloatingProject(models.Model):

    title_en = models.CharField(max_length=40,blank=True, null=True)
    title_ru = models.CharField(max_length=40,blank=True, null=True)
    title_ua = models.CharField(max_length=40,blank=True, null=True)
    description_en = models.TextField(max_length=150,blank=True, null=True)
    description_ru = models.TextField(max_length=150,blank=True, null=True)
    description_ua = models.TextField(max_length=150,blank=True, null=True)

    name_en = models.CharField(max_length=100, null=False, blank=False)
    name_ru = models.CharField(max_length=100, null=False, blank=False)
    name_ua = models.CharField(max_length=100, null=False, blank=False)

    location_en = models.CharField(max_length=200,blank=True, null=True)
    location_ru = models.CharField(max_length=200,blank=True, null=True)
    location_ua = models.CharField(max_length=200,blank=True, null=True)

    architectors_en = models.CharField(max_length=400,blank=True, null=True)
    architectors_ru = models.CharField(max_length=400,blank=True, null=True)
    architectors_ua = models.CharField(max_length=400,blank=True, null=True)

    photo_en = models.CharField(max_length=200,blank=True, null=True)
    photo_ru = models.CharField(max_length=200,blank=True, null=True)
    photo_ua = models.CharField(max_length=200,blank=True, null=True)

    text_en = models.TextField(max_length=500,blank=True, null=True)
    text_ru = models.TextField(max_length=500,blank=True, null=True)
    text_ua = models.TextField(max_length=500,blank=True, null=True)

    year_en = models.CharField(max_length=100,blank=True, null=True)
    year_ru = models.CharField(max_length=100,blank=True, null=True)
    year_ua = models.CharField(max_length=100,blank=True, null=True)

    img = models.FileField(blank=False, null=False)

    date = models.DateTimeField(default=datetime.now(), null=False, blank=False)
    active = models.BooleanField(default=True)

    category = 'floating'


    def __str__(self):
        return '%s - %s - %s' % (str(self.name_en), str(self.name_ru), str(self.name_ua))


###### InteriorProjects-photo #####

class InteriorImage(models.Model):
   project = models.ForeignKey(InteriorProject, on_delete=models.CASCADE)
   img = models.FileField(blank=True, null=True)

###### BuildingProjects-photo #####

class BuildingImage(models.Model):
   project = models.ForeignKey(BuildingProject, on_delete=models.CASCADE)
   img = models.FileField(blank=True, null=True)

###### FloatingProjects-photo #####

class FloatingImage(models.Model):
   project = models.ForeignKey(FloatingProject, on_delete=models.CASCADE)
   img = models.FileField(blank=True, null=True)

###### InteriorProjects-Publication #####

class InteriorPublication(models.Model):
   project = models.ForeignKey(InteriorProject, on_delete=models.CASCADE)
   name_en = models.CharField(max_length=100, null=False, blank=False)
   name_ru = models.CharField(max_length=100, null=False, blank=False)
   name_ua = models.CharField(max_length=100, null=False, blank=False)
   link = models.CharField(max_length=300, null=False, blank=False)

###### BuildingProjects-Publication #####

class BuildingPublication(models.Model):
   project = models.ForeignKey(BuildingProject, on_delete=models.CASCADE)
   name_en = models.CharField(max_length=100, null=False, blank=False)
   name_ru = models.CharField(max_length=100, null=False, blank=False)
   name_ua = models.CharField(max_length=100, null=False, blank=False)
   link = models.CharField(max_length=300, null=False, blank=False)

###### FloatingProjects-Publication #####

class FloatingPublication(models.Model):
   project = models.ForeignKey(FloatingProject, on_delete=models.CASCADE)
   name_en = models.CharField(max_length=100, null=False, blank=False)
   name_ru = models.CharField(max_length=100, null=False, blank=False)
   name_ua = models.CharField(max_length=100, null=False, blank=False)
   link = models.CharField(max_length=300, null=False, blank=False)


###### Home-photo #####

class HomeImage(models.Model):
   number = models.IntegerField(default=1)
   img = models.FileField(blank=False, null=False)

   def __str__(self):
        return "# " + str(self.number)


###### People-photo #####

class People(models.Model):
   number = models.IntegerField(default=1)
   img = models.FileField(blank=False, null=False)
   name_en = models.CharField(max_length=100, null=False, blank=False)
   name_ru = models.CharField(max_length=100, null=False, blank=False)
   name_ua = models.CharField(max_length=100, null=False, blank=False)

   def __str__(self):
        return "# " + str(self.number)
