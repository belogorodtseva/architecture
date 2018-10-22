# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin


from archapp.models import *


admin.site.register(HomeImage)

admin.site.register(BuildingType)
admin.site.register(InteriorType)
admin.site.register(FloatingType)

class BuildingImageInline(admin.TabularInline):
    model = BuildingImage

class BuildingPublicationInline(admin.TabularInline):
    model = BuildingPublication

class BuildingProjectAdmin(admin.ModelAdmin):
    inlines = [
        BuildingImageInline,
        BuildingPublicationInline
    ]

class InteriorImageInline(admin.TabularInline):
    model = InteriorImage

class InteriorPublicationInline(admin.TabularInline):
    model = InteriorPublication

class InteriorProjectAdmin(admin.ModelAdmin):
    inlines = [
        InteriorImageInline,
        InteriorPublicationInline
    ]

class FloatingImageInline(admin.TabularInline):
    model = FloatingImage

class FloatingPublicationInline(admin.TabularInline):
    model = FloatingPublication

class FloatingProjectAdmin(admin.ModelAdmin):
    inlines = [
        FloatingImageInline,
        FloatingPublicationInline
    ]

admin.site.register(BuildingProject, BuildingProjectAdmin)
admin.site.register(BuildingImage)
admin.site.register(BuildingPublication)

admin.site.register(InteriorProject, InteriorProjectAdmin)
admin.site.register(InteriorImage)
admin.site.register(InteriorPublication)

admin.site.register(FloatingProject, FloatingProjectAdmin)
admin.site.register(FloatingImage)
admin.site.register(FloatingPublication)
