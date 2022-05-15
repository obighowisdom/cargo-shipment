from django.db import models

# Create your models here.
from django.utils.text import slugify


class cons(models.Model):
    caption = models.CharField(max_length=200)
    true = models.CharField(max_length=200)
    trac_one = models.CharField(max_length=200)
    def __str__(self):
        return self.caption


# comment

class comment(models.Model):
    name = models.CharField(max_length=200)
    comments = models.CharField(max_length=1000)
    def __str__(self):
        return self.name

# location
class location(models.Model):
    status = models.CharField(max_length=200)
    previous_location = models.CharField(max_length=200)
    current_location = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    delivery_date = models.CharField(max_length=200)
    map = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.status


class location_two(models.Model):
    status = models.CharField(max_length=200)
    previous_location = models.CharField(max_length=200)
    current_location = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    delivery_date = models.CharField(max_length=200)
    map = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.status
