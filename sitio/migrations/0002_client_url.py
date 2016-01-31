# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='url',
            field=models.CharField(default='localhost', max_length=200, verbose_name='URL'),
            preserve_default=False,
        ),
    ]
