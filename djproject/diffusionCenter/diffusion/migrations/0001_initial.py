# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-11 12:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length_nm', models.IntegerField(default=50)),
                ('profile', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DiffusionRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diffusion_type', models.CharField(choices=[('INTER', 'Interdiffusion'), ('IMPUR', 'Impurity'), ('SELF', 'Self')], max_length=5)),
                ('material_1', models.CharField(max_length=10)),
                ('material_2', models.CharField(max_length=10)),
                ('additional_data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('short_name', models.CharField(max_length=10)),
                ('heat_transfer_coefficient', models.FloatField()),
                ('thermal_conductivity', models.FloatField()),
                ('melting_point', models.FloatField()),
                ('additional_data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rta_type', models.CharField(choices=[('F', 'Furnace'), ('L', 'Lamp')], max_length=1)),
                ('treatment_times', models.TextField()),
            ],
        ),
    ]