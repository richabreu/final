# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-11 02:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('final', '0004_auto_20170710_0110'),
    ]

    operations = [
        migrations.AddField(
            model_name='sourceurl',
            name='name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]