# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 02:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='transactions',
            field=models.ManyToManyField(blank=True, to='bikes.Transaction'),
        ),
        migrations.AlterField(
            model_name='refurb',
            name='items',
            field=models.ManyToManyField(blank=True, to='bikes.Item'),
        ),
        migrations.AlterField(
            model_name='refurb',
            name='repairs',
            field=models.ManyToManyField(blank=True, to='bikes.Repair'),
        ),
        migrations.AlterField(
            model_name='rental',
            name='transactions',
            field=models.ManyToManyField(blank=True, to='bikes.Transaction'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='items',
            field=models.ManyToManyField(blank=True, to='bikes.Item'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='repairs',
            field=models.ManyToManyField(blank=True, to='bikes.Repair'),
        ),
    ]