# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-11-30 07:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0010_auto_20191130_1236'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopCar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('gid', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='goods',
            name='price',
            field=models.IntegerField(),
        ),
    ]
