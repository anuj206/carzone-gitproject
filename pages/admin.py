from django.contrib import admin
from django.utils.html import format_html

from .models import Team
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 40px" />'.format(object.photo.url))
    thumbnail.short_description = 'Photo'

    list_display = ('id', 'thumbnail' ,'first_name', 'designation', 'created_at')
    list_display_links = ('first_name', 'id', 'thumbnail')
    search_fields = ('first_name', 'last_name', 'designation')
    list_filter = ('designation',)

admin.site.register(Team, TeamAdmin)
