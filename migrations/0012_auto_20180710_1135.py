# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-10 11:35
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('NearBeach', '0011_requirement_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks_history',
            name='task_history',
            field=tinymce.models.HTMLField(),
        ),
    ]
