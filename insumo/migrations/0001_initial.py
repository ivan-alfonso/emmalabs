# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 20:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Insumo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=50, null=True)),
                ('cantidad', models.IntegerField(default=1)),
                ('unidades', models.CharField(default=b'Unidades', max_length=20)),
            ],
        ),
    ]
