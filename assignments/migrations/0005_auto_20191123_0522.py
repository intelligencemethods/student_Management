# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-11-23 05:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0004_auto_20191123_0520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='teacher',
        ),
        migrations.AddField(
            model_name='teacher',
            name='teacher',
            field=models.ManyToManyField(to='assignments.Subject'),
        ),
    ]
