# -*- coding: utf-8 -*-
from django import forms
from sitio.models import Mail

class FormContactYou(forms.ModelForm):
    class Meta:
        model = Mail
        fields = ('name', 'mail', 'phone')
        widgets = {'name': forms.TextInput(attrs={'required': 'True',
                                                'placeholder': 'Nome', 'class':'form-control'}),
                    'mail': forms.TextInput(attrs={'required': 'False', 'type':'email',
                                                'placeholder': 'Email', 'class':'form-control'}),
                    'phone': forms.TextInput(attrs={'required': 'True', 'type': 'tel',
                                                'placeholder': 'Telefone', 'class':'form-control'}),
        }

class FormContactEJ(forms.ModelForm):
    class Meta:
        model = Mail
        fields = ('text', 'phone', 'mail', 'name')
        widgets = {'phone': forms.TextInput(attrs={'required': 'True', 'type': 'tel',
                                                'placeholder': 'Telefone', 'class':'form-control'}),
                    'mail': forms.TextInput(attrs={'required': 'True', 'type':'email',
                                                'placeholder': 'Email', 'class':'form-control'}),
                    'text': forms.Textarea(attrs={'required': 'True', 'rows': '6', 'cols': '61',
                                                'placeholder': 'Deixe sua Mensagem', 'class':'form-control mensagem'}),
                    'name': forms.TextInput(attrs={'required': 'True',
                                                'placeholder': 'Nome', 'class':'form-control'}),
        }
