# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 14:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0017_auto_20170831_1449'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='user',
            new_name='user_register_no',
        ),
    ]
