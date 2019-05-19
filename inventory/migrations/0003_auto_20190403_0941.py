# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-04-03 09:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20190403_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outgoing',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 3, 9, 41, 48, 447877)),
        ),
        migrations.AlterField(
            model_name='outgoing',
            name='engg_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='outgoing',
            name='product_id',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='outgoing',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='cetagory',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 3, 9, 41, 48, 447241)),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='supplier',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit_price',
            field=models.FloatField(),
        ),
    ]