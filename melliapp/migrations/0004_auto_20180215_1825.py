# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-15 18:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('melliapp', '0003_produkt_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produkt',
            old_name='image',
            new_name='photo',
        ),
    ]
