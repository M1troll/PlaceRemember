from django.contrib import admin

from .models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    list_display_links = ('user',)
    search_fields = ('user', 'image_url',)


class ImpressionAdmin(admin.ModelAdmin):
    list_display = ('title', 'lon', 'lat', 'author',)
    list_display_links = ('title', 'lon', 'lat', 'author',)
    search_fields = ('title', 'lon', 'lat', 'author',)


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Impression, ImpressionAdmin)
