# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-27 03:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protocolo', '0015_auto_20170326_2132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paso',
            name='salidas',
        ),
        migrations.AddField(
            model_name='paso',
            name='salida',
            field=models.CharField(max_length=500, null=True),
        ),
    ]