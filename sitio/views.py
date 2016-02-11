# -*- coding: utf-8 -*-
from django.shortcuts import render #, get_object_or_404, redirect, render_to_response
#from django.utils import timezone
#from django.template import RequestContext, Context
#from django.template.loader import get_template
from django.contrib import messages
from django.core.mail import send_mail
from sitio.models import *
from sitio.forms import *

# Retornando o nome do site e suas informações (atributos)
def getCompany():
    if Company.objects.all():
        #: Retorna informações da companhia caso tenha uma cadastrada
        return Company.objects.all()[0]
    else:
        return "None"

def contactEJ(request):
    if request.method == "POST":
        formEJ = FormContactEJ(request.POST, prefix='toEJ')
        if formEJ.is_valid():
            formEJ.save()
            #send_mail('Subject here 1', 'Here is the message. contactEJ', 'from@example.com',
            #         ['to@example.com'], fail_silently=False)
            messages.success(request, 'Email enviado com sucesso!')
    formEJ = FormContactEJ(prefix='toEJ')
    return formEJ

def contactYou(request):
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
    return render(request, 'sitio/index.html',
        {'photos': photos, 'title': "home", 'company': getCompany(),
         'formEJ': contactEJ(request), 'formYou': contactYou(request)})

def about(request):
    return render(request, 'sitio/sobre/index.html',
        {'company': getCompany(), 'title': "sobre",
        'formEJ': contactEJ(request), 'formYou': contactYou(request)})

def portfolio(request):
    clients = Client.objects.all() # Imagens dos slides
    return render(request, 'sitio/portfolio/index.html',
        {'clients': clients, 'title': "portfolio", 'company': getCompany(),
        'formEJ': contactEJ(request), 'formYou': contactYou(request)})

def services(request):
    categories = CategoryServices.objects.all()
    services = Service.objects.all()
    return render(request, 'sitio/servicos/index.html',
        {'company': getCompany(), 'title': "servicos", 'categories': categories, 'services': services,
        'formEJ': contactEJ(request), 'formYou': contactYou(request)})

def blog(request):   # Formulario contato
    return render(request, 'sitio/error404/index.html',
        {'title': "novidades", 'company': getCompany(),
        'formEJ': contactEJ(request), 'formYou': contactYou(request)})
