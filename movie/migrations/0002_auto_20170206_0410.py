# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 04:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='cover',
            field=models.ImageField(blank=True, default='no-pre.png', upload_to='movie_covers/'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='deskripsi'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=200, verbose_name='judul'),
        ),
    ]
