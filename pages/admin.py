from django.contrib import admin

# Register your models here.

from .models import Category, Message, Room

admin.site.register(Room)
admin.site.register(Category)
admin.site.register(Message)