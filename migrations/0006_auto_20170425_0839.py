# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 08:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SimpleBookStore', '0005_auto_20170425_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='photo',
            field=models.ImageField(blank=True, upload_to='uploads/books/photos/'),
        ),
    ]
