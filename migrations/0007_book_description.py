# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 10:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SimpleBookStore', '0006_auto_20170425_0839'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]