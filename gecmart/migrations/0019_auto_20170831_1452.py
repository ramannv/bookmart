# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 14:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0018_auto_20170831_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='user_register_no',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mart.User'),
        ),
    ]