# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('register_no', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='phNo',
            field=models.IntegerField(),
        ),
    ]
