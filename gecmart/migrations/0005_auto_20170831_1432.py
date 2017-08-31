# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 14:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0004_item_branch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='phNo',
        ),
        migrations.AddField(
            model_name='item',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mart.User'),
        ),
        migrations.AddField(
            model_name='user',
            name='phNo',
            field=models.IntegerField(default=0),
        ),
    ]