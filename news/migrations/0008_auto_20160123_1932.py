# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20160123_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='created_date',
            field=models.DateTimeField(verbose_name='Data de envio', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='photo',
            name='picture',
            field=models.FileField(upload_to='/media/img', verbose_name='Foto'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(verbose_name='Data de envio', default=django.utils.timezone.now),
        ),
    ]
