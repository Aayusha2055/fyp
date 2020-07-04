# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    location = models.CharField(max_length=255,  null=True)
    phone = models.CharField(max_length=255,  null=True)


class products(models.Model):
    name = models.CharField(max_length=50)
    stock = models.CharField(max_length=30)
    price = models.CharField(max_length=60)
    ratings = models.CharField(max_length=2)



    def __str__(self):
        return self.name


# class Profile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL)
#     dob = models.DateField(blank=True, null=True)


class Observation(models.Model):
    station = models.CharField(max_length=255,  null=True)
    max_temp = models.CharField(max_length=255, null=True)
    mini_temp = models.CharField(max_length=255, null=True)
    rainfall_mm = models.FloatField(max_length=255, null=True)
    status = models.CharField(max_length=255, null=True)