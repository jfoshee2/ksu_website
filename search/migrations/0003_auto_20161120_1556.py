# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-20 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20161120_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.CharField(max_length=2500),
        ),
    ]
