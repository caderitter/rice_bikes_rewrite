# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-03 02:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0014_transaction_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
    ]
