# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-27 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skulist', '0005_sku_fcst_sku_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sku_info',
            name='id',
        ),
        migrations.AlterField(
            model_name='sku_info',
            name='item',
            field=models.CharField(blank=True, db_column='KGF_STD_ITEM_CDE', max_length=14, primary_key=True, serialize=False),
        ),
    ]