# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='about',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='company',
            name='mission',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='company',
            name='value',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='company',
            name='vision',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='photo',
            name='name',
            field=models.TextField(),
        ),
    ]
