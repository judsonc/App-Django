# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0015_remove_client_created_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='image',
        ),
        migrations.AddField(
            model_name='client',
            name='author',
            field=models.ForeignKey(default='teste', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'Data de envio'),
        ),
        migrations.AddField(
            model_name='client',
            name='name',
            field=models.CharField(default='anf', max_length=100, verbose_name=b'Nome'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='picture',
            field=models.ImageField(default=b'img/default.jpeg', upload_to=b'img', verbose_name=b'Foto'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='picture',
            field=models.ImageField(default=b'img/default.jpeg', upload_to=b'img', verbose_name=b'Foto'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(null=True, verbose_name=b'Texto'),
        ),
    ]
