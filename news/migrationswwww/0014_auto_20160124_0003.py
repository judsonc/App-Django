# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_remove_client_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Data de envio'),
        ),
    ]
