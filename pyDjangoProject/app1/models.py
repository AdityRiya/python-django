from enum import unique
from django.db import models

# Create your models here.






# 1st model creation
class Topic(models.Model):
    top_name = models.CharField(max_length=264,unique=True)
    def __str__(self):
        return self.top_name
    
class Webpage(models.Model):
    topic = models.ForeignKey(
        'Topic',
    on_delete=models.CASCADE,)
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)
    def __str__(self):
        return self.name
class AccessRecord(models.Model):
    name = models.ForeignKey('Webpage',
    on_delete=models.CASCADE,)
    date = models.DateField()
    
    def __str__(self):
        return str(self.date)
    
    
# 2nd model for another page
class Firstname(models.Model):
    first_name = models.CharField(max_length=64,unique=True)
    def __str__(self):
        return self.first_name
class Lastname(models.Model):
    last_name = models.ForeignKey(
        'first_name',
    on_delete=models.CASCADE,)
    name = models.CharField(max_length=64,unique=True)
    url = models.URLField(unique=True)
    def __str__(self):
        return self.name