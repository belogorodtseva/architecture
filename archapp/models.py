# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime
from datetime import datetime

###### ArchProjects-type #####

class ArchitectureType(models.Model):

    title_en = models.CharField(max_length=40,blank=True, null=True)
    title_ru = models.CharField(max_length=40,blank=True, null=True)
    title_ua = models.CharField(max_length=40,blank=True, null=True)
    description_en = models.TextField(max_length=150,blank=True, null=True)
    description_ru = models.TextField(max_length=150,blank=True, null=True)
    description_ua = models.TextField(max_length=150,blank=True, null=True)

    name_en = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=100)
    name_ua = models.CharField(max_length=100)


    def __unicode__(self):
        return '%s' % (unicode(self.name_en))


###### DesignProjects-type #####

class DesignType(models.Model):

    title_en = models.CharField(max_length=40,blank=True, null=True)
    title_ru = models.CharField(max_length=40,blank=True, null=True)
    title_ua = models.CharField(max_length=40,blank=True, null=True)
    description_en = models.TextField(max_length=150,blank=True, null=True)
    description_ru = models.TextField(max_length=150,blank=True, null=True)
    description_ua = models.TextField(max_length=150,blank=True, null=True)

    name_en = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=100)
    name_ua = models.CharField(max_length=100)


    def __unicode__(self):
        return '%s' % (unicode(self.name_en))


###### ArchProjects #####

class ArchitectureProject(models.Model):

    title_en = models.CharField(max_length=40,blank=True, null=True)
    title_ru = models.CharField(max_length=40,blank=True, null=True)
    title_ua = models.CharField(max_length=40,blank=True, null=True)
    description_en = models.TextField(max_length=150,blank=True, null=True)
    description_ru = models.TextField(max_length=150,blank=True, null=True)
    description_ua = models.TextField(max_length=150,blank=True, null=True)

    name_en = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=100)
    name_ua = models.CharField(max_length=100)

    location_en = models.CharField(max_length=200,blank=True, null=True)
    location_ru = models.CharField(max_length=200,blank=True, null=True)
    location_ua = models.CharField(max_length=200,blank=True, null=True)

    year = models.CharField(max_length=9,blank=True, null=True)

    img = models.FileField(blank=True, null=True)


    type = models.ForeignKey(ArchitectureType, on_delete=models.CASCADE)

    date = models.DateTimeField(default=datetime.now(), null=False, blank=False)
    active = models.BooleanField(default=True)


    def __unicode__(self):
        return '%s - %s - %s' % (unicode(self.name_en), unicode(self.name_ru), unicode(self.name_ua))

###### DesignProjects #####

class DesignProject(models.Model):

    title_en = models.CharField(max_length=40,blank=True, null=True)
    title_ru = models.CharField(max_length=40,blank=True, null=True)
    title_ua = models.CharField(max_length=40,blank=True, null=True)
    description_en = models.TextField(max_length=150,blank=True, null=True)
    description_ru = models.TextField(max_length=150,blank=True, null=True)
    description_ua = models.TextField(max_length=150,blank=True, null=True)

    name_en = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=100)
    name_ua = models.CharField(max_length=100)

    location_en = models.CharField(max_length=200,blank=True, null=True)
    location_ru = models.CharField(max_length=200,blank=True, null=True)
    location_ua = models.CharField(max_length=200,blank=True, null=True)

    year = models.CharField(max_length=9,blank=True, null=True)

    img = models.FileField(blank=True, null=True)

    type = models.ForeignKey(DesignType, on_delete=models.CASCADE)

    date = models.DateTimeField(default=datetime.now(), null=False, blank=False)
    active = models.BooleanField(default=True)


    def __unicode__(self):
        return '%s - %s - %s' % (unicode(self.name_en), unicode(self.name_ru), unicode(self.name_ua))

###### ArchProjects-photo #####

class ArchitectureImage(models.Model):
   project = models.ForeignKey(ArchitectureProject, on_delete=models.CASCADE)
   img = models.FileField(blank=True, null=True)

###### DesignProjects-photo #####

class DesignImage(models.Model):
   project = models.ForeignKey(DesignProject, on_delete=models.CASCADE)
   img = models.FileField(blank=True, null=True)


###### Home-photo #####

class HomeImage(models.Model):
   number = models.IntegerField(default=1)
   img = models.FileField(blank=False, null=False)

   def __int__(self):
        return str(self.number)
