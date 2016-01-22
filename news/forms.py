from django import forms

from .models import Photo #, Post

"""  Inserir photos   """
class FormPhoto(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('name', 'url',)

""" FORMULARIO PRA PAGINA CONTATO / ADICIONA POSTS
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)
"""
