# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-11-29 12:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0005_auto_20191129_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
