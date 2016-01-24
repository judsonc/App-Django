# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.utils import timezone
from django.template import RequestContext
from .models import *
from .forms import FormPhoto
#from .forms import PostForm

# Retornando o nome do site e suas informações (atributos)
def getCompany():
    return Company.objects.all()[:1]

# Create your views here.
def page404(request):
    response = render_to_response('news/error404/index.html',
                            context_instance=RequestContext(request)
            )
    response.status_code = 404
    return response
    #return render(request, 'news/error404/index.html')

def home(request):
    photos = Banner.objects.all() # Imagens dos slides
    return render(request, 'news/index.html', {'photos': photos, 'title': "home", 'company': getCompany()})

def about(request):
    return render(request, 'news/sobre/index.html', {'company': getCompany(), 'title': "sobre"}) # Textos do sobre

def contact(request):   # Formulario add foto
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
    news = Post.objects.all()
    return render(request, 'news/novidades/index.html', {'posts': news, 'title': "novidades", 'company': getCompany()})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'news/novidades/post_detail.html', {'post': post, 'title': "novidades", 'company': getCompany()})
