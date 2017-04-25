# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-25 03:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0001_initial'),
        ('experimento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=50, null=True)),
                ('estado', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_creacion', models.DateTimeField(blank=True, null=True)),
                ('asistentes', models.ManyToManyField(to='usuario.Usuario')),
                ('cientifico_asignado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cientifico_asignado', to='usuario.Usuario')),
                ('experimentos', models.ManyToManyField(to='experimento.Experimento')),
            ],
        ),
    ]
