# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin


from archapp.models import *


admin.site.register(HomeImage)
admin.site.register(HomeProject)
admin.site.register(ArchitectureType)
admin.site.register(DesignType)

class ArchitectureImageInline(admin.TabularInline):
    model = ArchitectureImage

class ArchitectureProjectAdmin(admin.ModelAdmin):
    inlines = [
        ArchitectureImageInline,
    ]

class DesignImageInline(admin.TabularInline):
    model = DesignImage

class DesignProjectAdmin(admin.ModelAdmin):
    inlines = [
        DesignImageInline,
    ]


admin.site.register(ArchitectureProject, ArchitectureProjectAdmin)
admin.site.register(ArchitectureImage)

admin.site.register(DesignProject, DesignProjectAdmin)
admin.site.register(DesignImage)
