# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-29 05:47
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SimpleBookStore', '0009_auto_20170427_1905'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.SmallIntegerField()),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SimpleBookStore.Book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='users',
            field=models.ManyToManyField(related_name='users', through='SimpleBookStore.UserBook', to=settings.AUTH_USER_MODEL),
        ),
    ]
