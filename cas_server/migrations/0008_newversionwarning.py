# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 21:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cas_server', '0007_auto_20160723_2252'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewVersionWarning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=255)),
            ],
        ),
    ]