from email.policy import default
from enum import unique
from io import BufferedRandom
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class AppInfo(models.Model):
    name = models.CharField(max_length=50)
    carousel1 = models.ImageField(upload_to='carousel')
    carousel2 = models.ImageField(upload_to='carousel')
    carousel3 = models.ImageField(upload_to='carousel')
    banner = models.ImageField(upload_to='banner')
    logo = models.ImageField(upload_to='logo')
    avatar = models.ImageField(upload_to='dp')
    copyright = models.IntegerField()

    def __str__(self):
        return self.name
    
class Category(models.Model):
    brand = models.CharField( max_length=50)
    pix = models.ImageField(upload_to= 'brandpix')
    description = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.brand

class product(models.Model):
    type = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    seats = models.IntegerField()
    price = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='carpix')
    registered = models.BooleanField()
    upload_at = models.DateTimeField( auto_now_add=True)
    upload_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
        
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=70)
    message = models.TextField()
    sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    