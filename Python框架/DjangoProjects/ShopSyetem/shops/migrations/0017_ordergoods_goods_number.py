# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-11-30 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0016_auto_20191130_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordergoods',
            name='goods_number',
            field=models.IntegerField(default=1),
        ),
    ]
