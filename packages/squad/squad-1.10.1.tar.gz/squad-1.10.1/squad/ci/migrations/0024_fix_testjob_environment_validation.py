# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-23 11:51
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ci', '0023_remove_testjob_build'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testjob',
            name='environment',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Z0-9][a-zA-Z0-9_.-]*$')]),
        ),
    ]
