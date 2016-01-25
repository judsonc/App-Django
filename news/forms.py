# -*- coding: utf-8 -*-
from django import forms
from .models import Mail #, Post

class FormContactYou(forms.ModelForm):
    class Meta:
        model = Mail
        fields = ('name', 'mail', 'phone')
        widgets = {'name': forms.TextInput(attrs={'required': 'True',
                                                'placeholder': 'Nome', 'class':'form-control'}),
                    'mail': forms.TextInput(attrs={'required': 'False', 'type':'email',
                                                'placeholder': 'Email', 'class':'form-control'}),
                    'phone': forms.TextInput(attrs={'required': 'True',
                                                'placeholder': 'Telefone', 'class':'form-control'})
        }

class FormContactEJ(forms.ModelForm):
    class Meta:
        model = Mail
        fields = ('text', 'phone', 'mail')
        widgets = {'phone': forms.TextInput(attrs={'required': 'True',
                                            'placeholder': 'Telefone', 'class':'form-control'}),
                'mail': forms.TextInput(attrs={'required': 'True', 'type':'email',
                                            'placeholder': 'Email', 'class':'form-control'}),
                'text': forms.Textarea(attrs={'required': 'True', 'rows': '6', 'cols': '61',
                                            'placeholder': 'Deixe sua Mensagem', 'class':'form-control'})
        }

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
