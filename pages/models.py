from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=200)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    quantity = models.CharField(max_length=200)
    condition = models.CharField(max_length=200)
    image = models.ImageField(null=True,blank=True)
    notes = models.TextField(max_length=1000)
        
    
    #*Category(Dropdown: Apparels, Kitchenwares, Household tools, Ornamental items, Electronics, Reading Materials, Stationary Products, Consumables, Furniture, Others
    #Photo
    
    created = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.title



class Category(models.Model):   
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title