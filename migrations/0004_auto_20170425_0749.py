# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 07:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SimpleBookStore', '0003_author_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='birthdate',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='uploads/books/covers/'),
        ),
    ]
