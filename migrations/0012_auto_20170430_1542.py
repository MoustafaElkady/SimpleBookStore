# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-30 15:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SimpleBookStore', '0011_auto_20170430_0459'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='book',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]