# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import FV, Product, Category

# Register your models here.


admin.site.register(FV)
admin.site.register(Product)
admin.site.register(Category)