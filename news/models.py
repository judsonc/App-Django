# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField('Título', max_length=200)
    text = models.TextField('Texto')
    created_date = models.DateTimeField('Data de envio', default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'Postagem'
        verbose_name_plural = 'Postagens'

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Company(models.Model):
    name = models.CharField('Nome', max_length=100)
    about = models.TextField('Quem somos')
    mission = models.TextField('Missão')
    vision = models.TextField('Visão')
    value = models.TextField('Valores')

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.name

class Photo(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField('Nome', max_length=100)
    picture = models.ImageField('Foto', upload_to='img')
    created_date = models.DateTimeField('Data de envio', default=timezone.now)

    class Meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'

    def __str__(self):
        return self.name

#
# class Person(models.Model):
#     name = models.TextField()
#     mail = models.TextField()
#
#     def __str__(self):
#         return self.name
#
# class Mail(models.Model):
#     author = models.ForeignKey('auth.Person')
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#
#     def __str__(self):
#         return self.author
