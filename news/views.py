# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.utils import timezone
from django.contrib import messages
from django.template import RequestContext, Context
from django.template.loader import get_template
from django.core.mail import EmailMessage, send_mail
from .models import *
from .forms import *

# Retornando o nome do site e suas informações (atributos)
def getCompany():
    return Company.objects.all()[0]

def contactEJ(request):   # Formulario add foto
    if request.method == "POST":
        formEJ = FormContactEJ(request.POST, prefix='toEJ')
        if formEJ.is_valid():
            formEJ.save()
            messages.success(request, 'Enviado com sucesso!')
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
    return render(request, 'news/index.html',
        {'photos': photos, 'title': "home", 'company': getCompany(),
         'formEJ': contactEJ(request), 'formYou': contactYou(request)})

def about(request):
    return render(request, 'news/sobre/index.html',
        {'company': getCompany(), 'title': "sobre",
        'formEJ': contactEJ(request), 'formYou': contactYou(request)})

def portfolio(request):
    clients = Client.objects.all() # Imagens dos slides
    return render(request, 'news/portfolio/index.html',
        {'clients': clients, 'title': "portfolio", 'company': getCompany(),
        'formEJ': contactEJ(request), 'formYou': contactYou(request)})

def services(request):
    categories = CategoryServices.objects.all()
    services = Service.objects.all()
    return render(request, 'news/servicos/index.html',
        {'company': getCompany(), 'title': "servicos", 'categories': categories, 'services': services,
        'formEJ': contactEJ(request), 'formYou': contactYou(request)})

def blog(request):   # Formulario contato
    #news = Post.objects.all()
    #return render(request, 'news/novidades/index.html', {'posts': news, 'title': "novidades", 'company': getCompany()})
    return render(request, 'news/error404/index.html',
        {'title': "novidades", 'company': getCompany(),
        'formEJ': contactEJ(request), 'formYou': contactYou(request)})

'''
def post_detail(request, pk):
    #post = get_object_or_404(Post, pk=pk)
    #return render(request, 'news/novidades/post_detail.html', {'post': post, 'title': "novidades", 'company': getCompany()})
    return render(request, 'news/error404/index.html',
        {'title': "novidades", 'company': getCompany()})
'''

''' Form add image
if request.method == "POST":
    form = FormPhoto(request.POST, request.FILES)
    if form.is_valid():
        photo = form
        photo.author = request.user
        newphoto = Banner(picture = request.FILES['picture'])
        newphoto.save()
        return redirect('news.views.home')
else:
    form = FormPhoto()
'''
