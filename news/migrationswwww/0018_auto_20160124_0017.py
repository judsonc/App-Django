# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0017_auto_20160124_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='picture',
            field=models.ImageField(upload_to='img', verbose_name='Foto'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='picture',
            field=models.ImageField(upload_to='img', verbose_name='Foto'),
        ),
    ]
