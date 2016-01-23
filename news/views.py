# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Company, Photo
from .forms import FormPhoto
#from .forms import PostForm

# Create your views here.

def home(request):
    photos = Photo.objects.all() # Imagens dos slides
    # about = Company.objects.all() Usar depois pra pegar os textos do db
    text = Company.objects.all()[0]
    return render(request, 'news/index.html', {'photos': photos, 'title': "home", 'company': text})

def about(request):
    text = Company.objects.all()[0]
    return render(request, 'news/sobre/index.html', {'company': text, 'title': "sobre"}) # Textos do sobre

def contact(request):   # Formulario add foto
    text = Company.objects.all()[0]
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
    return render(request, 'news/contato/index.html', {'form': form, 'title': "contato", 'company': text})

def blog(request):   # Formulario contato
    text = Company.objects.all()[0]
    news = Post.objects.all()
    return render(request, 'news/novidades/index.html', {'posts': news, 'title': "novidades", 'company': text})

def post_detail(request, pk):
    text = Company.objects.all()[0]
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'news/novidades/post_detail.html', {'post': post, 'title': "novidades", 'company': text})
