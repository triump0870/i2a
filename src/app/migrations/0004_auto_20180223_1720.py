# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-23 17:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20180223_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaire',
            name='last_user',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile'),
        ),
    ]
