# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-12-02 08:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0024_auto_20191202_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
