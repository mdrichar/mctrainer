# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-23 02:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factoid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fid', models.IntegerField(default=0)),
                ('factor1', models.IntegerField(default=0)),
                ('factor2', models.IntegerField(default=0)),
            ],
        ),
    ]