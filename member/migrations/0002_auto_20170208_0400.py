# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 04:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='prof_pic',
            field=models.ImageField(blank=True, null=True, upload_to=b'', verbose_name='Photo Profile'),
        ),
    ]
