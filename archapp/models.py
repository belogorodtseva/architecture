# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

###### Projects #####

class Project(models.Model):
    name_en = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=100)
    name_ua = models.CharField(max_length=50)
    description_en = models.TextField()
    description_ru = models.TextField()
    description_ua = models.TextField()

    def __str__(self):
        return '%s - %s - %s' % (str(self.name_en), str(self.name_ru), str(self.name_ua))
