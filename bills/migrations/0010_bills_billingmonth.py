# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-09 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0009_remove_bills_billingmonth'),
    ]

    operations = [
        migrations.AddField(
            model_name='bills',
            name='billingMonth',
            field=models.DateField(blank=True, null=True),
        ),
    ]