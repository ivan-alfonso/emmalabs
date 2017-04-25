# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-25 03:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('protocolo', '0001_initial'),
        ('experimento', '0001_initial'),
        ('proyecto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resultado', models.CharField(blank=True, max_length=50, null=True)),
                ('satisfactorio', models.BooleanField()),
                ('observaciones', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_resultado', models.DateTimeField(blank=True, null=True)),
                ('experimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experimento', to='experimento.Experimento')),
                ('protocolo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='protocolo', to='protocolo.Protocolo')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proyecto', to='proyecto.Proyecto')),
            ],
        ),
    ]
