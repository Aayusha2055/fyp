# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(products)
admin.site.register(Alert)
# admin.site.register(Profile)

admin.site.site_header = "Flood detection system"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome to flood detection system"
