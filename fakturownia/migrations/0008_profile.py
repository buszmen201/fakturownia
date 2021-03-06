# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-14 21:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fakturownia', '0007_auto_20180214_2045'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_data', models.TextField(max_length=50)),
                ('address', models.CharField(blank=True, max_length=80)),
                ('nip', models.IntegerField(default=0)),
                ('phonenumber', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
