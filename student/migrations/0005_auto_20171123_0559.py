# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-23 05:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20171118_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Student is Activate by Default'),
        ),
    ]
