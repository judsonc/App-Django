# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.utils import timezone
from django.contrib import messages
from django.template import RequestContext, Context
from django.template.loader import get_template
from sitio.models import *
from sitio.forms import *

# Retornando o nome do site e suas informações (atributos)
def getCompany():
    if Company.objects.all():
        #: Retorna informações da companhia caso tenha uma cadastrada
        return Company.objects.all()[0]
    else:
        return "None"

def contactEJ(request):   # Formulario add foto
    if request.method == "POST":
        formEJ = FormContactEJ(request.POST, prefix='toEJ')
        if formEJ.is_valid():
            formEJ.save()
            messages.success(request, 'Email enviado com sucesso!')
        else:
            messages.error(request, 'Falha ao enviar o email!')
    formEJ = FormContactEJ(prefix='toEJ')
    return formEJ

def contactYou(request):   # Formulario add foto
    if request.method == "POST":
        formYou = FormContactYou(request.POST, prefix='toYou')
        if formYou.is_valid():
            formYou.save()
            messages.success(request, 'Enviado com sucesso!')
    formYou = FormContactYou(prefix='toYou')
    return formYou

# Create your views here.
def home(request):
    photos = Banner.objects.all() # Imagens dos slides
    return render(request, 'mobile/index.html',
        {'photos': photos, 'title': "home", 'company': getCompany()})

def about(request):
    return render(request, 'mobile/sobre/index.html',
        {'company': getCompany(), 'title': "sobre"})

def portfolio(request):
    clients = Client.objects.all() # Imagens dos slides
    return render(request, 'mobile/portfolio/index.html',
        {'clients': clients, 'title': "portfolio", 'company': getCompany()})

def services(request):
    categories = CategoryServices.objects.all()
    services = Service.objects.all()
    return render(request, 'mobile/servicos/index.html',
        {'company': getCompany(), 'title': "servicos", 'categories': categories, 'services': services})

def contact(request):  # Formulario contato
    return render(request, 'mobile/contato/index.html',
        {'title': "contato", 'company': getCompany(),
        'formEJ': contactEJ(request), 'formYou': contactYou(request)})

def blog(request):   # Formulario contato
    return render(request, 'mobile/error404/index.html',
        {'title': "novidades", 'company': getCompany()})
