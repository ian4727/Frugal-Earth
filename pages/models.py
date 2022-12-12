#from unicodedata import category
#from unittest.util import _MAX_LENGTH
#from pages.views import room
from django.db import models
from django.contrib.auth.models import AbstractUser

<<<<<<< HEAD

=======
>>>>>>> 840bf37d3ca46419406fb7ae06d5a6d9ec637024
# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
<<<<<<< HEAD
    email = models.EmailField(unique=True, default='')
    avatar = models.ImageField(null=True, default="defaultDp.jpg")



=======
    email = models.EmailField(unique=True, null=True)
    avatar = models.ImageField(null=True, default="defaultDp.jpg")
    
    
>>>>>>> 840bf37d3ca46419406fb7ae06d5a6d9ec637024
    REQUIRED_FIELDS = []



class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
<<<<<<< HEAD
=======
    price = models.CharField(max_length=200)
>>>>>>> 840bf37d3ca46419406fb7ae06d5a6d9ec637024
    location = models.CharField(max_length=200)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    #category = models.ForeignKey(to='consult.Question')
    quantity = models.CharField(max_length=200)
    condition = models.CharField(max_length=200)
    image = models.ImageField(null=True,blank=True)
    notes = models.TextField(null=True, blank=True)
<<<<<<< HEAD
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    price = models.CharField(max_length=200)


=======
    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
        
>>>>>>> 840bf37d3ca46419406fb7ae06d5a6d9ec637024
    class Meta:
       ordering = ['-updated', '-created']
    #*Category(Dropdown: Apparels, Kitchenwares, Household tools, Ornamental items, Electronics, Reading Materials, Stationary Products, Consumables, Furniture, Others
    #Photo
    def __str__ (self):
        return self.name
        #return str(self.title)

<<<<<<< HEAD


class Category(models.Model):
=======
   
     
class Category(models.Model):   
>>>>>>> 840bf37d3ca46419406fb7ae06d5a6d9ec637024
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]
<<<<<<< HEAD



class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.ForeignKey('Reason', on_delete=models.SET_NULL, null=True)
    reportmsg = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.reportmsg


class Reason(models.Model):
    reasonname = models.CharField(max_length=200)

    def __str__ (self):
        return self.reasonname
=======
>>>>>>> 840bf37d3ca46419406fb7ae06d5a6d9ec637024
