# -*- coding: utf-8 -*-
from django import forms
from .models import Banner #, Post

class FormContact(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea)

"""  Inserir photos
class FormPhoto(forms.ModelForm):
    class Meta:
        model = Banner
        fields = ('name', 'picture', 'picture_small')
"""

""" FORMULARIO PRA PAGINA CONTATO / ADICIONA POSTS
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)
"""
