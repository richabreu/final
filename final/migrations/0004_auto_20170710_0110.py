# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-10 01:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('final', '0003_auto_20170710_0105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='final.User'),
        ),
    ]
