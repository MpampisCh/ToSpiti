# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-27 00:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tospiti', '0004_property_squaremeters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='price',
            field=models.FloatField(blank=True, null=True, verbose_name='τιμή'),
        ),
    ]
