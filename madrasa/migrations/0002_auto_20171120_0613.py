# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-20 06:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madrasa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='madrasa',
            name='name',
            field=models.CharField(max_length=127, unique=True),
        ),
    ]
