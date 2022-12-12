from django.contrib import admin

# Register your models here.

<<<<<<< HEAD
from .models import Category, Message, Room, User, Report, Reason
=======
from .models import Category, Message, Room, User
>>>>>>> 840bf37d3ca46419406fb7ae06d5a6d9ec637024

admin.site.register(User)
admin.site.register(Room)
admin.site.register(Category)
admin.site.register(Message)
<<<<<<< HEAD
admin.site.register(Report)
admin.site.register(Reason)
=======
>>>>>>> 840bf37d3ca46419406fb7ae06d5a6d9ec637024
