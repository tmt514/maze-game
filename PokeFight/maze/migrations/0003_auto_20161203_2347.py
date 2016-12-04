# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-03 23:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maze', '0002_auto_20161203_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='Money',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='monster',
            name='attack',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='monster',
            name='defence',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='monster',
            name='health',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='monster',
            name='image_url',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='monster',
            name='move',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='monster',
            name='name',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='monster',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='maze.Room'),
        ),
    ]