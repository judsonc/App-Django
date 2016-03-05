# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

handler404 = 'sitio.views.not_found_error'

urlpatterns = [
    url(r'^$', views.home),
    url(r'^sobre/$', views.about),
    url(r'^portfolio/$', views.portfolio),
    url(r'^servicos/$', views.services),
    url(r'^novidades/$', views.blog),
    url(r'^teste/$', views.teste),
]
