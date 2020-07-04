# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

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

# class Profile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.")
#     phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

#     def __str__(self):
#         return self.user.phone_number


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