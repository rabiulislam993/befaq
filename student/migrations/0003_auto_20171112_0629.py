# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-12 06:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20171112_0628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='reg_id',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]