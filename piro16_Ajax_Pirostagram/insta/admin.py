from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'status']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['content']