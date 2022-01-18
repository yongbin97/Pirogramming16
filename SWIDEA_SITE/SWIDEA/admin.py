from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Develop)

@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    list_display = ['title', 'rate', 'develop']
    list_display_link =['title']
    search_field = ['title', 'Develop__title']