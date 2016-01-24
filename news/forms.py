# -*- coding: utf-8 -*-
from django import forms

from .models import Banner #, Post

"""  Inserir photos   """
class FormPhoto(forms.ModelForm):
    class Meta:
        model = Banner
        fields = ('name', 'picture', 'picture_small')

""" FORMULARIO PRA PAGINA CONTATO / ADICIONA POSTS
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)
"""
