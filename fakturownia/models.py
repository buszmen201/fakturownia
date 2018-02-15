# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.contrib.auth.models import User
from django.db import models
from localflavor.generic.models import IBANField


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.FloatField(default=0)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

    def vat_value(self):
        return self.price * 0.23

    def vat(self):
        return "23%"

    def price_netto(self):
        return self.price - (self.price * 0.23)


class FV(models.Model):
    payments = (
        ('got', 'gotówka'),
        ('prz', 'przelew'),
        ('rat', 'raty')
    )

    client = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    nip = models.IntegerField(default=00000000000)
    fv_date = models.DateField(default=datetime.date.today)
    complete_date = models.DateField(default=datetime.date.today)
    payment_method = models.CharField(
        max_length=3,
        choices=payments,
        default='prz',
    )
    iban = IBANField()
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.client


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    seller_data = models.TextField(max_length=50, blank=False)
    address = models.CharField(max_length=80, blank=True)
    nip = models.CharField(max_length=11, unique=False)
    phonenumber = models.CharField(max_length=9, unique=False)
