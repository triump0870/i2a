# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-23 18:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_application_next_review_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='application_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.Application'),
            preserve_default=False,
        ),
    ]
