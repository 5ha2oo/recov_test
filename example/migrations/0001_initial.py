# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-03-01 10:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='', max_length=64)),
                ('name', models.CharField(default='', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='TE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='example.Exercise')),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='te',
            name='training',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='example.Training'),
        ),
    ]
