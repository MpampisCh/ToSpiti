# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-28 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tospiti', '0012_auto_20170128_1554'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agent',
            options={'verbose_name': 'Agent', 'verbose_name_plural': 'Agents'},
        ),
        migrations.AlterModelOptions(
            name='facility',
            options={'verbose_name': 'Facility', 'verbose_name_plural': 'Facilities'},
        ),
        migrations.AlterModelOptions(
            name='prop_category',
            options={'verbose_name': 'Prop_Category', 'verbose_name_plural': 'Prop_Categories'},
        ),
        migrations.AlterModelOptions(
            name='prop_genre',
            options={'verbose_name': 'Prop_Genre', 'verbose_name_plural': 'Prop_Genres'},
        ),
        migrations.AlterModelOptions(
            name='prop_picture',
            options={'verbose_name': 'Picture', 'verbose_name_plural': 'Pictures'},
        ),
        migrations.AlterModelOptions(
            name='property',
            options={'verbose_name': 'Property', 'verbose_name_plural': 'Properties'},
        ),
        migrations.AlterField(
            model_name='agent',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True),
        ),
    ]
