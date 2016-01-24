# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0010_auto_20160123_2004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Nome')),
                ('picture', models.ImageField(upload_to=b'img', verbose_name=b'Foto')),
                ('category', models.CharField(max_length=1, choices=[(b'sites', b'Sites'), (b'programas', b'Programas'), (b'eventos', b'Eventos'), (b'consultorias', b'Consultorias')])),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'Data de envio')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Portf\xf3lio',
                'verbose_name_plural': 'Portf\xf3lio',
            },
        ),
        migrations.RemoveField(
            model_name='post',
            name='published_date',
        ),
        migrations.AlterField(
            model_name='company',
            name='mission',
            field=models.TextField(verbose_name=b'Miss\xc3\xa3o'),
        ),
        migrations.AlterField(
            model_name='company',
            name='vision',
            field=models.TextField(verbose_name=b'Vis\xc3\xa3o'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, verbose_name=b'T\xc3\xadtulo'),
        ),
    ]
