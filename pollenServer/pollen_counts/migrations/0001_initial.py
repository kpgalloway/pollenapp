# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 04:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PollenCounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('location', models.CharField(max_length=10)),
                ('alder_count', models.FloatField()),
                ('willow_count', models.FloatField()),
                ('birch_count', models.FloatField()),
                ('spruce_count', models.FloatField()),
                ('other1_tree_count', models.FloatField()),
                ('other2_tree__count', models.FloatField()),
                ('total_tree_count', models.FloatField()),
                ('grass_count', models.FloatField()),
                ('grass2_count', models.FloatField()),
                ('total_grass_count', models.FloatField()),
                ('weed_count', models.FloatField()),
                ('other1_count', models.FloatField()),
                ('other2_count', models.FloatField()),
                ('total_pollen_count', models.FloatField()),
                ('mold_count', models.FloatField()),
                ('comments', models.TextField()),
            ],
        ),
    ]