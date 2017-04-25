# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SimpleBookStore', '0004_auto_20170425_0749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='photo',
            field=models.ImageField(upload_to='uploads/books/photos/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(upload_to='uploads/books/covers/'),
        ),
    ]
