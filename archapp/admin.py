# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin


from archapp.models import *


admin.site.register(HomeImage)
# admin.site.register(HomeProject)
admin.site.register(BuildingType)
admin.site.register(InteriorType)
admin.site.register(FloatingType)

class BuildingImageInline(admin.TabularInline):
    model = BuildingImage

class BuildingProjectAdmin(admin.ModelAdmin):
    inlines = [
        BuildingImageInline,
    ]

class InteriorImageInline(admin.TabularInline):
    model = InteriorImage

class InteriorProjectAdmin(admin.ModelAdmin):
    inlines = [
        InteriorImageInline,
    ]

class FloatingImageInline(admin.TabularInline):
    model = FloatingImage

class FloatingProjectAdmin(admin.ModelAdmin):
    inlines = [
        FloatingImageInline,
    ]

admin.site.register(BuildingProject, BuildingProjectAdmin)
admin.site.register(BuildingImage)

admin.site.register(InteriorProject, InteriorProjectAdmin)
admin.site.register(InteriorImage)

admin.site.register(FloatingProject, FloatingProjectAdmin)
admin.site.register(FloatingImage)
