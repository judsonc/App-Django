# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
#from django.utils import timezone

class Company(models.Model):
    author = models.ForeignKey('auth.User', default=1, verbose_name='Usuário')
    name = models.CharField('Nome', max_length=100)
    about = models.TextField('Quem somos')
    mission = models.TextField('Missão')
    vision = models.TextField('Visão')
    value = models.TextField('Valores')
    address = models.CharField('Endereço', max_length=100)
    zip = models.CharField('CEP', max_length=9)
    neighboor = models.CharField('Bairro', max_length=50)
    created_date = models.DateTimeField('Data de alteração', auto_now_add=True)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Sua Empresa'

    def __str__(self):
        return self.name

class Banner(models.Model):
    author = models.ForeignKey('auth.User', default=1, verbose_name='Usuário')
    name = models.CharField('Nome', max_length=100)
    picture = models.ImageField('Foto (DESKTOP)*', upload_to='img/banner')
    picture_small = models.ImageField('Foto (MOBILE)', upload_to='img/banner', null=True, blank=True)
    created_date = models.DateTimeField('Data de envio', auto_now_add=True)

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'

    def __str__(self):
        return self.name

class CategoryServices(models.Model):
    author = models.ForeignKey('auth.User', default=1, verbose_name='Usuário')
    name = models.CharField('Nome', max_length=20)
    picture = models.ImageField('Foto (150x120)*', upload_to='img/service')
    text = models.TextField('Descrição', max_length=175)
    created_date = models.DateTimeField('Data de envio', auto_now_add=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias de Serviços'

    def __str__(self):
        return self.name

class Service(models.Model):
    author = models.ForeignKey('auth.User', default=1, verbose_name='Usuário')
    name = models.CharField('Nome', max_length=20)
    picture = models.ImageField('Foto (150x120)*', upload_to='img/service')
    text = models.TextField('Descrição', max_length=175)
    category = models.ForeignKey(CategoryServices, verbose_name="Categoria")
    created_date = models.DateTimeField('Data de envio', auto_now_add=True)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.name + " | " + self.category.name

class Client(models.Model):
    author = models.ForeignKey('auth.User', default=1, verbose_name='Usuário')
    name = models.CharField('Nome', max_length=100)
    url = models.CharField('URL', max_length=200, null=True, blank=True)
    picture = models.ImageField('Foto (325x190)*', upload_to='img/portfolio')
    category = models.ForeignKey(CategoryServices, verbose_name="Categoria")
    created_date = models.DateTimeField('Data de envio', auto_now_add=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Portfólio'

    def __str__(self):
        return self.name.title() + " | " + self.category.name.title()

class Mail(models.Model):
    name = models.CharField('Nome', max_length=50, null=True, blank=True)
    phone = models.CharField('Telefone', max_length=20, null=True, blank=True)
    mail = models.EmailField('Email', max_length=50)
    text = models.TextField('Mensagem', max_length=300)
    created_date = models.DateTimeField('Data de envio', auto_now_add=True)

    class Meta:
        verbose_name = 'Email'
        verbose_name_plural = 'Caixa de Emails'

    def __str__(self):
        return self.mail
