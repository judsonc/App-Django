# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response #, get_object_or_404, redirect,
from django.template import RequestContext #, Context
#from django.http import HttpResponseNotFound
#from django.utils import timezone
#from django.template.loader import get_template
#from django.core.mail import send_mail
#from datetime import datetime
from ipware.ip import get_ip
from django.contrib import messages
from sitio.models import Company, Banner, Client, CategoryServices, Service
from sitio.forms import FormContactEJ, FormContactYou

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
    return home(request)
    """
    ip = get_ip(request)
    if ip is None:
        ip = "Conexão falhou!!"
    return render(request, 'sitio/error404/index.html',
        {'title': "novidades", 'company': getCompany(), 'ip': ip,
        'formEJ': contactEJ(request), 'formYou': contactYou(request)})
    """

def not_found_error(request):
    ip = get_ip(request)
    if ip is None:
        ip = "Conexão falhou!!"
    response = render_to_response('sitio/error404/index.html',
                    {'company': getCompany(), 'title': "Página não encontrada", 'ip': ip,
                    'formEJ': contactEJ(request), 'formYou': contactYou(request)},
                    context_instance = RequestContext(request))
    response.status_code = 404
    return response
