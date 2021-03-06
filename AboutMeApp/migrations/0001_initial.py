# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 20:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EducationalOrganization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='Учебное заведение')),
                ('site', models.URLField(blank=True, verbose_name='Сайт')),
                ('address', models.CharField(max_length=32, verbose_name='Город')),
                ('phone', models.CharField(blank=True, max_length=32, verbose_name='Телефон')),
                ('logo', models.CharField(blank=True, max_length=64, verbose_name='Логотип')),
                ('desc', models.TextField(blank=True, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='Название')),
                ('ico_fa', models.CharField(blank=True, max_length=64, verbose_name='Иконка (FA)')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='Организация')),
                ('site', models.URLField(blank=True, verbose_name='Сайт')),
                ('place', models.CharField(max_length=32, verbose_name='Город')),
                ('phone', models.CharField(blank=True, max_length=32, verbose_name='Телефон')),
                ('logo', models.CharField(blank=True, max_length=64, verbose_name='Логотип')),
                ('desc', models.TextField(blank=True, verbose_name='Описание деятельности компании')),
            ],
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty', models.CharField(max_length=256, verbose_name='Факультет')),
                ('specialty', models.CharField(max_length=256, verbose_name='Специальность')),
                ('degree', models.CharField(max_length=128, verbose_name='Уровень образования')),
                ('date_start', models.DateField(verbose_name='Дата начала обучения')),
                ('date_finish', models.DateField(blank=True, null=True, verbose_name='Дата завершения обучения')),
                ('educational_organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AboutMeApp.EducationalOrganization', verbose_name='Учебное заведение')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_birthday', models.DateField(verbose_name='Дата рождения')),
                ('first_name', models.CharField(max_length=32, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=32, verbose_name='Фамилия')),
                ('second_name', models.CharField(max_length=32, verbose_name='Отчество')),
                ('place_birthday', models.CharField(max_length=64, verbose_name='Место рождения')),
                ('hobbies', models.ManyToManyField(to='AboutMeApp.Hobby')),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=16, verbose_name='Должность')),
                ('desc', models.TextField(verbose_name='Описание')),
                ('date_start', models.DateField(verbose_name='Дата начала')),
                ('date_finish', models.DateField(blank=True, null=True, verbose_name='Дата завершения')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AboutMeApp.Organization', verbose_name='Организация')),
            ],
        ),
    ]
