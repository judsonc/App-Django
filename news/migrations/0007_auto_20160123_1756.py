# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20160121_1620'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'Empresa', 'verbose_name_plural': 'Empresas'},
        ),
        migrations.AlterModelOptions(
            name='photo',
            options={'verbose_name': 'Foto', 'verbose_name_plural': 'Fotos'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Postagem', 'verbose_name_plural': 'Postagens'},
        ),
        migrations.RemoveField(
            model_name='photo',
            name='url',
        ),
        migrations.AddField(
            model_name='photo',
            name='picture',
            field=models.FileField(default=datetime.datetime(2016, 1, 23, 20, 56, 56, 229308, tzinfo=utc), upload_to='/upload/img'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='about',
            field=models.TextField(verbose_name='Quem somos'),
        ),
        migrations.AlterField(
            model_name='company',
            name='mission',
            field=models.TextField(verbose_name='Missão'),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='company',
            name='value',
            field=models.TextField(verbose_name='Valores'),
        ),
        migrations.AlterField(
            model_name='company',
            name='vision',
            field=models.TextField(verbose_name='Visão'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(verbose_name='Texto'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Título'),
        ),
    ]
