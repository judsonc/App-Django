# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^sobre/$', views.about),
    url(r'^portfolio/$', views.portfolio),
    url(r'^servicos/$', views.services),
    url(r'^novidades/$', views.blog),
    url(r'^contato/$', views.contact),
]
