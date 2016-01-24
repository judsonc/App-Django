# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Company, Photo
from .forms import FormPhoto
#from .forms import PostForm

# Retornando o nome do site e suas informações (atributos)
def getCompany():
    text = Company.objects.all()[0]
    if text:
        return text
    else:
        return ''

# Create your views here.
def home(request):
    photos = Photo.objects.all() # Imagens dos slides
    return render(request, 'news/index.html', {'photos': photos, 'title': "home", 'company': getCompany()})

def about(request):
    return render(request, 'news/sobre/index.html', {'company': getCompany(), 'title': "sobre"}) # Textos do sobre

def contact(request):   # Formulario add foto
    if request.method == "POST":
        form = FormPhoto(request.POST, request.FILES)
        if form.is_valid():
            photo = form
            photo.author = request.user
            newphoto = Photo(picture = request.FILES['picture'])
            newphoto.save()
            return redirect('news.views.home')
    else:
        form = FormPhoto()
    return render(request, 'news/contato/index.html', {'form': form, 'title': "contato", 'company': getCompany()})

def blog(request):   # Formulario contato
    news = Post.objects.all()
    return render(request, 'news/novidades/index.html', {'posts': news, 'title': "novidades", 'company': getCompany()})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'news/novidades/post_detail.html', {'post': post, 'title': "novidades", 'company': getCompany()})
