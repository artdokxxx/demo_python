# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-04 10:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AboutMeApp', '0009_auto_20160704_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='study',
            name='date_finish',
            field=models.DateField(blank=True, null=True, verbose_name='Дата завершения обучения'),
        ),
        migrations.AlterField(
            model_name='work',
            name='date_finish',
            field=models.DateField(blank=True, null=True, verbose_name='Дата завершения'),
        ),
    ]
