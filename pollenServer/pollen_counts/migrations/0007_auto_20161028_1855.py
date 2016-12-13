# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 18:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollen_counts', '0006_auto_20161028_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='pollencounts',
            name='poplar_aspen',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='pollencounts',
            name='alder',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='pollencounts',
            name='birch',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='pollencounts',
            name='grass',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='pollencounts',
            name='grass_2',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='pollencounts',
            name='mold',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='pollencounts',
            name='other1',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='pollencounts',
            name='other1_tree',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='pollencounts',
            name='other2',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='pollencounts',
            name='other2_tree',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='pollencounts',
            name='spruce',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='pollencounts',
            name='total_grass',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='pollencounts',
            name='total_pollen',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='pollencounts',
            name='total_tree',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='pollencounts',
            name='weed',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='pollencounts',
            name='willow',
            field=models.FloatField(null=True),
        ),
    ]