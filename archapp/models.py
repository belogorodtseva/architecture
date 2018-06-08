# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime
from datetime import datetime

###### InteriorType #####

class InteriorType(models.Model):

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


###### BuildingsType #####

class BuildingType(models.Model):

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

###### FloatingType #####

class FloatingType(models.Model):

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


###### BuildingsProject #####

class BuildingProject(models.Model):

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

    text_en = models.TextField(max_length=500,blank=True, null=True)
    text_ru = models.TextField(max_length=500,blank=True, null=True)
    text_ua = models.TextField(max_length=500,blank=True, null=True)

    year = models.CharField(max_length=9,blank=True, null=True)

    img = models.FileField(blank=True, null=True)


    type = models.ForeignKey(BuildingType, blank=True, null=True)

    date = models.DateTimeField(default=datetime.now(), null=False, blank=False)
    active = models.BooleanField(default=True)

    category = 'building'


    def __unicode__(self):
        return '%s - %s - %s' % (unicode(self.name_en), unicode(self.name_ru), unicode(self.name_ua))

###### InteriorProject #####

class InteriorProject(models.Model):

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

    text_en = models.TextField(max_length=500,blank=True, null=True)
    text_ru = models.TextField(max_length=500,blank=True, null=True)
    text_ua = models.TextField(max_length=500,blank=True, null=True)

    year = models.CharField(max_length=9,blank=True, null=True)

    img = models.FileField(blank=False, null=False)

    type = models.ForeignKey(InteriorType, blank=True, null=True)

    date = models.DateTimeField(default=datetime.now(), null=False, blank=False)
    active = models.BooleanField(default=True)

    category = 'interior'


    def __unicode__(self):
        return '%s - %s - %s' % (unicode(self.name_en), unicode(self.name_ru), unicode(self.name_ua))

###### FloatingProject #####

class FloatingProject(models.Model):

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

    text_en = models.TextField(max_length=500,blank=True, null=True)
    text_ru = models.TextField(max_length=500,blank=True, null=True)
    text_ua = models.TextField(max_length=500,blank=True, null=True)

    year = models.CharField(max_length=9,blank=True, null=True)

    img = models.FileField(blank=True, null=True)


    type = models.ForeignKey(FloatingType, blank=True, null=True)

    date = models.DateTimeField(default=datetime.now(), null=False, blank=False)
    active = models.BooleanField(default=True)

    category = 'floating'


    def __unicode__(self):
        return '%s - %s - %s' % (unicode(self.name_en), unicode(self.name_ru), unicode(self.name_ua))


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


###### Home-photo #####

class HomeImage(models.Model):
   number = models.IntegerField(default=1)
   img = models.FileField(blank=False, null=False)

   def __str__(self):
        return "# " + str(self.number)


# ###### Home-project #####

# class HomeProject(models.Model):
#    number = models.IntegerField(default=1)
#    project = models.ForeignKey(Project, on_delete=models.CASCADE)
#    img = models.FileField(blank=False, null=False)
#
#    def __unicode__(self):
#         return "# " + str(self.number) + " - " + unicode(self.buildingProject)
