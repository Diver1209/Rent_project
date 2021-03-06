# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-16 20:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TOFI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('RoleID', models.IntegerField()),
                ('Name', models.CharField(max_length=50)),
                ('Surname', models.CharField(max_length=50)),
                ('LastName', models.CharField(max_length=50)),
                ('Age', models.IntegerField()),
                ('PassportID', models.CharField(max_length=50)),
                ('Phone', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
