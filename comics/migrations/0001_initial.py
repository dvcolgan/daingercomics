# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-05 20:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BackgroundImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=b'img/')),
            ],
        ),
        migrations.CreateModel(
            name='Comic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to=b'img/')),
                ('image_title', models.CharField(blank=True, max_length=511)),
                ('image_alt', models.CharField(blank=True, max_length=511)),
                ('post', models.TextField(blank=True)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='StaticPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('slug', models.SlugField(max_length=255)),
            ],
        ),
    ]
