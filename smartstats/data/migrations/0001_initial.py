# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-08 13:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoordianteCountryMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=5)),
                ('lon', models.FloatField(default=0)),
                ('lat', models.FloatField(default=0)),
            ],
        ),
    ]
