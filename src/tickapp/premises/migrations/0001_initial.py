# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-29 20:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=200)),
                ('cat_desc', models.TextField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drink_name', models.CharField(max_length=200)),
                ('drink_price', models.IntegerField(default=0)),
                ('drink_desc', models.TextField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Premise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True, max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'published')),
            ],
        ),
        migrations.CreateModel(
            name='Premise_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=200)),
                ('cat_desc', models.TextField(blank=True, max_length=100)),
                ('premise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='premises.Premise')),
            ],
        ),
        migrations.AddField(
            model_name='drink',
            name='premise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='premises.Premise_Category'),
        ),
    ]
