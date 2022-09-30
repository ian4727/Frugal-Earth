from django.contrib import admin

# Register your models here.

from .models import Posts, Message, Category

admin.site.register(Posts)
admin.site.register(Message)
admin.site.register(Category)