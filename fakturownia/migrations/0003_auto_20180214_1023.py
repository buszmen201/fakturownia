# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-14 09:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fakturownia', '0002_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fv',
            name='products',
        ),
        migrations.AddField(
            model_name='fv',
            name='products',
            field=models.ManyToManyField(to='fakturownia.Product'),
        ),
    ]
