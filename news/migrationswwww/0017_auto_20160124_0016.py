# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0016_auto_20160124_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='category',
            field=models.CharField(choices=[('sites', 'Sites'), ('programas', 'Programas'), ('eventos', 'Eventos'), ('consultorias', 'Consultorias')], max_length=12),
        ),
        migrations.AlterField(
            model_name='client',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data de envio'),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(verbose_name='Nome', max_length=100),
        ),
        migrations.AlterField(
            model_name='client',
            name='picture',
            field=models.ImageField(default='img/default.jpeg', verbose_name='Foto', upload_to='img'),
        ),
        migrations.AlterField(
            model_name='company',
            name='mission',
            field=models.TextField(verbose_name='Missão'),
        ),
        migrations.AlterField(
            model_name='company',
            name='vision',
            field=models.TextField(verbose_name='Visão'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='picture',
            field=models.ImageField(default='img/default.jpeg', verbose_name='Foto', upload_to='img'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(null=True, verbose_name='Texto'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(verbose_name='Título', max_length=200),
        ),
    ]
