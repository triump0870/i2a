# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-24 08:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20180224_0704'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tagtype',
            options={'ordering': ('created',)},
        ),
    ]