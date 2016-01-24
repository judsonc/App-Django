# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='about',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='company',
            name='mission',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='company',
            name='value',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='company',
            name='vision',
            field=models.CharField(max_length=200),
        ),
    ]
