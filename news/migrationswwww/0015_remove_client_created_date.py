# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0014_auto_20160124_0003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='created_date',
        ),
    ]
