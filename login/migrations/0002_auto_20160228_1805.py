# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-28 17:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]