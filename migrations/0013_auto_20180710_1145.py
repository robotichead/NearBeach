# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-10 11:45
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('NearBeach', '0012_auto_20180710_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='task_long_description',
            field=tinymce.models.HTMLField(),
        ),
    ]
