# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-16 18:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('homepage', '0003_auto_20161016_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='answered_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
