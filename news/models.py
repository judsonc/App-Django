# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

class Company(models.Model):
    #author = models.ForeignKey('auth.User', default=1)
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
    author = models.ForeignKey('auth.User', default=1)
    name = models.CharField('Nome', max_length=100)
    picture = models.ImageField('Foto (DESKTOP)*', upload_to='img/banner')
    picture_small = models.ImageField('Foto (MOBILE)', upload_to='img/banner')
    created_date = models.DateTimeField('Data de envio', auto_now_add=True)

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'

    def __str__(self):
        return self.name

class CategoryServices(models.Model):
    author = models.ForeignKey('auth.User', default=1)
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
    author = models.ForeignKey('auth.User', default=1)
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
    author = models.ForeignKey('auth.User', default=1)
    name = models.CharField('Nome', max_length=100)
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
    phone = models.CharField('Telefone', max_length=11, null=True, blank=True)
    mail = models.EmailField('Email', max_length=50)
    text = models.TextField('Mensagem', max_length=200)
    created_date = models.DateTimeField('Data de envio', auto_now_add=True)

    class Meta:
        verbose_name = 'Email'
        verbose_name_plural = 'Caixa de Emails'

    def __str__(self):
        return self.mail

# class Mail(models.Model):
#     mail = models.ForeignKey(Person)
#     text = models.TextField()
#
#     class Meta:
#         verbose_name = 'Email'
#         verbose_name_plural = 'Emails'
#
#     def __str__(self):
#         return self.mail.name.title()


# class Post(models.Model):
#     author = models.ForeignKey('auth.User')
#     title = models.CharField('Título', max_length=200)
#     text = models.TextField('Texto', null=True)
#     created_date = models.DateTimeField('Data de envio', auto_now_add=True)
#
#     class Meta:
#         verbose_name = 'Post'
#         verbose_name_plural = 'Blog'
#
#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()
#
#     def __str__(self):
#         return self.title
