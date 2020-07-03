# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

# Create your models here.

class products(models.Model):
    name = models.CharField(max_length=50)
    stock = models.CharField(max_length=30)
    price = models.CharField(max_length=60)
    ratings = models.CharField(max_length=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Products"

class Profile(models.Model):
    user = models.onetoonefield(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.IntegerField(max_length=10, null=True)

    def __str__(self):
        return self.phone_number


class Observation(models.Model):
    station = models.CharField(max_length=255,  null=True)
    max_temp = models.CharField(max_length=255, null=True)
    mini_temp = models.CharField(max_length=255, null=True)
    rainfall_mm = models.FloatField(max_length=255, null=True)
    status = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.station

class Alert(models.Model):
    location = models.CharField(max_length=255,  null=True)
    number = models.CharField(max_length=255,  null=True)
    housenum = models.CharField(max_length=255,  null=True)
    info = models.CharField(max_length=255,  null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.housenum