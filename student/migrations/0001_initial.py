# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-18 10:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('madrasa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('father', models.CharField(max_length=100)),
                ('address', models.TextField(blank=True, null=True)),
                ('markaz', models.CharField(blank=True, max_length=127)),
                ('marhala', models.CharField(choices=[('takmil', 'Takmil'), ('fazilat', 'Fazilat'), ('sanabia', 'Sanabia Ulia'), ('mutawassitah', 'Mutawassitah'), ('ibtedaiyah', 'Ibtedaiyah'), ('hifz', 'Hifzul Quran'), ('tazbid', 'Ilmut Tazbid wal Qirat')], max_length=10)),
                ('reg_year', models.CharField(choices=[('2016', '2016'), ('2017', '2017'), ('2018', '2018')], default='2018', max_length=4)),
                ('registered_at', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('madrasa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='madrasa.Madrasa')),
                ('registrar', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
