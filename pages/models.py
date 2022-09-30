from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    quantity = models.SmallIntegerField(max_length=200)
    size = models.CharField (max_length=200)
    condition = models.CharField(max_length=200)
    notes = models.CharField(max_length=1000)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
        
    
    #*Category(Dropdown: Apparels, Kitchenwares, Household tools, Ornamental items, Electronics, Reading Materials, Stationary Products, Consumables, Furniture, Others
    #Photo
    
    created = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.title

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    posts = models.ForeignKey(Posts, on_delete=models.SET_NULL, null=True)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]

class Category(models.Model):   
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title