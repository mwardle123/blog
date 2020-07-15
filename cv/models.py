from django.conf import settings
from django.db import models
from django.utils import timezone
from abc import ABC, abstractmethod
from django.db.models import TextField, Model, DateTimeField

class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class CV(models.Model):
    title = models.CharField(max_length=200, default='CV')
    name = models.CharField(max_length=200)
    addresses = models.TextField()
    mobile_number = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    personal_profile = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Item(models.Model):
    category = models.ForeignKey('cv.Category', related_name='items', on_delete=models.CASCADE, default='')
    text = models.TextField()

    def __str__(self):
        return self.text