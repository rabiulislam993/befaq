# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-12 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_student_registrar'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='is_rejected',
            field=models.BooleanField(default=False),
        ),
    ]