# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 14:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0002_auto_20170831_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='sems',
            field=models.CharField(choices=[('S1', 'S1'), ('S2', 'S2'), ('S3', 'S3'), ('S4', 'S4'), ('S5', 'S5'), ('S6', 'S6'), ('S7', 'S7'), ('S8', 'S8'), ('Other', 'Other')], default='S1', max_length=6),
        ),
        migrations.AddField(
            model_name='user',
            name='branch',
            field=models.CharField(default='XX', max_length=2),
        ),
    ]
