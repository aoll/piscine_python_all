# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-11 11:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ex07', '0002_auto_20170411_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='movies',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]