# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-09 15:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0014_remove_bills_billingmonth2'),
    ]

    operations = [
        migrations.AddField(
            model_name='bills',
            name='billingMonth2',
            field=models.DateTimeField(default='2016-04-02'),
        ),
    ]