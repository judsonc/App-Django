# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('picture', models.ImageField(upload_to='img/banner', verbose_name='Foto (DESKTOP)*')),
                ('picture_small', models.ImageField(upload_to='img/banner', verbose_name='Foto (MOBILE)')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Data de envio')),
                ('author', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Banner',
                'verbose_name_plural': 'Banners',
            },
        ),
        migrations.CreateModel(
            name='CategoryServices',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='Nome')),
                ('picture', models.ImageField(upload_to='img/service', verbose_name='Foto (150x120)*')),
                ('text', models.TextField(max_length=175, verbose_name='Descri\xe7\xe3o')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Data de envio')),
                ('author', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias de Servi\xe7os',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('picture', models.ImageField(upload_to='img/portfolio', verbose_name='Foto (325x190)*')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Data de envio')),
                ('author', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(verbose_name='Categoria', to='sitio.CategoryServices')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Portf\xf3lio',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('about', models.TextField(verbose_name='Quem somos')),
                ('mission', models.TextField(verbose_name='Miss\xe3o')),
                ('vision', models.TextField(verbose_name='Vis\xe3o')),
                ('value', models.TextField(verbose_name='Valores')),
                ('address', models.CharField(max_length=100, verbose_name='Endere\xe7o')),
                ('zip', models.CharField(max_length=9, verbose_name='CEP')),
                ('neighboor', models.CharField(max_length=50, verbose_name='Bairro')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Data de altera\xe7\xe3o')),
                ('author', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Sua Empresa',
            },
        ),
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, null=True, verbose_name='Nome', blank=True)),
                ('phone', models.CharField(max_length=11, null=True, verbose_name='Telefone', blank=True)),
                ('mail', models.EmailField(max_length=50, verbose_name='Email')),
                ('text', models.TextField(max_length=200, verbose_name='Mensagem')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Data de envio')),
            ],
            options={
                'verbose_name': 'Email',
                'verbose_name_plural': 'Caixa de Emails',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='Nome')),
                ('picture', models.ImageField(upload_to='img/service', verbose_name='Foto (150x120)*')),
                ('text', models.TextField(max_length=175, verbose_name='Descri\xe7\xe3o')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Data de envio')),
                ('author', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(verbose_name='Categoria', to='sitio.CategoryServices')),
            ],
            options={
                'verbose_name': 'Servi\xe7o',
                'verbose_name_plural': 'Servi\xe7os',
            },
        ),
    ]
