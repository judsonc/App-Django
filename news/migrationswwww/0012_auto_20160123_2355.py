# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_auto_20160123_2222'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'Cliente', 'verbose_name_plural': 'Portf\xf3lio'},
        ),
        migrations.AlterModelOptions(
            name='photo',
            options={'verbose_name': 'Banner', 'verbose_name_plural': 'Slide'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Post', 'verbose_name_plural': 'Blog'},
        ),
        migrations.RemoveField(
            model_name='client',
            name='name',
        ),
        migrations.RemoveField(
            model_name='client',
            name='picture',
        ),
        migrations.AddField(
            model_name='client',
            name='image',
            field=models.ForeignKey(default=django.utils.timezone.now, to='news.Photo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='category',
            field=models.CharField(max_length=12, choices=[(b'sites', b'Sites'), (b'programas', b'Programas'), (b'eventos', b'Eventos'), (b'consultorias', b'Consultorias')]),
        ),
    ]
