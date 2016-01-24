# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.template import RequestContext, Context
from django.template.loader import get_template
from django.core.mail import EmailMessage, send_mail, BadHeaderError
from .models import *
from .forms import FormContact
#from .forms import PostForm

# Retornando o nome do site e suas informações (atributos)
def getCompany():
    return Company.objects.all()[0]

# Create your views here.
def home(request):
    photos = Banner.objects.all() # Imagens dos slides
    return render(request, 'news/index.html', {'photos': photos, 'title': "home", 'company': getCompany()})

def about(request):
    return render(request, 'news/sobre/index.html', {'company': getCompany(), 'title': "sobre"}) # Textos do sobre

def contact(request):   # Formulario add foto
    if request.method == "POST":
        name = request.POST.get('name', '')
        message = request.POST.get('message', '')
        email = request.POST.get('email', '')
        if name and message and email:
            try:
                send_mail(name, message, email, ['ex@ex.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('news.views.home')
    else:
        pass
    return render(request, 'news/contato/index.html', {'form': form, 'title': "contato", 'company': getCompany()})

def portfolio(request):
    clients = Client.objects.all() # Imagens dos slides
    return render(request, 'news/portfolio/index.html', {'clients': clients, 'title': "portfolio", 'company': getCompany()})

def services(request):
    categories = CategoryServices.objects.all()
    services = Service.objects.all()
    return render(request, 'news/servicos/index.html', {'company': getCompany(),
                            'title': "servicos", 'categories': categories, 'services': services})

def blog(request):   # Formulario contato
    #news = Post.objects.all()
    return render(request, 'news/error404/index.html', {'title': "novidades", 'company': getCompany()})
    #return render(request, 'news/novidades/index.html', {'posts': news, 'title': "novidades", 'company': getCompany()})

def post_detail(request, pk):
    #post = get_object_or_404(Post, pk=pk)
    return render(request, 'news/error404/index.html', {'title': "novidades", 'company': getCompany()})
    #return render(request, 'news/novidades/post_detail.html', {'post': post, 'title': "novidades", 'company': getCompany()})


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
