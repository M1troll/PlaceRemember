from django.contrib import admin

from .models import *


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    list_display_links = ('user',)
    search_fields = ('user', 'image_url',)


@admin.register(Impression)
class ImpressionAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'author', 'is_deleted',)
    list_display_links = ('title', 'created_at', 'author', 'is_deleted',)
    search_fields = ('title', 'created_at', 'author', 'is_deleted',)
