# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-29 21:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blackout', '0004_auto_20160529_2107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='bakery',
        ),
    ]
