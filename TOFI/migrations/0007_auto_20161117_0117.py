# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 01:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TOFI', '0006_auto_20161117_0034'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Role',
        ),
        migrations.DeleteModel(
            name='Tenant',
        ),
        migrations.AddField(
            model_name='myuser',
            name='ie',
            field=models.BooleanField(default=False, verbose_name='ИП'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='license_field',
            field=models.CharField(default=None, max_length=50, verbose_name='Лицензия'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='taxpayer_account_number',
            field=models.IntegerField(default=None, verbose_name='УНН'),
        ),
    ]
